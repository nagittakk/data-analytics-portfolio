"""
Task Manager

This program is designed specifically for businesses, enabling the efficient assignment and tracking of team 
responsibilities. It utilizes .txt files for seamless storage and updating of task-related information directly 
on the computer, promoting streamlined team coordination and productivity.
"""

# Import libraries
from datetime import datetime

# Defined Functions

def reg_user(new_user, usernames):
    """
    Registers a new user by adding their username and password to 'user.txt'.

    Parameters:
        new_user (str): The new username to register.
        usernames (list): A list of existing usernames to check against.

    Returns:
        str: Message indicating whether the new user's details were updated or not.
    """
    while True:
        # Check if username is already in use
        if new_user in usernames:
            new_user = input(f"\nThe username \"{new_user}\" is already in use. "
                             "Please enter an alternative username: ")
            continue
        else:
            # Prompt user to set a password and confirm it
            new_password = input("\nPlease enter the new user's password: ")
            confirm_password = input("\nPlease confirm the new password: ")
            if new_password == confirm_password:
                # Save new user details to 'user.txt'
                with open('user.txt', 'a+') as user_file:
                    user_file.write(f"\n{new_user}, {new_password}")

                # Confirmation message
                message = (f"\nNew user's login details have been updated:\n\nUsername: {new_user}\n"
                           f"Password: {new_password}")
                break
            else:
                # Password mismatch error message
                message = "\nThe passwords you have entered do not match. Failed to update new user's details."
                break

    return message


def add_task(task_user, task_title, task_description, due_date):
    """
    Adds a new task to 'tasks.txt' with the specified details.

    Parameters:
        task_user (str): Username to whom the task is assigned.
        task_title (str): Title of the task.
        task_description (str): Description of the task.
        due_date (str): Due date of the task.

    Returns:
        str: Message summarizing the new task details.
    """
    # Append new task details to 'tasks.txt'
    with open('tasks.txt', 'a+') as task_file:
        task_file.write(f"\n{task_user}, {task_title}, {task_description}, "
                        f"{datetime.today().strftime('%d %b %Y')}, {due_date}, No")

    # Confirmation message displaying task summary
    message = (f"New task details have been saved\n\nNew Task Summary\n"
               f"Task: {task_title}\nAssigned to: {task_user}\nDate assigned: "
               f"{datetime.today().strftime('%d %b %Y')}\nDue date: {due_date}\n"
               "Task complete? No\nTask description: {task_description}")

    return message


def view_all():
    """
    Reads all tasks from 'tasks.txt' and displays them.

    Returns:
        str: Message listing all tasks with total count.
    """
    # Read all lines in 'tasks.txt'
    with open('tasks.txt', 'r') as task_file:
        task_lines = task_file.readlines()

    tasks = ""  # Initialize empty string to hold task details
    count = 0  # Initialize counter for tasks

    # Loop through each line in the file and format the output
    for line in task_lines:
        count += 1
        temp = line.strip().split(', ')
        tasks += f"{str(count)}. {temp[1]}\n"

    # Return the formatted message
    message = f"\nAll Tasks ({count}):\n{tasks}"
    return message


def view_mine(username):
    """
    Displays tasks assigned to a specific user and allows updates to task status, assigned user, or due date.

    Parameters:
        username (str): The username of the user viewing their tasks.

    Returns:
        str: Summary of updates or changes made to tasks.
    """
    with open('tasks.txt', 'r') as task_file:
        task_lines = task_file.readlines()

    my_tasks = ""  # Initialize user's tasks summary
    count = 0  # Counter for user's tasks
    task_list = []  # List to store user's tasks
    other_tasks = []  # List for tasks assigned to other users

    # Organize tasks into user's and others' lists
    for line in task_lines:
        temp = line.strip().split(', ')
        if username in temp:
            count += 1
            my_tasks += f"{str(count)}. {temp[1]}\n"
            task_list.append(temp)
        else:
            other_tasks.append(temp)

    print(f"\nMy Tasks ({count}):\n{my_tasks}")

    while True:
        try:
            choice_task = int(input("Select a task number to edit or '-1' to exit 'View my tasks': "))

            # If a valid task number is chosen
            if 0 < choice_task <= count:
                chosen_list = task_list[choice_task - 1]
                if "Yes" in chosen_list:
                    message = f"\nThe task '{chosen_list[1]}' is completed and cannot be updated."
                else:
                    choice_changes = input(f"Select an option for task '{chosen_list[1]}':\n"
                                           "Update task status - ts\n"
                                           "Update task username - tu\n"
                                           "Update due date - td\n").lower()

                    # Update task status
                    if choice_changes == "ts":
                        status = input(f"Set task '{chosen_list[1]}' status to Yes? (Y/N): ").lower()
                        if status == "y":
                            chosen_list[5] = "Yes"
                            task_list[choice_task - 1] = chosen_list
                            message = f"Status for '{chosen_list[1]}' updated to 'Yes'."
                            combined_tasks = other_tasks + task_list
                            with open('tasks.txt', 'w') as task_file:
                                for task in combined_tasks:
                                    task_file.write(", ".join(task) + "\n")
                        else:
                            message = f"Task '{chosen_list[1]}' remains incomplete."

                    # Update assigned username
                    elif choice_changes == "tu":
                        username_transfer = input(f"Enter new username for task '{chosen_list[1]}': ")
                        chosen_list[0] = username_transfer
                        task_list[choice_task - 1] = chosen_list
                        combined_tasks = other_tasks + task_list
                        with open('tasks.txt', 'w') as task_file:
                            for task in combined_tasks:
                                task_file.write(", ".join(task) + "\n")
                        message = f"Task '{chosen_list[1]}' assigned to '{username_transfer}'."

                    # Update due date
                    elif choice_changes == "td":
                        new_date = input(f"Enter new due date for '{chosen_list[1]}' (dd mm yy): ")
                        chosen_list[4] = new_date
                        task_list[choice_task - 1] = chosen_list
                        combined_tasks = other_tasks + task_list
                        with open('tasks.txt', 'w') as task_file:
                            for task in combined_tasks:
                                task_file.write(", ".join(task) + "\n")
                        message = f"Due date for '{chosen_list[1]}' updated to '{new_date}'."
                break

            elif choice_task > count:
                print("\nInvalid entry. Please try again.")

            else:
                message = "Exiting 'View my tasks'."
                break

        except ValueError:
            print("Please enter a valid task number or '-1' to exit.")

    return message



