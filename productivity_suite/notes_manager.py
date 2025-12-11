# notes_manager.py
import json
import os
from datetime import datetime

DATA_FILE = "data/notes.json"
BACKUP_DIR = "data/backups"

class NotesManager:
    def __init__(self):
        os.makedirs("data", exist_ok=True)
        os.makedirs(BACKUP_DIR, exist_ok=True)
        self.notes = []
        self.load_notes()

    def add_note(self, title, content):
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.notes.append(note)
        self.save_notes()
        return note

    def save_notes(self):
        # create backup
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(BACKUP_DIR, f"backup_{timestamp}.json")
        with open(backup_file, "w") as bf:
            json.dump(self.notes, bf, indent=2)

        # save actual notes
        with open(DATA_FILE, "w") as f:
            json.dump(self.notes, f, indent=2)

    def load_notes(self):
        try:
            with open(DATA_FILE, "r") as f:
                self.notes = json.load(f)
        except FileNotFoundError:
            self.notes = []

    def view_notes(self):
        return self.notes

    def search_notes(self, keyword):
        return [n for n in self.notes if keyword.lower() in n["title"].lower()]

    def edit_note(self, note_id, new_title, new_content):
        for note in self.notes:
            if note["id"] == note_id:
                note["title"] = new_title
                note["content"] = new_content
                note["modified"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                return True
        return False

    def delete_note(self, note_id):
        self.notes = [n for n in self.notes if n["id"] != note_id]
        self.save_notes()

    def export_notes(self, filename="exported_notes.txt"):
        with open(filename, "w") as f:
            for n in self.notes:
                f.write(f"ID: {n['id']}\n")
                f.write(f"Title: {n['title']}\n")
                f.write(f"Content:\n{n['content']}\n")
                f.write("-" * 40 + "\n")
        return filename
