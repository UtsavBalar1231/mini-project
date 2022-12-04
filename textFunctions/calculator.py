# Calculator using tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x300")
        self.resizable(False, False)
        self.configure(bg="white")
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        self.entry = ttk.Entry(self, font=("Arial", 20))
        self.entry.place(x=10, y=10, width=280, height=40)

        self.button_1 = ttk.Button(self, text="1", command=lambda: self.entry.insert(tk.END, "1"))
        self.button_1.place(x=10, y=60, width=50, height=50)

        self.button_2 = ttk.Button(self, text="2", command=lambda: self.entry.insert(tk.END, "2"))
        self.button_2.place(x=70, y=60, width=50, height=50)

        self.button_3 = ttk.Button(self, text="3", command=lambda: self.entry.insert(tk.END, "3"))
        self.button_3.place(x=130, y=60, width=50, height=50)
        
        self.button_4 = ttk.Button(self, text="4", command=lambda: self.entry.insert(tk.END, "4"))
        self.button_4.place(x=10, y=120, width=50, height=50)
        
        self.button_5 = ttk.Button(self, text="5", command=lambda: self.entry.insert(tk.END, "5"))
        self.button_5.place(x=70, y=120, width=50, height=50)

        self.button_6 = ttk.Button(self, text="6", command=lambda: self.entry.insert(tk.END, "6"))
        self.button_6.place(x=130, y=120, width=50, height=50)
        
        self.button_7 = ttk.Button(self, text="7", command=lambda: self.entry.insert(tk.END, "7"))
        self.button_7.place(x=10, y=180, width=50, height=50)
        
        self.button_8 = ttk.Button(self, text="8", command=lambda: self.entry.insert(tk.END, "8"))
        self.button_8.place(x=70, y=180, width=50, height=50)
        
        self.button_9 = ttk.Button(self, text="9", command=lambda: self.entry.insert(tk.END, "9"))
        self.button_9.place(x=130, y=180, width=50, height=50)
        
        self.button_0 = ttk.Button(self, text="0", command=lambda: self.entry.insert(tk.END, "0"))
        self.button_0.place(x=70, y=240, width=50, height=50)
        
        self.button_plus = ttk.Button(self, text="+", command=lambda: self.entry.insert(tk.END, "+"))
        self.button_plus.place(x=190, y=60, width=50, height=50)
        
        self.button_minus = ttk.Button(self, text="-", command=lambda: self.entry.insert(tk.END, "-"))
        self.button_minus.place(x=190, y=120, width=50, height=50)
        
        self.button_multiply = ttk.Button(self, text="*", command=lambda: self.entry.insert(tk.END, "*"))
        self.button_multiply.place(x=190, y=180, width=50, height=50)
        
        self.button_divide = ttk.Button(self, text="/", command=lambda: self.entry.insert(tk.END, "/"))
        self.button_divide.place(x=190, y=240, width=50, height=50)
        
        self.button_equal = ttk.Button(self, text="=", command=self.calculate)
        self.button_equal.place(x=250, y=60, width=40, height=228)
        
        self.button_clear = ttk.Button(self, text="C", command=self.clear)
        self.button_clear.place(x=250, y=10, width=40, height=40)
        
    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except:
            messagebox.showerror("Error", "Invalid input")

    def clear(self):
        self.entry.delete(0, tk.END)

    def create_menu(self):
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.destroy)

        self.edit_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Copy", command=lambda: self.entry.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label="Cut", command=lambda: self.entry.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Paste", command=lambda: self.entry.event_generate("<<Paste>>"))
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=lambda: self.entry.event_generate("<<SelectAll>>"))

        self.help_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.about)
        
    def about(self):
        messagebox.showinfo("About", "Calculator")
        
if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
    