import datetime


# Display stats function
def display_stats():
    """
    Displays task and user statistics from task_overview.txt and user_overview.txt files.
    
    Returns:
        message (str): Formatted statistics including task and user overview.
    """
    # Open task_overview.txt file for reading task statistics
    with open('task_overview.txt', 'r') as task_overview_file:
        task_o_lines = task_overview_file.readlines()

    # Loop through each line in task_overview.txt file
    for line in task_o_lines:
        task_stat = line.strip()  # Remove newline character
        task_stat = task_stat.split(', ')  # Split line to separate each stat

    # Open user_overview.txt file to read user statistics
    with open('user_overview.txt', 'r') as user_overview_file:
        user_o_lines = user_overview_file.readlines()

    user_o_list = []  # List to store each user statistic

    # Loop through each line in user_overview.txt file
    for line in user_o_lines:
        user_stat = line.strip()  # Remove newline character
        user_stat = user_stat.split(', ')  # Split line to separate each value
        user_o_list.append(user_stat)  # Append user statistics to the list
    
    # Format message with task and user statistics
    message = f'''
                Task Overview 
    
Number of tasks:                          {task_stat[0]}
Number of completed tasks:                {task_stat[1]}
Number on uncompleted tasks:              {task_stat[2]}
Number of tasks overdue and uncompleted:  {task_stat[3]}
% of uncompleted tasks:                   {task_stat[4]}
% of overdue tasks:                       {task_stat[5]} 

		User Overview			  '''
    
    for stat in user_o_list:
        message += f'''
        
Username - {stat[0]}
Number of tasks assigned to user:          {stat[1]}
% of all tasks assigned to user:           {stat[2]} 
% of tasks complete:                       {stat[3]} 
% of tasks uncompleted:                    {stat[4]} 
% of tasks overdue and uncompleted:        {stat[5]}'''
        
    return message


# generate reports function
def gen_report():
    """
    Generates reports based on tasks and users, calculating statistics and saving them to text files.
    
    Returns:
        str: Confirmation message indicating report generation completion.
    """
    # Open tasks.txt file to read task information
    with open('tasks.txt', 'r') as task_file:
        task_lines = task_file.readlines()  

    completed_tasks = 0  # Counter for completed tasks
    all_tasks = []  # List to store all tasks from tasks.txt file

    today = datetime.datetime.today()  # Today's date for comparison
    overdue = 0  # Counter for overdue tasks

    # Loop through each line in tasks.txt file
    for line in task_lines:
        temp = line.strip()  # Remove newline character
        temp = temp.split(', ')  # Split line for indexing
        all_tasks.append(temp)

        # Check if task is complete
        if temp[5] == "Yes":
            completed_tasks += 1  # Increment completed tasks counter

        # Check if task is overdue and incomplete
        if datetime.datetime.strptime(temp[4], '%d %b %Y') < today and temp[5] == "No":
            overdue += 1  # Increment overdue counter
        
        # Format task_overview report values
        task_report = f"{len(all_tasks)}, {completed_tasks}, {len(all_tasks) - completed_tasks}, {overdue}, {round(((len(all_tasks) - completed_tasks) / len(all_tasks)) * 100, 2)} %, {round((overdue / len(all_tasks)) * 100, 2)} %"

        # Write task overview report to task_overview.txt
        with open('task_overview.txt', 'w') as task_overview_file:
            task_overview_file.write(task_report) 

    # Open user.txt file to read user information
    with open('user.txt', 'r') as user_file: 
        user_lines = user_file.readlines()

    all_users = []  # List to store all users from user.txt file

    # Loop through each line in user.txt file
    for line in user_lines:
        temp = line.strip()  # Remove newline character
        temp = temp.split(', ')  # Split line for indexing
        all_users.append(temp)

    user_report = ""  # String to store each user's statistics
    count = 0  # Counter for user's tasks
    yes_count = 0  # Counter for user's completed tasks
    late_count = 0  # Counter for user's overdue tasks

    # Loop through each user and assign statistics
    for u in all_users: 
        for t in all_tasks:  # Loop through all tasks
            if u[0] in t:  # If user is assigned to task
                count += 1
                if t[5] == "Yes":  # If user's task is complete
                    yes_count += 1
                if datetime.datetime.strptime(t[4], '%d %b %Y') < today and t[5] == "No":  # If task is overdue and incomplete
                    late_count += 1
        # Format user_overview report values           
        user_report += f"{u[0]}, {count}, {round((count / len(all_tasks)) * 100, 2)} %, {round((yes_count / count) * 100, 2)} %, {round(100 - (yes_count / count) * 100, 2)} %, {round((late_count / count) * 100, 2)} %\n"
        
        # Reset counters for next user
        count = 0 
        yes_count = 0
        late_count = 0

    # Write user overview report to user_overview.txt
    with open('user_overview.txt', 'w') as user_overview_file:
        user_overview_file.write(user_report) 
        

    return "\nTask Overview and User Overview reports have been generated. To view them select 'display stats' from the main menu."


