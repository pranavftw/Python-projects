import sqlite3

# Create or connect to the database
def create_connection():
    conn = sqlite3.connect('information.db')
    return conn

# Initialize the contacts table
def init_contacts_table():
    conn = create_connection()
    query = '''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL,
        category TEXT DEFAULT 'General'
    );
    '''
    conn.execute(query)
    conn.commit()
    conn.close()

# Add a contact
def add_contact(name, phone, email, category='General'):
    conn = create_connection()
    query = 'INSERT INTO contacts (name, phone, email, category) VALUES (?, ?, ?, ?)'
    data = (name, phone, email, category)
    conn.execute(query, data)
    conn.commit()
    conn.close()

# View all contacts
def view_contacts():
    conn = create_connection()
    query = 'SELECT * FROM contacts'
    cursor = conn.execute(query)
    contacts = cursor.fetchall()
    conn.close()
    return contacts

# Search for a contact by name
def search_contact(name):
    conn = create_connection()
    query = 'SELECT * FROM contacts WHERE name LIKE ?'
    data = ('%' + name + '%',)
    cursor = conn.execute(query, data)
    matching_contacts = cursor.fetchall()
    conn.close()
    return matching_contacts

# Edit a contact
def edit_contact(contact_id, new_name, new_phone, new_email, new_category):
    conn = create_connection()
    query = 'UPDATE contacts SET name=?, phone=?, email=?, category=? WHERE id=?'
    data = (new_name, new_phone, new_email, new_category, contact_id)
    conn.execute(query, data)
    conn.commit()
    conn.close()

# Delete a contact
def delete_contact(contact_id):
    conn = create_connection()
    query = 'DELETE FROM contacts WHERE id=?'
    data = (contact_id,)
    conn.execute(query, data)
    conn.commit()
    conn.close()

