import json

print("Welcome to StudyBuddy")

# Save tasks into a JSON file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


# Load saved tasks from the JSON file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []


tasks = load_tasks()

while True:
    print(''' ===== STUDYBUDDY =====
    1. Add Task
    2. View Tasks
    3. Mark Task as Completed
    4. Exit

    ''')

    choice = input("Enter your choice: ")
    # print(choice)
    # print(type(choice))

    # Add a new task
    if choice == "1":
        print("Add Task Selected")

        course = input("Enter course: ")
        description = input("Enter task description: ")
        deadline = input("Enter deadline: ")
        study_time = input("Enter study time (hours): ")
        priority = input("Enter priority (High/Medium/Low): ")

        task = {
            "ID": len(tasks) + 1,
            "Course": course,
            "Description": description,
            "Deadline": deadline,
            "Status": "Pending",
            "Study Time": study_time,
            "Priority": priority
        }

        tasks.append(task)
        save_tasks()
        print("Task added successfully")

        print()

    # View existing tasks
    elif choice == "2":
        print("View Tasks Selected")

        if len(tasks) == 0:
            print("No tasks found.")

        else:
            print("===== YOUR TASKS =====")

            for task in tasks:
                print(f'''
                Task ID: {task["ID"]}
                Course: {task["Course"]}
                Description: {task["Description"]}
                Deadline: {task["Deadline"]}
                Status: {task["Status"]}
                Study Time: {task["Study Time"]}
                Priority: {task["Priority"]}
                -----------------------------
''')

    # Mark a task as completed
    elif choice == "3":
        task_completed_ID = int(input("Enter the ID of the Task you have completed: "))

        found = False

        for task in tasks:
            if task_completed_ID == task["ID"]:
                task["Status"] = "Completed"
                found = True
                break

        if found:
            save_tasks()
            print("Task completed successfully!")
        else:
            print("Task not found!")

    # Exit the program
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")

# Edit/Update Existing Tasks
edit_task_ID = int(input("Enter the ID of the task you want to edit: "))

found = False 

for task in tasks: 

    if edit_task_ID == task["ID"]:
        found = True
        break

if found: 
    print("Task found!")

    # Display the task's current information
    print("Current Task:")
    print(task)

    print("What would you like to edit?")
    print("1. Course")
    print("2. Description")
    print("3. Deadline")
    print("4. Status")

else: 
    print("Task not found!")


choice = input("Enter your choice (1-4): ")

if choice == "1":
    new_course = input("Enter the new course: ")
    task["Course"] = new_course
    #save_tasks()

    print("Task updated successfully!")
    print(task)
elif choice =="2":
    new_description = input("Enter the new description: ")
    task["Description"] = new_description
    #save_tasks()

    print("Task updated successfully!")
    print(task)
elif choice == "3":
    new_deadline = input("Enter the new deadline: ")
    task["Deadline"] = new_deadline
    #save_tasks()

    print("Task updated successfully!")
    print(task)
elif choice == "4":
    new_status = input("Enter the new status: ")
    task["Status"] = new_status

    #save_tasks()
    print("Task updated successfully!")
    print(task)
else :
    print("Invalid choice. Please enter a number from 1 to 4.")


# Save and confirm only after a valid choice
if choice in ("1", "2", "3", "4"):
    save_tasks()
    print("Task updated successfully!")
    print(task)