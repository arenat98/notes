from datetime import datetime

class Note:
    def __init__(self, note_id, title, body, timestamp=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp if timestamp else datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):
        return {
            "note_id": self.note_id,
            "title": self.title,
            "body": self.body,
            "timestamp": self.timestamp
        }
