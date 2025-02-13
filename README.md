Task Manager CLI

Overview

A simple command-line task manager to help you keep track of your tasks. You can add, view, update, and delete tasks, as well as sort them by priority or deadline. Tasks are stored persistently using SQLite.

Features

✔️ Add tasks with descriptions, deadlines, and priority levels (High, Medium, Low).
✔️ View all tasks, pending or completed.
✔️ Sort tasks by deadline or priority.
✔️ Search for tasks by keyword.
✔️ See tasks that are due soon.
✔️ Mark tasks as completed or pending.
✔️ Delete tasks.

Getting Started

Requirements

Python 3.x installed on your system.


Installation & Usage

1. Clone or download this repository.


2. Open a terminal or command prompt in the project folder.


3. Run the program using:

python task_manager.py


4. Follow the menu prompts to manage your tasks.



How It Works

Enter a task description, optional deadline, and priority when adding a task.

Tasks are stored in an SQLite database (tasks.db) and persist even after the program is closed.

Use the menu options to view, update, search, and delete tasks.

When updating a task, enter "pending" or "completed" as the new status.


Example Usage

Task Manager  
1. Add a new task  
2. View all tasks  
3. Sort by deadline  
4. Sort by priority  
5. View pending tasks  
6. Mark task as completed  
7. Delete a task  
8. Exit  

Enter your choice: 1  
Task description: Complete project report  
Deadline (YYYY-MM-DD): 2025-02-15  
Priority (high/medium/low): high  
Task added successfully!

Notes

If you leave the deadline empty, it remains optional.

Task priorities help in sorting tasks efficiently.

Updating a task requires entering "pending" or "completed".


Contributing

Feel free to improve the project by adding new features or optimizing the code.

License

This project is free to use and modify.

