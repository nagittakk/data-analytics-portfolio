'''
Task Manager

This program is tailored for businesses, facilitating efficient assignment and tracking of team responsibilities. 
This project underscores the utilization of .txt files for seamless storage and updating of task-related information 
directly on the computer, ensuring streamlined team coordination and productivity.

'''


#=====importing libraries===========
from datetime import date

#====Login Section====
# open user.txt file to read only
with open('user.txt', 'r') as users_file: 
    user_lines = users_file.readlines()

usernames = [] # empty list to store usernames from user.txt file
passwords = [] # empty list to store passwords from user.txt file
Logged_out = "\nYou have been logged out. Goodbye!!!" # message to display when user is logged out from program

# block for appending usernames and passwords to empty list
for line in user_lines:   
    temp = line.strip() # remove new line character
    temp = temp.split(', ') # separate each word in line to have a separate index that can be used
    usernames.append(temp[0])
    passwords.append(temp[1])

# while loop to check if username exists in list
while True:
    username = input("Please enter your username: ") # username exists 
    if username in usernames: 
        break
    else:
        print("\nYou have entered an invalid username!\n") # username doesn't exist, error message
        username = " "
    continue

# while loop to check if password exists in list
while True:
    password = input("\nPlease enter your password: ") # password exists
    if password in passwords:
        break
    else:
        print("\nYou have entered an invalid password!\n") # password doesn't exist, error message
        username = " "
    continue

