import sqlite3
import datetime

def initialize_db():
    db_connect = sqlite3.connect("tasks.db")
    cursor = db_connect.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            deadline TEXT,
            status TEXT CHECK(status IN ('pending', 'completed')) NOT NULL DEFAULT 'pending',
            priority TEXT CHECK(priority IN ('high', 'medium', 'low')) NOT NULL DEFAULT 'medium')
    """)
    db_connect.commit()
    db_connect.close()

def add_task(description, deadline, priority):
    db_connect = sqlite3.connect("tasks.db")
    cursor = db_connect.cursor()
    cursor.execute("INSERT INTO tasks (description, deadline, status, priority) VALUES (?, ?, 'pending', ?)",
                   (description, deadline, priority))
    db_connect.commit()
    db_connect.close()

def view_tasks(order_by=None):
    db_connect = sqlite3.connect("tasks.db")
    cursor = db_connect.cursor()
    query = "SELECT * FROM tasks"
    
    if order_by == "deadline":
        query += " ORDER BY deadline ASC"
    elif order_by == "priority":
        query += " ORDER BY CASE priority WHEN 'high' THEN 1 WHEN 'medium' THEN 2 WHEN 'low' THEN 3 END"
    
    cursor.execute(query)
    tasks = cursor.fetchall()
    db_connect.close()

    for task in tasks:
        print(f"[{task[0]}] {task[1]} | Deadline: {task[2]} | Status: {task[3]} | Priority: {task[4]}")

def search_tasks(keyword):
    db_connect = sqlite3.connect("tasks.db")
    cursor = db_connect.cursor()
    cursor.execute("SELECT * FROM tasks WHERE description LIKE ?", ('%' + keyword + '%',))
    tasks = cursor.fetchall()
    db_connect.close()

    for task in tasks:
        print(f"[{task[0]}] {task[1]} | Deadline: {task[2]} | Status: {task[3]} | Priority: {task[4]}")

def view_due_soon():
    db_connect = sqlite3.connect("tasks.db")
    cursor = db_connect.cursor()
    tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    cursor.execute("SELECT * FROM tasks WHERE deadline <= ? AND status = 'pending'", (tomorrow,))
    tasks = cursor.fetchall()
    db_connect.close()

    for task in tasks:
        print(f"[{task[0]}] {task[1]} | Deadline: {task[2]} | Priority: {task[4]}")

def update_task(task_id, new_status):
    db_connect = sqlite3.connect("tasks.db")
    cursor = db_connect.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    db_connect.commit()
    db_connect.close()

def delete_task(task_id):
    db_connect = sqlite3.connect("tasks.db")
    cursor = db_connect.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db_connect.commit()
    db_connect.close()

def main():
    initialize_db()
    while True:
        print("\nTask Manager")
        print("1. Add task")
        print("2. View tasks")
        print("3. Search tasks")
        print("4. Sort by deadline")
        print("5. Sort by priority")
        print("6. Tasks due soon")
        print("7. Update task")
        print("8. Delete task")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            desc = input("Task description: ")
            deadline = input("Deadline (YYYY-MM-DD, optional): ")
            priority = input("Priority (high/medium/low): ").lower()
            if priority not in ["high", "medium", "low"]:
                priority = "medium"
            add_task(desc, deadline, priority)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            keyword = input("Search keyword: ")
            search_tasks(keyword)
        elif choice == "4":
            view_tasks(order_by="deadline")
        elif choice == "5":
            view_tasks(order_by="priority")
        elif choice == "6":
            view_due_soon()
        elif choice == "7":
            task_id = input("Task ID to update: ")
            new_status = input("New status (pending/completed): ").lower()
            update_task(task_id, new_status)
        elif choice == "8":
            task_id = input("Task ID to delete: ")
            delete_task(task_id)
        elif choice == "9":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()