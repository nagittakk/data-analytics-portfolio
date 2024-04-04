'''
Task Managaer (modified)

This program is designed specifically for businesses, enabling the efficient assignment and tracking of team responsibilities. 
It utilizes .txt files for seamless storage and updating of task-related information directly on the computer,
promoting streamlined team coordination and productivity. Moreover, task management is enhanced through the 
integration of Python functions, enhancing code modularity for improved functionality.

'''

# notes, double ckeck file opns, double check printed formatting

#=====importing libraries===========
from datetime import datetime

# ==== defined functions ====

# reg_user functions
def reg_user(new_user, usernames): # function takes new user name and list of existing usernames
	while True:
		# check whether user name is alreaady in use
		if new_user in usernames:
			new_user = input(f"\nThe username \"{new_user}\" is already in use. Please enter an alternative user name: ")
			continue

		# new_user is not in usernames list	
		else: 
			new_password = input("\nPlease enter the new user's password: ") 
			confirm_password = input("\nPlease confirm the new password: ")
			# check for matching passwords
			if new_password == confirm_password:       # passwords do match          
									
				with open('user.txt', 'a+') as user_file: 
					user_file.write(f"\n{new_user}, {new_password}") # appending new user details to user.txt file

				# message showing summary of updated user details	
				message = f"\nNew user's login details have been updated:\n\nUsername: {new_user}\n\nPassword: {new_password}"
				break
				
			else: # passwords do not match + display message for passwords not matching
				message = f"\nThe passwords you have entered do not match. Failed to update new user's details."
				break
			
			
	return message



# add_task function
def add_task(task_user, task_title, task_description, due_date):

	# append new task to task.txt file - open to read and write (append)
	with open('tasks.txt', 'a+') as task_file: 
			task_file.write(f"\n{task_user}, {task_title}, {task_description}, {datetime.today().strftime('%d %b %Y')}, {due_date}, No")

	# display message after new task apended to task.txt file
	message = f'''New task details have been saved\n\n
			New Task Summary
                  
Task:			{task_title}
Assigned to:		{task_user}
Date assigned:		{datetime.today().strftime('%d %b %Y')}
Due date:		{due_date}
Task complete?		No
Task description:	{task_description}'''
	
	return message



# view_all function
def view_all():
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
	
	# display message of list of all tasks, with total tasks and tasks numbered
	message = (f"\nAll Tasks({count}):\n{tasks}")

	return message




