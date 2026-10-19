class Notebook:

    def __init__(self):
        self.notes = []

    def add_note(self,note):
        self.notes.append(note)

    def show_note(self):
        for i,note in enumerate(self.notes, start=1):
            print(f"Note {i} : {note}")


book = Notebook()
book.add_note("Buy Products")
book.add_note("Read Books")
book.add_note("Call the doctor")
book.show_note()