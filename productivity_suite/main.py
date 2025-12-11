# main.py
from calculator import calculator_menu
from notes_manager import NotesManager
from timer import timer_menu
from file_organizer import file_organizer_menu
from unit_converter import converter_menu

notes = NotesManager()

def main_menu():
    while True:
        print("""
==========================================
     PERSONAL PRODUCTIVITY SUITE
==========================================

MAIN MENU:
1. Calculator Tool
2. Notes Manager
3. Timer & Stopwatch
4. File Organizer
5. Unit Converter
6. Backup & Restore
7. Exit
""")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            calculator_menu()

        elif choice == "2":
            notes_menu()

        elif choice == "3":
            timer_menu()

        elif choice == "4":
            file_organizer_menu()

        elif choice == "5":
            converter_menu()

        elif choice == "6":
            print("Backups stored in: data/backups")
            input("Press Enter to continue...")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

def notes_menu():
    while True:
        print("""
NOTES MANAGER:
1. View All Notes
2. Add New Note
3. Search Notes
4. Edit Note
5. Delete Note
6. Export Notes
7. Back to Main Menu
""")

        choice = input("Enter choice: ")

        if choice == "1":
            for n in notes.view_notes():
                print(f"[{n['id']}] {n['title']} - {n['created']}")

        elif choice == "2":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            note = notes.add_note(title, content)

            print(f"\nNote added successfully!")
            print(f"Note ID: {note['id']}")
            print(f"Created: {note['created']}")

        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            results = notes.search_notes(keyword)
            for n in results:
                print(f"[{n['id']}] {n['title']}")

        elif choice == "4":
            note_id = int(input("Enter note ID to edit: "))
            new_title = input("New title: ")
            new_content = input("New content: ")
            if notes.edit_note(note_id, new_title, new_content):
                print("Note updated!")
            else:
                print("Invalid ID.")

        elif choice == "5":
            note_id = int(input("Enter note ID to delete: "))
            notes.delete_note(note_id)
            print("Note deleted.")

        elif choice == "6":
            file = notes.export_notes()
            print(f"Notes exported to {file}")

        elif choice == "7":
            break

        input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
