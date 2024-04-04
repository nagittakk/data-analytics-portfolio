'''
Database Querying

A user-friendly program for querying a HyperionDev-based database with the flexibility to select specific fields for display. 
After each query, users are prompted to save the results in either XML or JSON format, with the ability to customize the filename. 
This project aims to streamline database interactions and enhance data management capabilities for users.


'''

# impotr sqlite3
import sqlite3

# import json module
import json

# import xml.etree.ElementTree 
import xml.etree.ElementTree as ET

# import tabulate to  create tables to display data
from tabulate import tabulate


try:
    conn = sqlite3.connect("HyperionDev.db")
except sqlite3.Error:
    print("Please store your database as HyperionDev.db")
    quit()

cur = conn.cursor()


def usage_is_incorrect(input, num_args):
    if len(input) != num_args + 1:
        print(f"The {input[0]} command requires {num_args} arguments.")
        return True
    return False


def store_data_as_json(data, filename):

    # create dictionary from list
    
    headings = data[0] # separate list for keys
    rest_of_data = data[1:] # remove headings/keys from list
    count = 0 # set counter for inner dictionary entries
    dictionary = {} # create empty outer dictionary

    for i in rest_of_data: # loop through each list in data list
        count += 1 # increase counter by 1 for each inner list/entry
        i_dict = {} # empty inner list

        for j in range(len(headings)): # looping through vals for each key
            i_dict[headings[j]] = i[j] # add inner key:val pair to inner dictionary

        dictionary[f'{count}'] = i_dict # add inner dictionary to outer dictoinary
                   

    # create json string
    data_json = json.dumps(dictionary, sort_keys=True, indent=4)
    
    # write json string to json file 
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(data_json, outfile)

    # display message after file has been created
    print(f"\nThe file '{filename}' has been saved.")


def store_data_as_xml(data, filename, root_tag): 

    # save headings of list/ xml tree tags as separate list
    children = data[0] 

    # remove headings (children) list from data list
    rest_of_data = data[1:] 

    # --- create xml tree for data - for loop --- #

    # root element
    root = ET.Element(root_tag) 

    # counter for each data entry --> for multiple records
    count = 0 
    for s in rest_of_data:
        # condition that there are multiple records - numbered
        if len(rest_of_data) > 2: 
            count += 1
            # sub element - 'store records attributes'
            num = ET.SubElement(root, f'{count}') 
        
        # condition for single record
        else:
            count = 'info' 
            # sub element - 'store records attributes'
            num = ET.SubElement(root, f'{count}') 
        for i in range(len(s)):
            
            # storing each attribute
            ET.SubElement(num, children[i]).text = str(s[i])  
    
    # create elemet tree
    tree = ET.ElementTree(root) 

    # save element tree to .xml file
    tree.write(open(filename, 'a'), encoding='unicode') 
    
    # display message after file has been saved
    print(f"\nThe file '{filename}' has been saved.") 

    

def offer_to_store(data, root_tag):
    while True:
        
        print("\nWould you like to store this result?")
        choice = input("Y/[N]? : ").strip().lower()

        if choice == "y":
            
            filename = input("\nSpecify filename. Must end in .xml or .json: ")
            ext = filename.split(".")[-1]

            if ext == 'xml':
                store_data_as_xml(data, filename, root_tag)
                
                

            elif ext == 'json':
                store_data_as_json(data, filename)
                
                

            else:
                print("\nInvalid file extension. Please use .xml or .json")

        elif choice == 'n':
            break

        else:
            print("Invalid choice")


usage = '''
What would you like to do?

d - demo
vs <student_id>            - view subjects taken by a student
la <firstname> <surname>   - lookup address for a given firstname and surname
lr <student_id>            - list reviews for a given student_id
lc <teacher_id>            - list all courses taken by teacher_id
lnc                        - list all students who haven't completed their course
lf                         - list all students who have completed their course and achieved 30 or below
e                          - exit this program

Type your option here: '''


print("Welcome to the data querying app!")


