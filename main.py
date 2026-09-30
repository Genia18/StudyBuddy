print("Welcome to StudyBuddy")

tasks = []

while True:
    print(''' ===== STUDYBUDDY =====
    1. Add Task
    2. View Tasks
    3. Exit

    ''')

    choice = input("Enter your choice: ")
    # print(choice)
    # print(type(choice))


    if choice == "1":
        print("Add Task Selected")
        course = input("Enter course: ")
        description = input("Enter task description: ")
        deadline = input("Enter deadline: ")
        study_time = input("Enter study time (hours): ")
        priority = input("Enter priority (High/Medium/Low): ")

        task = {
            "ID" : len(tasks) + 1,
            "Course" : course,
            "Description" : description,
            "Deadline" : deadline,
            "Status" : "Pending",
            "Study Time" : study_time,
            "Priority" : priority
        }
        tasks.append(task)
        print("Task added successfully")

        print()


        

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

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")