# view_mine function
def view_mine(username):
	# opening task.txt file to read only
	with open('tasks.txt', 'r') as task_file: 
			task_lines = task_file.readlines()

	my_tasks = "" # empty user task string
	count = 0 # count for number of tasks
	task_list = [] # empty list for user tasks lists to be added to
	other_tasks = [] # empty list for tasks that do not belong to the user - to be added to task.txt after changes to user's tasks - overwritten to file

	# loop through each line in task.txt file
	for line in task_lines:
		temp = line.strip() # remove new line character
		temp = temp.split(', ') # separate each word in line to have a separate index that can be used 

		# condition for task belonging to user
		if username in temp:
			count += 1
			my_tasks += f"{str(count)}. {temp[1]}\n" # add user task to empty my_task string (numbered with count)
			task_list.append(temp)
		else:
			my_tasks = my_tasks # keep my_task string as is
			other_tasks.append(temp) # append tasks that do not belong to the user to the other tasks lists

	# display message of list of user's numbered tasks and task total
	print(f"\nMy Tasks({count}):\n{my_tasks}")

	choice_task = 0 # initialize choice of task to open while loop

	# while loop for valid entry for choice of task number
	while True:
		# user selcetion of task or to exit (as integer)
		choice_task = int(input('''\nSelect a task from your list of tasks to edit. Enter the task number or enter '-1' to to exit \'View my tasks\': ''')) 
		
		if choice_task > 0 and choice_task <= count: 

			chosen_list = task_list[choice_task-1] # task selection from list of task lines/lists (calc index from choice -1)

			# if statment to notify user whether updates can be made to the selected task based on the task status
			if "Yes" in chosen_list:
				message = f"\nThe task {chosen_list[1]} has already been completed and may not be updated."

			else: # updates can be made to the selected task

				choice_changes = input(f'''\nWhat changes would you like to make to the task '{chosen_list[1]}'? Select one of the following options:
							
			Update task completion status - ts
							
			Update task username - tu
							
			Update task due date - td
							
			:''').lower()

				# choice to update task status
				if choice_changes == "ts":
					# ask user whether they would like to update the task status to yes
					status = input(f"\nWould you like to update the completion status of the task '{chosen_list[1]}' to Yes? (Enter Y for yes or N for no): ").lower() 

					if status == "y": # task complete

						chosen_list[5] = "Yes" # update task status to 'yes'
						task_list[choice_task-1] = chosen_list # update the task list 
						

						message = f'''\nThe status for the task '{chosen_list[1]}' has been updated to \'Yes\'.\n 
		Updated Task summary
		
Task:				{chosen_list[1]}
Assigned to:		{chosen_list[0]}
Date assigned:		{chosen_list[3]}
Due date:		{chosen_list[4]}
Task complete?		Yes
Task description:	{chosen_list[2]}''' # display message for updated task

						# combined list of user's tasks and other users's tasks
						combined_tasks = other_tasks + task_list 

						# overwrite combined tasks to task.txt file - open for file writing only
						with open('tasks.txt', 'w') as task_file: 
							for task in combined_tasks: # for each task
								for i in range(0,6): # for detail item in the list (index)
									if i != 5: # for list index that isn't the last position (task status)
										task_file.write(f"{task[i]}, ") # write list index to file
									else:
										task_file.write(f"{task[i]}\n") # write list index to file + new line
						


					else: 
						message = f'''\nThe status for the task '{chosen_list[1]}' has been left as \'No\'.\n\n
		Task summary
		
Task:				{chosen_list[1]}
Assigned to:		{chosen_list[0]}
Date assigned:		{chosen_list[3]}
Due date:		{chosen_list[4]}
Task complete?		No
Task description:	{chosen_list[2]}''' # display message for unchanged task

				# choice to update task username
				elif choice_changes == "tu":

					# request for the username for task transfer
					username_transfer = input(f"\nEnter the username you would like to transfer the task '{chosen_list[1]}' to: ") 
					
					chosen_list[0] = username_transfer # update username in chosen task 
					task_list[choice_task-1] = chosen_list # update task list

					# combined list of user's tasks and other users's tasks
					combined_tasks = other_tasks + task_list

					# overwrite combined tasks to task.txt file - open for file writing
					with open('tasks.txt', 'w') as task_file: 
						for task in combined_tasks: # for each task 
								for i in range(0,6): # for detail item in the list (index)
									if i != 5: # for list index that isn't the last position (task status)
										task_file.write(f"{task[i]}, ") # write list index to file
									else:
										task_file.write(f"{task[i]}\n") # write list index to file + new line
									
								
					message = f'''\nThe task '{chosen_list[1]}' has been transfered to the username '{username_transfer}'.\n
		Updated Task summary
		
Task:				{chosen_list[1]}
Assigned to:		{chosen_list[0]}
Date assigned:		{chosen_list[3]}
Due date:		{chosen_list[4]}
Task complete?		No
Task description:	{chosen_list[2]}''' # display message for updated task

				# choice to update task due date
				elif choice_changes == "td":
					# request new due date from user
					new_date = input(f"\nEnter new due date for the task {chosen_list[1]} (format: dd mm yy - e.g. 26 Jan 2024): ")
					chosen_list[4] = new_date# update due date in chosen task 
					task_list[choice_task-1] = chosen_list # update task list

					# combined list of user's tasks and other users's tasks
					combined_tasks = other_tasks + task_list

					# overwrite all tasks to task.txt file - open for file writing
					with open('tasks.txt', 'w') as task_file: 
						for task in combined_tasks: # for each task 
								for i in range(0,6): # for detail item in the list (index)
									if i != 5: # for list index that isn't the last position (task status)
										task_file.write(f"{task[i]}, ") # write list index to file
									else:
										task_file.write(f"{task[i]}\n") # write list index to file + new line

					message = f'''\nThe due date for the task {chosen_list[2]} has been updated to {new_date}\n
		Updated Task summary
		
Task:				{chosen_list[1]}
Assigned to:		{chosen_list[0]}
Date assigned:		{chosen_list[3]}
Due date:		{chosen_list[4]}
Task complete?		No
Task description:	{chosen_list[2]}''' # display message for updated task
			break

		elif choice_task > count:
			print ("\nInvalid entry. Please try again. ")
			

		else:
			message = "..."
			break
			

	return message



 # display stats function
