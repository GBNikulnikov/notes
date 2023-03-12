import json
import global_def


def notes_write():
    with open("data/notes.json", "w") as write_file:
        json.dump(global_def.notes, write_file, indent=2)


def notes_read():
    with open("data/notes.json", "r") as read_file:
        return json.load(read_file)
