# todos.py

import sqlite3

# Create or connect to the database
def create_connection():
    conn = sqlite3.connect('information.db')
    return conn

# Initialize the todos table
def init_todos_table():
    conn = create_connection()
    query = '''
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        completed INTEGER NOT NULL
    );
    '''
    conn.execute(query)
    conn.commit()
    conn.close()

# Add a to-do item
def add_todo(description):
    conn = create_connection()
    query = 'INSERT INTO todos (description, completed) VALUES (?, 0)'
    data = (description,)
    conn.execute(query, data)
    conn.commit()
    conn.close()

# View all to-do items
def view_todos():
    conn = create_connection()
    query = 'SELECT * FROM todos'
    cursor = conn.execute(query)
    todos = cursor.fetchall()
    conn.close()
    return todos

# Mark a to-do item as completed
def mark_todo_completed(todo_id):
    conn = create_connection()
    query = 'UPDATE todos SET completed=1 WHERE id=?'
    data = (todo_id,)
    conn.execute(query, data)
    conn.commit()
    conn.close()

# Delete a to-do item
def delete_todo(todo_id):
    conn = create_connection()
    query = 'DELETE FROM todos WHERE id=?'
    data = (todo_id,)
    conn.execute(query, data)
    conn.commit()
    conn.close()

# Uncomment the line below to initialize the todos table
# init_todos_table()
