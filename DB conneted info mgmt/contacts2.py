import sqlite3

# Create the Contacts table
def create_contacts_table():
    conn = sqlite3.connect('information.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Add a contact
def add_contact(name, phone, email):
    conn = sqlite3.connect('information.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
    conn.commit()
    conn.close()

# View all contacts
def view_contacts():
    conn = sqlite3.connect('information.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    conn.close()
    return contacts

# Search for a contact
def search_contact(name):
    conn = sqlite3.connect('information.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts WHERE name LIKE ?', ('%' + name + '%',))
    matching_contacts = cursor.fetchall()
    conn.close()
    return matching_contacts

# Edit or delete a contact
def edit_contact(contact_id, new_name, new_phone, new_email):
    conn = sqlite3.connect('information.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE contacts SET name=?, phone=?, email=? WHERE id=?', (new_name, new_phone, new_email, contact_id))
    conn.commit()
    conn.close()
