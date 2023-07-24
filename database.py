import sqlite3

db=sqlite3.connect('todo_list.db')
c = db.cursor()

async def db_start():
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    done INTEGER DEFAULT 0
                 )''')
    db.commit()

def add_task_to_db(task_text):
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task_text,))
    db.commit()

def checker():
    c.execute("SELECT id FROM tasks")
    tasks = c.fetchall()
    db.commit()
    return [task[0] for task in tasks]

def checker_done(task_id):
    c.execute("SELECT done FROM tasks where id=?", (task_id,))
    tasks = c.fetchall()
    db.commit()
    return [task[0] for task in tasks]


def list_tasks_in_db():
    c.execute("SELECT id, task, done FROM tasks")
    tasks = c.fetchall()

    db.commit()
    return tasks

def update_task_status_in_db(task_id, status):
    c.execute("UPDATE tasks SET done = ? WHERE id = ?", (status, task_id))
    db.commit()

class TaskNotFoundError(Exception):
    pass

def delete_task_from_db(task_id):
    try:

        c.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
        task = c.fetchone()

        if not task:
            raise TaskNotFoundError(f"Task with ID {task_id} does not exist.")


        c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        db.commit()


        c.execute("SELECT id FROM tasks")
        remaining_tasks = c.fetchall()


        for index, (old_task_id,) in enumerate(remaining_tasks, start=1):
            c.execute("UPDATE tasks SET id = ? WHERE id = ?", (index, old_task_id))

        db.commit()
        print(f"Task with ID {task_id} has been deleted.")

    except ValueError:
        print(f"An error occurred while accessing the database:")

    except TaskNotFoundError as tnfe:
        print(f"Error: {tnfe}")