# ====Login Section====
# Start of main script after function definitions

# Open user.txt file to read user credentials
with open('user.txt', 'r') as users_file: 
    user_lines = users_file.readlines()

usernames = []  # List to store usernames from user.txt
passwords = []  # List to store passwords from user.txt
Logged_out = "\nYou have been logged out. Goodbye!!!"  # Logout message
return_to_menu = "\nWould you like to go back to the main menu? (Enter Y for yes, or N for no): "
invalid_entry = "\nYou have made entered an invalid input. Try again"

# Append usernames and passwords to lists
for line in user_lines:   
    temp = line.strip()  # Remove newline character
    temp = temp.split(', ')  # Split line for indexing
    usernames.append(temp[0])
    passwords.append(temp[1])

# Username verification loop
while True:
    username = input("Please enter your username: ")
    if username in usernames: 
        break
    else:
        print("\nYou have entered an invalid username!\n")
    continue

# Password verification loop
while True:
    password = input("\nPlease enter your password: ")
    if password in passwords:
        break
    else:
        print("\nYou have entered an invalid password!\n")
    continue

# Menu options for 'admin' user
if username == "admin":
    while True:
        menu = input('''\nMain Menu
        Select one of the following options: 
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        gr - generate reports
        ds - display statistics
        e - exit
        : ''').lower()    

        if menu == 'r':
            print(reg_user(input("\nPlease enter the new username: "), usernames))
            while True:
                back_to_menu = input(return_to_menu).lower()
                if back_to_menu == "y":
                    break
                elif back_to_menu == "n":
                    print(Logged_out)
                    exit()
                else:
                    print(invalid_entry)
        elif menu == 'a':
            print(add_task(input("\nPlease enter the username of the person to whom the task is to be assigned: "),input("\nPlease enter the title of the task: "), input("\nPlease enter the task description: "), input("\nPlease enter the due date for the task (format: dd mm yy - e.g. 26 Jan 2024): ")))
            while True:
                back_to_menu = input(return_to_menu).lower()
                if back_to_menu == "y":
                    break 
                elif back_to_menu == "n":
                    print(Logged_out) 
                    exit() 
                else:
                    print(invalid_entry) 
        elif menu == 'va':
            print(view_all()) 
            while True:
                back_to_menu = input(return_to_menu).lower()
                if back_to_menu == "y":
                    break 
                elif back_to_menu == "n":
                    print(Logged_out) 
                    exit() 
                else:
                    print(invalid_entry) 
        elif menu == 'vm':
            print(view_mine(username)) 
            while True:
                back_to_menu = input(return_to_menu).lower()
                if back_to_menu == "y":
                    break 
                elif back_to_menu == "n":
                    print(Logged_out) 
                    exit() 
                else:
                    print(invalid_entry) 
        elif menu == 'gr':
            print(gen_report()) 
            while True:
                back_to_menu = input(return_to_menu).lower()
                if back_to_menu == "y":
                    break 
                elif back_to_menu == "n":
                    print(Logged_out) 
                    exit() 
                else:
                    print(invalid_entry) 
        elif menu == 'ds':
            print(display_stats()) 
            while True:
                back_to_menu = input(return_to_menu).lower()
                if back_to_menu == "y":
                    break 
                elif back_to_menu == "n":
                    print(Logged_out) 
                    exit() 
                else:
                    print(invalid_entry) 
        elif menu == 'e':
            print(Logged_out) 
            exit() 
        else:
            print(invalid