def display_stats():
    with open('task_overview.txt', 'r') as task_overview_file:
        task_o_lines = task_overview_file.readlines()

    # loop through each line in task_overview.txt file
    for line in task_o_lines:
        task_stat = line.strip() # remove new line character
        task_stat = task_stat.split(', ') # separate each stat in line to have a separate index values that can be called

    # opening user_overview.txt file to read only
    with open('user_overview.txt', 'r') as user_overview_file:
        user_o_lines = user_overview_file.readlines()

    user_o_list = []     # empty list to add each task to for counting

    # loop through each line in user_ovrtview.txt file
    for line in user_o_lines:
        user_stat = line.strip() # remove new line character
        user_stat = user_stat.split(', ') # separate each word in line to have a separate index that can be used
        user_o_list.append(user_stat) # append task to user_o_list
    
    message = f'''
                Task Overview 
    
Number of tasks:                          {task_stat[0]}
Number of completed tasks:                {task_stat[1]}
Number on uncompleted tasks:              {task_stat[2]}
Number of tasks overdue and uncompleted:  {task_stat[3]}
% of uncompleted tasks:                   {task_stat[4]}
% of overdue tasks:                       {task_stat[5]} 

		User Overview			  ''' # display of task overview/statistics

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
    # open task text file to read info
    with open('tasks.txt', 'r') as task_file:
        task_lines = task_file.readlines()  

    completed_tasks = 0 # completed tasks counter - initialize outside of loop
    all_tasks = [] # empty list to store all tasks from the task file

    today = datetime.today() # todays date to compare task dates with
    overdue = 0 # overdue tasks counter

    # loop through each line in task.txt file
    for line in task_lines:
        temp = line.strip() # remove new line character
        temp = temp.split(', ') # separate each word in line to have a separate index that can be used 
        all_tasks.append(temp)

        # if statemtment for completes tasks
        if temp[5] == "Yes": # check whether task is complete
            completed_tasks += 1 # increase complete tasks counter by 1 if task is complete

        if datetime.strptime(temp[4], '%d %b %Y') < today and temp[5] == "No": # compare task date with today's date
            overdue += 1 # increase overdue counter by 1 if task is date is before today's date
        
        # task_overview report values
        task_report = f"{str(len(all_tasks))}, {str(completed_tasks)}, {str(len(all_tasks) - completed_tasks)}, {str(overdue)}, {str(round(((len(all_tasks) - completed_tasks) / len(all_tasks)) * 100,2))} %, {str(round((overdue / len(all_tasks)) * 100,2))} %"

        # write task_overview report values to task_overview_file - create and overwrite text file
        with open('task_overview.txt', 'w') as task_overview_file:
            task_overview_file.write(task_report) 

    # open user text file to read info
    with open('user.txt', 'r') as user_file: 
        user_lines = user_file.readlines()

        all_users = [] # empty list to store all users from the user file

        # loop through each line in user.txt file
        for line in user_lines:
            temp = line.strip() # remove new line character
            temp = temp.split(', ') # separate each word in line to have a separate index that can be used 
            all_users.append(temp)

        user_report = "" # empty string for stats of each user
        count = 0 # user's task counter
        yes_count = 0 # user's complete tasks counter
        late_count = 0 # user's overdue and uncomplete task counter

        # for loop to asign stats to each user
        for u in all_users: 
            for t in all_tasks: # for all the tasks
                if u[0] in t: # if the user is in the task
                    count += 1
                    if t[5] == "Yes": # is user task is complete
                        yes_count += 1
                    if datetime.strptime(t[4], '%d %b %Y') < today and t[5] == "No": # if due date is before today's date and task is uncomplete
                        late_count += 1
            # user_overview report values            
            user_report += f"{u[0]}, {count}, {str(round((count / len(all_tasks)) * 100,2))} %, {str(round((yes_count/count) * 100,2))} %, {str(round(100 - (yes_count/count) * 100,2))} %, {str(round((late_count/count) * 100,2))} %\n"
            
            # start counters at 0 for next user
            count = 0 
            yes_count = 0
            late_count = 0

    # write user_overview report to task_overview_file - create and overwrite text file
    with open('user_overview.txt', 'w') as user_overview_file:
        user_overview_file.write(user_report) 
        


    return "\nTask Overview and User Overview reports have been generated. To view them select 'display stats' from the main menu. " # display message for generated reports