# condition nest/block for user with 'admin' username, with menu that includes the option to register a new user
if username == "admin":
    while True:
        menu = input('''\nSelect one of the following options: 
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        s - statistics
        e - exit
        : ''').lower()    

        # if block for registering a new user
        if menu == 'r':
            new_user = input("\nPlease enter the new username: ") # request new usersame
            new_password = input("\nPlease enter the new password: ") # request new password
            confirm_password = input("\nPlease confirm the new password: ") # requwat confirmation of new password

            # check for matching passwords
            if new_password == confirm_password:       # passwords do match                
                
                with open('user.txt', 'a+') as file: 
                    file.write(f"\n{new_user}, {new_password}") # appending new user details to user.txt file

                print(f'''\nNew user's login details have been updated:\n
Username: {new_user}\n
Password: {new_password}''') # message showing summary of updated user details

                # while loop for prompt to return to main menu or not 
                while True:
                    back_to_menu = input("\nWould you like to go back to the main menu? (Enter Y for yes, or N for no): ").lower()
                    if back_to_menu == "y":
                        break # close inner loop and return to main menu (outer loop)
                    elif back_to_menu == "n":
                        print(Logged_out) # user to be logged out with display message
                        exit() # exit the main while loop
                    else:
                        print("\nYou have made entered an invalid input. Try again") # error message for invalid entry
                    
            else: # passwords do not match
                print("\nThe passwords you have entered do not match."
                      " Failed to update new user's details.") # display message for passwords not matching
                
                # while loop for prompt to return to main menu or not 
                while True:
                    back_to_menu = input("\nWould you like to go back to the main menu? (Enter Y for yes, or N for no): ").lower()
                    if back_to_menu == "y":
                        break # # close inner loop and return to main menu (outer loop)
                    elif back_to_menu == "n":
                        print(Logged_out) # user to be logged out with display message
                        exit() # exit the main while loop
                    else:
                        print("\nYou have made entered an invalid input. Try again") # error message for invalid entry
                
        # elif block for adding new task
        elif menu == 'a':
            task_user = input("\nPlease enter the username of the person to whom the task is to be assigned: ") # request task user
            task_title = input("\nPlease enter the title of the task: ") # request task title
            task_description = input("\nPlease enter the task description: ") # request Task description
            due_date = input("\nPlease enter the due date for the task (format: dd mm yy - e.g. 26 Jan 2024): ") # request task due date

            # append new task to task.txt file - open to read and write (append)
            with open('tasks.txt', 'a+') as user_file: 
                    user_file.write(f"\n{task_user}, {task_title}, {task_description}, {date.today().strftime('%d %b %Y')}, {due_date}, No")

            # display message after new task apended to task.txt file
            print(f'''\nNew task details have been saved\n
        New Task Summary\n\n
Task:\t\t\t{task_title}\n
Assigned to:\t\t{task_user}\n
Date assigned:\t\t{date.today().strftime('%d %b %Y')}\n
Due date:\t\t{due_date}\n
Task complete?\t\tNo\n
Task description:\t{task_description}''')
             
            # while loop for prompt to return to main menu or not 
            while True:
                back_to_menu = input("\nWould you like to go back to the main menu? (Enter Y for yes, or N for no): ").lower()
                if back_to_menu == "y":
                    break # close inner loop and return to main menu (outer loop)
                elif back_to_menu == "n":
                    print(Logged_out) # user to be logged out with display message
                    exit() # exit the main while loop
                else:
                    print("\nYou have made entered an invalid input. Try again") # error message for invalid entry 

        # elif block for viewing all tasks
        elif menu == 'va':
            # opening task.txt file to read only
            with open('tasks.txt', 'r') as task_file: 
                task_lines = task_file.readlines()

            tasks = "" # empty task string
            count = 0 # counter for no. of tasks

            # loop through each line in task.txt file 
            for line in task_lines:
                count += 1
                temp = line.strip() # remove new line character
                temp = temp.split(', ') # separate each word in line to have a separate index that can be used
                tasks += f"{str(count)}. {temp[1]}\n" # add tasks to empty task string (numbered with count)
            
            # display list of all tasks, with total tasks and tasks numbered
            print(f"\nAll Tasks({count}):\n{tasks}") 

            # while loop for prompt to return to main menu or not 
            while True:
                back_to_menu = input("\nWould you like to go back to the main menu? (Enter Y for yes, or N for no): ").lower()
                if back_to_menu == "y":
                    break # close inner loop and return to main menu (outer loop)
                elif back_to_menu == "n":
                    print(Logged_out) # user to be logged out with display message
                    exit() # exit the main while loop
                else:
                    print("\nYou have made entered an invalid input. Try again") # error message for invalid entry
        
        # elif block for viewing user's/my tasks
        elif menu == 'vm':
            # opening task.txt file to read only
            with open('tasks.txt', 'r') as task_file: 
                    task_lines = task_file.readlines()

            my_tasks = "" # empty user task string
            count = 0 # count for number of tasks

            # loop throuhg each line in task.txt file
            for line in task_lines:
                temp = line.strip() # remove new line character
                temp = temp.split(', ') # separate each word in line to have a separate index that can be used

                # condition for task belonging to user
                if username in temp:
                    count += 1
                    my_tasks += f"{str(count)}. {temp[1]}\n" # add user task to empty my_task string (numbered with count)
                else:
                    my_tasks = my_tasks # keep my_task string as is

            # display list of user's numbered tasks and task total
            print(f"\nMy Tasks({count}):\n{my_tasks}") 

            # while loop for prompt to return to main menu or not 
            while True:
                back_to_menu = input("\nWould you like to go back to the main menu? (Enter Y for yes, or N for no): ").lower()
                if back_to_menu == "y":
                    break # close inner loop and return to main menu (outer loop)
                elif back_to_menu == "n":
                    print(Logged_out) # user to be logged out with display message
                    exit() # exit the main while loop
                else:
                    print("\nYou have made entered an invalid input. Try again") # error message for invalid entry 

        # elif statement for user choosing to exit program
        elif menu == 'e':
            print(Logged_out) # user log out display message
            exit() # exit the main while loop

        # elif statement for 'admin' to view statistics
        elif menu == 's':
            # opening task.txt file to read only
            with open('tasks.txt', 'r') as task_file: 
                    task_lines = task_file.readlines()

            task_list = []     # empty list to add each task to for counting

            # loop throuhg each line in task.txt file
            for line in task_lines:
                temp = line.strip() # remove new line character
                temp = temp.split(', ') # separate each word in line to have a separate index that can be used
                task_list.append(temp[0]) # append task to task list for counting (index doesn'r really matter)

            # opening user.txt file to read only
            with open('tasks.txt', 'r') as task_file: 
                    task_lines = task_file.readlines()

            user_list = []     # empty list to add each task to for counting

            # loop throuhg each line in user.txt file
            for line in task_lines:
                temp = line.strip() # remove new line character
                temp = temp.split(', ') # separate each word in line to have a separate index that can be used
                user_list.append(temp[0]) # append task to user list for counting(index doesn'r really matter)

            print(f'''Statistics\n
Number of tasks: {str(len(task_list))}\n\n
Number of users: {str(len(user_list))}''') # display of task and user statistics - counting of users and tasks
            
            # while loop for prompt to return to main menu or not 
            while True:
                back_to_menu = input("\nWould you like to go back to the main menu? (Enter Y for yes, or N for no): ").lower()
                if back_to_menu == "y":
                    break # close inner loop and return to main menu (outer loop)
                elif back_to_menu == "n":
                    print(Logged_out) # user to be logged out with display message
                    exit() # exit the main while loop
                else:
                    print("\nYou have made entered an invalid input. Try again") # error message for invalid entry


        else:
            print("\nYou have made entered an invalid input. Please try again.") # invalid entry by user at main menu

