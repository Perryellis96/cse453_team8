
import tkinter as tk
import pathlib

from sympy import root



class Application(tk.Tk):
     def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Homograph')
        
        first_label = tk.Label(self, text = "A homograph is two or more words that are spelled the same \n but aren't necessarily pronounced the same. \nCan have different meanings and origins. \n Program that detects file path homograph attacks.", font=12)
        first_label.pack(padx = 3, pady = 3)
       

        second_label = tk.Label(self, text = "Enter your first path: ", font=12)
        second_label.pack(padx = 3, pady = 3)
        Application.first_entry = tk.Entry(self, width = 30)
        Application.first_entry.pack(padx = 7, pady = 7)
        third_label = tk.Label(self, text = "Enter your second path: ", font=12)
        third_label.pack(padx = 3, pady = 3)
        Application.second_entry = tk.Entry(self, width = 30)
        Application.second_entry.pack(padx = 7, pady = 7)
        first_button = tk.Button(self, bg="#0048ba" ,text ="check path", fg="black", command = lambda:canonicalization())
        first_button.pack(padx= 5, pady = 5)
        Application.text_box = tk.Text(self, height=10, width=30, bg = "light cyan")
        Application.text_box.pack(padx= 10, pady = 5)
        Application.text_box.tag_configure("center", justify="center")
        Application.text_box.tag_add("center", 1.0)
        #fact = canonicalization
        #Application.text_box.insert(0.0, fact)

        
        

def canonicalization():

  path_1 = pathlib.Path(str(Application.first_entry.get()))
  path_2 = pathlib.Path(str(Application.second_entry.get()))

  if path_1.resolve() == path_2.resolve():
      Application.text_box.insert(1.0, f"**The paths are homographs:\n\n {path_1.resolve()}\n")
        
  else:
      Application.text_box.insert(1.0, f"The paths are NOT homographs \n\nPath-1: {path_1.resolve()}\n\nPath-2:{path_2.resolve()}\n\n")
    
#page_content = canonicalization
#text_box = tk.Text(root, height=10, width=20)
#text_box.insert(page_content)
app = Application()
app.mainloop()
