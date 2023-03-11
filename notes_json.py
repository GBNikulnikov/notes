import json
from global_def import *


def notes_write():
    with open("data/notes.json", "w") as write_file:
        json.dump(notes, write_file, indent=2)


def notes_read():
    with open("data/notes.json", "r") as read_file:
        notes = json.load(read_file)