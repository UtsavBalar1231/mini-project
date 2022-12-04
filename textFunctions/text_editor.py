import tkinter as tk
from tkinter import filedialog


class TextEditor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.text = tk.Text(self)
        self.text.pack(side="top", fill="both", expand=True)
        self.text.insert(tk.END, "Hello World")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.open_file = tk.Button(self, text="Open File", fg="blue",
                                   command=self.open_file)

        self.open_file.pack(side="left")

        self.save_file = tk.Button(self, text="Save File", fg="green",
                                   command=self.save_file)

        self.save_file.pack(side="left")

    def open_file(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                              filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        if filename:
            with open(filename, 'r') as f:
                self.text.delete(1.0, tk.END)
                self.text.insert(1.0, f.read())

    def save_file(self):
        filename = filedialog.asksaveasfilename(initialdir="/", title="Select File",
                                                filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        if filename:
            with open(filename, 'w') as f:
                f.write(self.text.get(1.0, tk.END))


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(master=root)
    app.mainloop()
