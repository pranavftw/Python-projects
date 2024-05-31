import contacts
import appointments
import todos


def main():
    print("Welcome to the Personal Information Management Expert System!")
    while True:
        print("\nChoose an option:")
        print("1. Contacts Management")
        print("2. Appointments Management")
        print("3. To-Do List Management")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            contacts_management()
        elif choice == '2':
            appointments_management()
        elif choice == '3':
            todos_management()
        elif choice == '4':
            print("Thank you for using the Personal Information Management Expert System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


def contacts_management():
    while True:
        print("\nContacts Management:")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Edit a contact")
        print("5. Delete a contact")
        print("6. Go back")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            contacts.add_contact(name, phone, email)
            print("Contact added successfully.")
        elif choice == '2':
            all_contacts = contacts.view_contacts()
            print("\nAll Contacts:")
            for contact in all_contacts:
                print(f"Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")
        elif choice == '3':
            name = input("Enter contact name to search for: ")
            matching_contacts = contacts.search_contact(name)
            if matching_contacts:
                print("\nMatching contacts:")
                for contact in matching_contacts:
                    print(f"Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            contact_id = input("Enter the contact ID to edit: ")
            new_name = input("Enter new name (press Enter to keep current): ")
            new_phone = input("Enter new phone (press Enter to keep current): ")
            new_email = input("Enter new email (press Enter to keep current): ")
            contacts.edit_contact(contact_id, new_name, new_phone, new_email)
            print("Contact edited successfully.")
        elif choice == '5':
            contact_id = input("Enter the contact ID to delete: ")
            contacts.delete_contact(contact_id)
            print("Contact deleted successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a valid option.")


def appointments_management():
    while True:
        print("\nAppointments Management:")
        print("1. Add an appointment")
        print("2. View upcoming appointments")
        print("3. View appointments for a specific date")
        print("4. Edit an appointment")
        print("5. Delete an appointment")
        print("6. Go back")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            title = input("Enter appointment title: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM, press Enter for all-day): ")
            appointments.add_appointment(title, date, time)
            print("Appointment added successfully.")
        elif choice == '2':
            upcoming_appointments = appointments.view_upcoming_appointments()
            print("\nUpcoming Appointments:")
            for appointment in upcoming_appointments:
                print(f"Title: {appointment[1]}, Date: {appointment[2]}, Time: {appointment[3]}")
        elif choice == '3':
            date = input("Enter date to view appointments (YYYY-MM-DD): ")
            appointments_for_date = appointments.view_appointments_by_date(date)
            if appointments_for_date:
                print(f"\nAppointments for {date}:")
                for appointment in appointments_for_date:
                    print(f"Title: {appointment[1]}, Time: {appointment[3]}")
            else:
                print("No appointments found for the specified date.")
        elif choice == '4':
            appointment_id = input("Enter the appointment ID to edit: ")
            new_title = input("Enter new title (press Enter to keep current): ")
            new_date = input("Enter new date (YYYY-MM-DD, press Enter to keep current): ")
            new_time = input("Enter new time (HH:MM, press Enter to keep current): ")
            appointments.edit_appointment(appointment_id, new_title, new_date, new_time)
            print("Appointment edited successfully.")
        elif choice == '5':
            appointment_id = input("Enter the appointment ID to delete: ")
            appointments.delete_appointment(appointment_id)
            print("Appointment deleted successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a valid option.")


def todos_management():
    while True:
        print("\nTo-Do List Management:")
        print("1. Add a to-do item")
        print("2. View all to-do items")
        print("3. Mark a to-do item as completed")
        print("4. Delete a to-do item")
        print("5. Go back")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            description = input("Enter to-do item description: ")
            todos.add_todo(description)
            print("To-Do item added successfully.")
        elif choice == '2':
            all_todos = todos.view_todos()
            print("\nTo-Do List:")
            for todo in all_todos:
                status = "Completed" if todo[2] == 1 else "Not completed"
                print(f"Description: {todo[1]} ({status})")
        elif choice == '3':
            todo_id = input("Enter the ID of the to-do item to mark as completed: ")
            todos.mark_todo_completed(todo_id)
            print("To-Do item marked as completed.")
        elif choice == '4':
            todo_id = input("Enter the ID of the to-do item to delete: ")
            todos.delete_todo(todo_id)
            print("To-Do item deleted.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