#====Login Section====
# open user.txt file to read only
with open('user.txt', 'r') as users_file: 
    user_lines = users_file.readlines()


usernames = [] # empty list to store usernames from user.txt file
passwords = [] # empty list to store passwords from user.txt file
Logged_out = "\nYou have been logged out. Goodbye!!!" # message to display when user is logged out from program
return_to_menu = "\nWould you like to go back to the main menu? (Enter Y for yes, or N for no): "
invalid_entry = "\nYou have made entered an invalid input. Try again"

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
        password = " "
    continue



# condition nest/block for user with 'admin' username, with menu that includes the option to register a new user
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

        # if block for registering a new user
        if menu == 'r':

            # use reg_user function to register new user
            print(reg_user(input("\nPlease enter the new username: "), usernames))

            # while loop for prompt to return to main menu or not 
            while True:
                back_to_menu = input(return_to_menu).lower()
                if back_to_menu == "y":
                    break # close inner loop and return to main menu (outer loop)
                elif back_to_menu == "n":
                    print(Logged_out) # user to be logged out with display message
                    exit() # exit the main while loop
                else:
                    print(invalid_entry) # error message for invalid entry
                
        # elif block for adding new task
        elif menu == 'a':
            
            # use add_task function to add task
            print(add_task(input("\nPlease enter the username of the person to whom the task is to be assigned: "),input("\nPlease enter the title of the task: "), input("\nPlease enter the task description: "), input("\nPlease enter the due date for the task (format: dd mm yy - e.g. 26 Jan 2024): ")))
             
            # while loop for prompt to return to main menu or not 
            while True:
                back_to_menu = input(return_to_menu).lower()
                if back_to_menu == "y":
                    break 
                elif back_to_menu == "n":
                    print(Logged_out) 
                    exit() 
                else:
                    print(invalid_entry) 

        # elif block for viewing all tasks
        elif menu == 'va':

            # use view_all function to view all tasks
            print(view_all()) 

            # while loop for prompt to return to main menu or not 
            while True:
                back_to_menu = input(return_to_menu).lower()
                if back_to_menu == "y":
                    break 
                elif back_to_menu == "n":
                    print(Logged_out) 
                    exit() 
                else:
                    print(invalid_entry) 
        
        # elif block for viewing user's/my tasks
        elif menu == 'vm':

            # use view_mine function to view users tasks 
            print(view_mine(username)) 

            # while loop for prompt to return to main menu or not 
            while True:
                back_to_menu = input(return_to_menu).lower()
                if back_to_menu == "y":
                    break 
                elif back_to_menu == "n":
                    print(Logged_out) 
                    exit() 
                else:
                    print(invalid_entry) 

		# elif statement for 'admin' to generate reports
        elif menu == 'gr':
            
            # use gen_report fucntoin to generate task_overview and user_overview reports from task_manager.py
            print(gen_report()) 
            
            # while loop for prompt to return to main menu or not 
            while True:
                back_to_menu = input(return_to_menu).lower()
                if back_to_menu == "y":
                    break 
                elif back_to_menu == "n":
                    print(Logged_out) 
                    exit() 
                else:
                    print(invalid_entry)


        # elif statement for 'admin' to view statistics
        elif menu == 'ds':
            
            # use display_stats fucntoin to displays task_manager.py stats
            print(display_stats())
            
            # while loop for prompt to return to main menu or not 
            while True:
                back_to_menu = input(return_to_menu).lower()
                if back_to_menu == "y":
                    break 
                elif back_to_menu == "n":
                    print(Logged_out) 
                    exit() 
                else:
                    print(invalid_entry) 

		# elif statement for user choosing to exit program
        elif menu == 'e':
            print(Logged_out) # user log out display message
            exit() # exit the main while loop


        else:
            print(invalid_entry) # invalid entry by user at main menu

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


        elif menu == 'e':
            print(Logged_out)
            exit()

        else:
            print(invalid_entry)