import tkinter as tk
from tkinter import simpledialog, messagebox
import os

class NotebookManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Notebook Manager")
        self.root.geometry("600x400")
        self.root.configure(bg="#FFD700")  

        self.label = tk.Label(root, text="My Notes", font=("Comic Sans MS", 20), bg="#FFD700", fg="#8B008B")  
        self.label.pack(pady=10)

        self.notes_listbox = tk.Listbox(root, font=("Comic Sans MS", 12), height=10, width=50, bg="#FFFACD", fg="#8B4513")  
        self.notes_listbox.pack(pady=10)

        self.button_frame = tk.Frame(root, bg="#FFD700")
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Note", font=("Comic Sans MS", 12), bg="#FF69B4", fg="#FFFFFF", command=self.add_note) 
        self.add_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Note", font=("Comic Sans MS", 12), bg="#FF69B4", fg="#FFFFFF", command=self.delete_note)
        self.delete_button.grid(row=0, column=1, padx=5)

        self.notes_dir = "notes"
        os.makedirs(self.notes_dir, exist_ok=True)
        self.load_notes()

    def load_notes(self):
        self.notes_listbox.delete(0, tk.END)
        notes = [note.replace(".txt", "") for note in os.listdir(self.notes_dir) if note.endswith(".txt")]
        for note in notes:
            self.notes_listbox.insert(tk.END, note)

    def add_note(self):
        note_title = simpledialog.askstring("Add Note", "Enter note title:", parent=self.root)
        if note_title:
            note_path = os.path.join(self.notes_dir, f"{note_title}.txt")
            with open(note_path, "w") as note_file:
                note_file.write("") 
            self.load_notes()

    def delete_note(self):
        selected_note = self.notes_listbox.get(tk.ACTIVE)
        if selected_note:
            note_path = os.path.join(self.notes_dir, f"{selected_note}.txt")
            os.remove(note_path)
            self.load_notes()

if __name__ == "__main__":
    root = tk.Tk()
    app = NotebookManager(root)
    root.mainloop()