while True:
    print()
    # Get input from user
    user_input = input(usage).split(" ")
    print()


    # Parse user input into command and args
    command = user_input[0]
    if len(user_input) > 1:
        args = user_input[1:]


    # demo - a nice bit of code from me to you - this prints all student names and surnames :)
    if command == 'd': 
        data = cur.execute("SELECT * FROM Student")
        for _, firstname, surname, _, _ in data:
            print(f"{firstname} {surname}")


    # view subjects by student_id
    elif command == 'vs': 
        if usage_is_incorrect(user_input, 1):
            continue
            
        student_id = args[0]

        # try-exception block incase user entry is invalid
        try:   
            # SQL query to get subject(s) of student with specified id --> join Course and StudentCourse tables
            cur.execute('''SELECT course_name FROM Course
                        LEFT JOIN StudentCourse
                        ON StudentCourse.course_code = Course.course_code
                        WHERE student_id = ?''', (student_id,))
            subjects = cur.fetchall()
    
        except Exception:
            print(f"Student with student ID '{student_id}' does not exist.")

        # display message of student subject(s)
        print(f"Subject(s) taken by student with student ID: '{student_id}':") 
        for count, sub in enumerate(subjects, start = 1 ):
            print(f"\n{count}. {sub[0]}") # printing of individual subjects

        # empty string to store subject(s) before storage in data list
        subs = "" 

        # for loop to create string of subject(s) 
        for i in range(len(subjects)): 
            if i == (len(subjects) -  1):
                subs += f"{subjects[i][0]}"
            else:
                subs += f"{subjects[i][0]}, "
        
        # store student subject data in list
        data = [['student_ID','subject(s)'],
            [student_id, subs]]
        
        # root tag if .xml format it selected to save the results as a file
        root_tag = 'student_subject(s)' 

        # offer to store data function
        offer_to_store(data, root_tag)
    

    # list address by name and surname
    elif command == 'la':
        if usage_is_incorrect(user_input, 2):
            continue
            
        firstname, surname = args[0].capitalize(), args[1].capitalize()

        # try-exception block incase user entry is invalid
        try: 
            # SQL query to get address of student with first name and surname 
            cur.execute('''SELECT street, city FROM Address
                        LEFT JOIN Student
                        ON Student.address_id = Address.address_id
                        WHERE first_name = ? AND last_name = ?''', (firstname, surname))
            address = cur.fetchall()

        except Exception:
            print(f"Student with first name '{firstname}' and Surname '{surname}' does not exist. (Check spelling and try again).")
            
        # display message of student address
        print(f"Address of student '{firstname} {surname}': {address[0][0]}, {address[0][1]} ") 

        # empty string to store address before storage in list
        location = f"{address[0][0]}, {address[0][1]}"
        
        # store student address data in data list
        data = [['first_name', 'surname', 'address'],
            [firstname, surname, address[0][1]]]

       # root tag if .xml format it selected to save the results as a file
        root_tag = 'student_address' 

        # offer to store data function
        offer_to_store(data, root_tag)
    

    # list reviews by student_id
    elif command == 'lr':
        if usage_is_incorrect(user_input, 1):
            continue
            
        student_id = args[0]
        
        # try-exception block incase user entry is invalid
        try:
            # SQL query to get student review(s) with student id --> join Review and Student tables
            cur.execute('''SELECT completeness, efficiency, documentation, review_text FROM Review 
                        LEFT JOIN Student
                        ON Student.student_id = Review.student_id
                        WHERE Review.student_id = ?''', (student_id,))
            review = cur.fetchall()

        except Exception:
            print(f"Student with student ID '{student_id}' does not exist. (Check the student ID and try again).")          
        
        # display message of student review data
        print(f"Feedback for student with student ID '{student_id}' :") 
        for count, r in enumerate(review, start = 1):
            print(f'''
Assignment {count}:\n
            Completeness - {r[0]}/4
            Efficiency - {r[1]}/4
            Documentation - {r[2]}/4
            Comments - {r[3]}\n''') # printing of review sections

        # store student review data in list
        data = [['completeness','efficiency','documentation','comments']] 
        for i in review:
            data.append(i)
        
        # root tag if .xml format it selected to save the results as a file
        root_tag = f'{student_id}_reviews' 

        # offer to store data function
        offer_to_store(data, root_tag)


     # list courses lectured by teacher according to teacher_id
    elif command == 'lc':
        if usage_is_incorrect(user_input, 1):
            continue
            
        teacher_id = args[0]
        
        # try-exception block incase user entry is invalid
        try:
            cur.execute('''SELECT course_name FROM Course 
                        WHERE teacher_id = ?''', (teacher_id,))
            courses = cur.fetchall()

        except Exception:
            print(f"Teacher with teacher ID '{teacher_id}' does not exist. (Check the teacher ID and try again).")
        
        # display message of teacher's course(s)
        print(f"Course(s) taught by teacher with teacher ID: '{teacher_id}':\n") 
        for count, course in enumerate(courses, start = 1 ):
            print(f"{count}. {course[0]}") # printing of course name(s)

        # empty string to store course(s) before storage in data list
        course = "" 

        # for loop to create string of course(s)
        for i in range(len(courses)): 
            if i == (len(courses) -  1):
                course += f"{courses[i][0]}"
            else:
                course += f"{courses[i][0]}, "
        
        # store teacher course data in list
        data = [['teacher_ID', 'course(s)'],
                [teacher_id, course]] 

        # root tag if .xml format it selected to save the results as a file
        root_tag = 'Teacher_course_info' 

        # offer to store data function
        offer_to_store(data, root_tag)


    elif command == 'lnc':# list all students who haven't completed their course
    
        # SQL query to get students whose courses are incomplete -- is_complete = 0 (FALSE) --> join Student, StudentCourse and Course tables
        cur.execute('''SELECT Student.student_id, first_name, last_name, email, course_name FROM Student
                    JOIN StudentCourse
                    ON StudentCourse.student_id = Student.student_id
                    JOIN Course
                    ON Course.course_code = StudentCourse.course_code
                    WHERE is_complete = ?''', (0,)) 
        incomplete = cur.fetchall()

        # create list for tale
        students = [['Student ID','First Name', 'Surname', 'Email Address', 'Course']]
        for i in incomplete:
            students.append(i)

        # display table of data
        print(f'''\n
                                     ___Students in Progress___
{tabulate(students, headers = 'firstrow', tablefmt = 'fancy_grid')}''')

        # store 'incomplete' data in list
        data = [['student_ID','first_name', 'surname', 'email_address', 'course']]
        for i in incomplete:
            data.append(i)
        
        # root tag if .xml format it selected to save the results as a file
        root_tag = 'students_in_progress' 
        

        # offer to store data function 
        offer_to_store(data, root_tag)


    # list all students who have completed their course and got a mark <= 30
    elif command == 'lf':

        # SQL query to get students whose final bark is 30 or lower --> join Student, StudntCourse and Course tables
        cur.execute('''SELECT Student.student_id, first_name, last_name, email, course_name, mark FROM Student
                    JOIN StudentCourse
                    ON StudentCourse.student_id = Student.student_id
                    JOIN Course
                    ON Course.course_code = StudentCourse.course_code
                    WHERE mark <= ?''', (30,)) 
        thirty_or_less = cur.fetchall()

        # create list for table - with headings
        students = [['Student ID','First Name', 'Surname', 'Email Address', 'Course', 'Mark']]
        for i in  thirty_or_less:
            students.append(i)

        # display table of data
        print(f'''\n
                        ___Students with a Final Mark of 30 or Less___
{tabulate(students, headers = 'firstrow', tablefmt = 'fancy_grid')}''')

        # store course final mark data in list
        data = [['student_ID','first_name', 'surname', 'email_address', 'course', 'mark']]
        for i in  thirty_or_less:
            data.append(i)
        
        # root tag if .xml format it selected to save the results as a file
        root_tag = 'final_mark_lower_than_30' 

        # offer to store data function   
        offer_to_store(data, root_tag)


    # exit
    elif command == 'e':
        print("Programme exited successfully!")
        break


    # error message --> incorrect command is entered
    else:
        print(f"Incorrect command: '{command}'")