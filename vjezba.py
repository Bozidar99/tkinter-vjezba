import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

class App(tk.Tk):
    def __init__(self,title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0],size[1])


        self.menu = Menu(self)
        self.main = Main(self)


        self.mainloop()


class Menu(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.place(x = 0, y = 1, relheight = 1, relwidth = 0.3)

        self.create_widgets()

    def create_widgets(self):

        button1 = ttk.Button(self, text = "Button 1")
        button2 = ttk.Button(self, text = "Button 2")
        button3 = ttk.Button(self, text = "Button 3")

        slider1 = ttk.Scale(self, orient = "vertical")
        slider2 = ttk.Scale(self, orient = "vertical")

        check_frame = ttk.Frame(self)
        check1 = ttk.Checkbutton(check_frame, text = "check1")
        check2 = ttk.Checkbutton(check_frame, text = "check2")

        entry = ttk.Entry(self)

        self.columnconfigure((0,1,2), weight=1, uniform="a")
        self.rowconfigure((0,1,2,3,4), weight=1, uniform="a")

        button1.grid(row = 0, column = 0, sticky = "nswe", columnspan=1,  pady = 5, padx = 5)
        button2.grid(row = 0, column = 1, sticky = "nswe", columnspan=2,  pady = 5, padx = 5)
        button3.grid(row = 1, column = 0, sticky = "nswe", columnspan=3,  pady = 5, padx = 5)

        slider1.grid(row = 2, column = 0, sticky= "ns", rowspan=2,  pady = 5, padx = 5)
        slider2.grid(row = 2, column = 2, sticky= "ns", rowspan=2,   pady = 5, padx = 5)

        check_frame.grid(row = 4, column = 0, columnspan=3, sticky="nesw")
        check1.pack(side = "left", expand=True)
        check2.pack(side = "left", expand=True)

        entry.place(relx = 0.5, rely = 0.95, relwidth= 0.9, anchor="center")

class Main(ttk.Frame):
    def __init__(self, parent):
       super().__init__(parent)
       self.place(relx = 0.3, y = 0, relwidth=0.7, relheight= 1)
       Entry(self, "Entry 1","Button 1","green")
       Entry(self, "Entry 2","Button 2","red")
     
  
class Entry(ttk.Frame):
    def __init__(self,parent,label_text,button_text,label_backgorund):
        super().__init__(parent)

        label = ttk.Label(self, text = label_text, background = label_backgorund)
        button = ttk.Button(self, text = button_text)

        label.pack(expand = True, fill = "both")
        button.pack(expand = True, fill = "both", pady = 20)

        self.pack(side="left", expand= True, fill = "both", padx = 20, pady = 20)
    


App("Tkinter projekt", (600,600))