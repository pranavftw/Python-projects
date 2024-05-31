import sqlite3

# Create the Appointments table
def create_appointments_table():
    conn = sqlite3.connect('information.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            date DATE NOT NULL,
            time TIME
        )
    ''')
    conn.commit()
    conn.close()

# Add an appointment
def add_appointment(title, date, time):
    conn = sqlite3.connect('information.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO appointments (title, date, time) VALUES (?, ?, ?)', (title, date, time))
    conn.commit()
    conn.close()

# View upcoming appointments
def view_upcoming_appointments():
    conn = sqlite3.connect('information.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM appointments WHERE date >= CURRENT_DATE ORDER BY date, time')
    upcoming_appointments = cursor.fetchall()
    conn.close()
    return upcoming_appointments

# View appointments for a specific date
def view_appointments_by_date(date):
    conn = sqlite3.connect('information.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM appointments WHERE date = ? ORDER BY time', (date,))
    appointments = cursor.fetchall()
    conn.close()
    return appointments

# Edit or delete an appointment
def edit_appointment(appointment_id, new_title, new_date, new_time):
    conn = sqlite3.connect('information.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE appointments SET title=?, date=?, time=? WHERE id=?', (new_title, new_date, new_time, appointment_id))
    conn.commit()
    conn.close()


def delete_appointment(appointment_id):
    return None