# condition nest/block for user with username that is NOT 'admin, with menu that excludes the option to register a new user
# code is exactly the same as above but without register user block (f menu == 'r') 
else:
    while True:
        menu = input('''\nSelect one of the following options:
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit
        : ''').lower()                

        if menu == 'a':
            task_user = input("\nPlease enter the username of the person to whom the task is to be assigned: ")
            task_title = input("\nPlease enter the title of the task: ")   
            task_description = input("\nPlease enter the task description: ")
            due_date = input("\nPlease enter the due date for the task (format: dd mm yy - e.g. 26 Jan 2024): ")

            with open('tasks.txt', 'a+') as user_file: 
                    user_file.write(f"\n{task_user}, {task_title}, {task_description}, {date.today().strftime('%d %b %Y')}, {due_date}, No")

            print(f'''\nNew task details have been saved\n
        New Task Summary\n\n
Task:\t\t\t{task_title}\n
Assigned to:\t\t{task_user}\n
Date assigned:\t\t{date.today().strftime('%d %b %Y')}\n
Due date:\t\t{due_date}\n
Task complete?\t\tNo\n
Task description:\t{task_description}''')

            while True:
                back_to_menu = input("\nWould you like to go back to the main menu? (Enter Y for yes, or N for no): ").lower()
                if back_to_menu == "y":
                    break
                elif back_to_menu == "n":
                    print(Logged_out) 
                    exit() 
                else:
                    print("\nYou have made entered an invalid input. Try again") 


        elif menu == 'va':
            with open('tasks.txt', 'r') as task_file: 
                task_lines = task_file.readlines()

            tasks = ""
            count = 0

            for line in task_lines:
                count += 1
                temp = line.strip() # remove new line character
                temp = temp.split(', ') # separate each word in line to have a separate index that can be used
                tasks += f"{str(count)}. {temp[1]}\n"
                
            print(f"\nAll Tasks({count}):\n{tasks}") 

            while True:
                back_to_menu = input("\nWould you like to go back to the main menu? (Enter Y for yes, or N for no): ").lower()
                if back_to_menu == "y":
                    break 
                elif back_to_menu == "n":
                    print(Logged_out) 
                    exit() 
                else:
                    print("\nYou have made entered an invalid input. Try again") 
        

        elif menu == 'vm':
            with open('tasks.txt', 'r') as task_file: 
                    task_lines = task_file.readlines()

            my_tasks = ""
            count = 0

            for line in task_lines:
                temp = line.strip() 
                temp = temp.split(', ') 

                if username in temp:
                    count += 1
                    my_tasks += f"{str(count)}. {temp[1]}\n"
                else:
                    my_tasks = my_tasks

            print(f"\nMy Tasks({count}):\n{my_tasks}")

            while True:
                back_to_menu = input("\nWould you like to go back to the main menu? (Enter Y for yes, or N for no): ").lower()
                if back_to_menu == "y":
                    break 
                elif back_to_menu == "n":
                    print(Logged_out) 
                    exit() 
                else:
                    print("\nYou have made entered an invalid input. Try again")


        elif menu == 'e':
            print(Logged_out)
            exit()

        else:
            print("\nYou have made entered an invalid input. Please try again.")