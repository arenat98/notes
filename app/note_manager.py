import json
from .note import Note
from datetime import datetime

class NoteManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = self.load_notes()
        self.next_id = len(self.notes) + 1

    def load_notes(self):
        try:
            with open(self.filename, "r") as file:
                notes_data = json.load(file)
                return [Note(**note_data) for note_data in notes_data]
        except FileNotFoundError:
            return []

    def save_notes(self):
        with open(self.filename, "w") as file:
            json.dump([note.to_dict() for note in self.notes], file)

    def add_note(self, title, body):
        note = Note(self.next_id, title, body)
        self.notes.append(note)
        self.next_id += 1
        self.save_notes()

    def edit_note(self, note_id, title, body):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = title
                note.body = body
                break
        self.save_notes()

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != note_id]
        self.save_notes()

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def get_all_notes(self):
        return self.notes
