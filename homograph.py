import pathlib 
import tkinter as tk

# This function tests if two canon symbols are homographs.
def homograph(path_1, path_2):
  if path_1.resolve() == path_2.resolve():
    print(f"The paths are homographs. The canonical path is:\n {path_1.resolve()}")  
  else:
    print(f"These two paths are NOT homographs. Please view the differing canonical paths for comparison. \nPath-1: {path_1.resolve()}\nPath-2: {path_2.resolve()}")

# Tests program by running different homograph tests
def homographs_test():
    '''This part of the program is the canonicalization '''
    print("Homograph Test Cases\n")
    print("\nH-1: Relative Path versus Step Up Relative Path")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("../Public/source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-1.b TestCase")
    path_2 = pathlib.Path("../../Users/Public/source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-1.c TestCase")
    path_2 = pathlib.Path("./source/../source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-2: Relative Path versus Absolute Path")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("../Public/source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-3: Relative Path versus Relative Path and Current Directory")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("./source/./repos/./secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-3.b TestCase")
    path_2 = pathlib.Path("./source/./repos/./secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-3.c TestCase")
    path_2 = pathlib.Path("././source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-4: Relative Path versus Relative Path Using Step Up and Current Directory")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("./../Public/source/repos/../repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-4.b TestCase")
    path_2 = pathlib.Path("./source/./repos/../repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-4.c TestCase")
    path_2 = pathlib.Path("././source/../source/repos/secret/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-5: Absolute Path versus Relative Path")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("./source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-6: Absolute Path versus Relative Step-Up Path")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("./source/../source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-6.b TestCase")
    path_2 = pathlib.Path("./source/repos/../repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-6.c TestCase")
    path_2 = pathlib.Path("./source/repos/../repos/secret/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-7: Absolute Path versus Relative Path and Current Directory")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("././source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-7.b TestCase")
    path_2 = pathlib.Path("./source/./repos/./secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-7.c TestCase")
    path_2 = pathlib.Path("././source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-8: Absolute Path versus Relative Path Using Step Up and Current Directory")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("../Public/source/repos/../repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-8.b TestCase")
    path_2 = pathlib.Path("./source/./repos/../repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-8.c TestCase")
    path_2 = pathlib.Path("././source/../source/repos//secret/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-9: Absolute Path versus Absolute Step-Up Path")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/../users/Public/source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-9.b TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/../source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-9.c TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/../source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-10: Absolute Path versus Absolute Path and Current Directory")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/source/repos/./secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-10.b TestCase")
    path_2 = pathlib.Path("C:/users/./Public/source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-10.c TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/repos/./secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-11: Absolute Path versus Absolute Path Using Step Up and Current Directory")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/source/repos/secret/./../secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-11.b TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/./repos/../repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-11.c TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/../source/repos/secret/./password.txt")
    homograph(path_1, path_2)

    print("\nH-12: Relative Path versus Absolute Step-Up Path")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/source/repos/secret/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-12.b TestCase")
    path_2 = pathlib.Path("C:/users/../users/Public/source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-12.c TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/../source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-13: Relative Path versus Absolute Path and Current Directory")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/source/./repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-13.b TestCase")
    path_2 = pathlib.Path("C:/users/./Public/source/./repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-13.c TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/repos/secret/./password.txt")
    homograph(path_1, path_2)

    print("\nH-14: Relative Path versus Absolute Path and Current Directory")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/source/repos/./repos/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-14.b TestCase")
    path_2 = pathlib.Path("C:/users/./Public/source/./repos/secret/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-14.c TestCase")
    path_2 = pathlib.Path("C:/users/Public/./source/./repos/../repos/secret/./password.txt")
    homograph(path_1, path_2)

    print("\nH-15: Absolute Path versus Absolute Path with Detours")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/detour/../source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-15.b TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/repos/open/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-16: Absolute Path versus Relative Path with Detours")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("./detour/../source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-16.b TestCase")
    path_2 = pathlib.Path("./source/repos/open/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-17: Relative Path versus Relative Path with Detours")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("./detour/../source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-17.b TestCase")
    path_2 = pathlib.Path("./source/repos/open/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-18: Relative Path versus Absolute Path with Detours")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/detour/../source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nH-18.b TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/repos/open/../secret/password.txt")
    homograph(path_1, path_2)

    print("Tests completed...\n\n")

# Tests program by running different non-homograph tests
def nonhomographs_test():
    print("Nonhomograph Test Cases\n")
    print("NH-1: Different File Extensions in an Absolute Path")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/source/repos/secret/password.html")
    homograph(path_1, path_2)

    print("\nNH-1.d TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/repos/secret/password.doc")
    homograph(path_1, path_2)

    print("\nNH-1.d TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/repos/secret/password.png")
    homograph(path_1, path_2)

    print("\nNH-1.d TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/repos/secret/password.xlsx")
    homograph(path_1, path_2)

    print("\nNH-2: Different File Extensions in a Relative Path")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("../../users/Public/source/repos/secret/password.html")
    homograph(path_1, path_2)

    print("\nNH-2.b TestCase")
    path_2 = pathlib.Path("../../users/Public/source/repos/secret/password.doc")
    homograph(path_1, path_2)

    print("\nNH-2.c TestCase")
    path_2 = pathlib.Path("../../users/Public/source/repos/secret/password.png")
    homograph(path_1, path_2)

    print("\nNH-2.d TestCase")
    path_2 = pathlib.Path("../../users/Public/source/repos/secret/password.xlsx")
    homograph(path_1, path_2)

    print("\nNH-3: Absolute Path versus Step Up Relative Path")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("../source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-3.b TestCase")
    path_2 = pathlib.Path("../source/repos/secret/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-4: Step Up Relative Path versus Absolute Path ")
    path_1 = pathlib.Path("../source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-4.b TestCase")
    path_1 = pathlib.Path("../source/repos/secret/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-5: Relative Path versus Absolute Path")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/sources/repos/password.txt")
    homograph(path_1, path_2)

    print("\nNH-6: Absolute Path versus Relative Path")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("/source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-7: Absolute Path versus Absolute Path and Current Directory")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/source/repos/./repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-7.b TestCase")
    path_2 = pathlib.Path("C:/users/./users/Public/source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-7.c TestCase")
    path_2 = pathlib.Path("C:/users/./users/Public/source/repos/secret/./password.txt")
    homograph(path_1, path_2)

    print("\nNH-8: Absolute Path versus Absolute Step-Up Path")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/../Public/source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-8.b TestCase")
    path_2 = pathlib.Path("C:/users/Public/../../Public/source/repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-9: Relative Path versus Step Up Relative Path")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("./source/repos/secret/../password.txt")
    homograph(path_1, path_2)

    print("\nNH-9.b TestCase")
    path_2 = pathlib.Path("./source/repos/../repos/secret/../password.txt")
    homograph(path_1, path_2)

    print("\nNH-9.c TestCase")
    path_2 = pathlib.Path("./source/../source/repos/secret/../password.txt")
    homograph(path_1, path_2)

    print("\nNH-10: Relative Path versus Relative Path and Current Directory")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("./source/repos/./repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-10.b TestCase")
    path_2 = pathlib.Path("./source/./repos/secret/../repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-11: Relative Path versus Relative Path Using Step Up and Current Directory")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("./source/repos/../secret/./password.txt")
    homograph(path_1, path_2)

    print("\nNH-11.b TestCase")
    path_2 = pathlib.Path("./source/repos/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-11.c TestCase")
    path_2 = pathlib.Path("./source/repos/./../secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-12: Relative Path versus Relative Path Using Step Up and Current Directory")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("./source/repos/./../secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-12.b TestCase")
    path_2 = pathlib.Path("./source/repos/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-12.c TestCase")
    path_2 = pathlib.Path("./source/./secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-13: Absolute Path versus Relative Path Using Step Up and Current Directory")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("././source/repos/secret/../repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-13.b TestCase")
    path_2 = pathlib.Path("././source/repos/./secret/../repos/./secret/password.txt")
    homograph(path_1, path_2)
    
    print("\nNH-13.c TestCase")
    path_2 = pathlib.Path("./source/repos/./secret/../repos/./secret/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-14: Absolute Path versus Absolute Path Using Step Up and Current Directory")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/source/repos/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-14.b TestCase")
    path_2 = pathlib.Path("C:/users/Public/./source/repos/../secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-14.c TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/repos/./../secret/password.txt")
    homograph(path_1, path_2)


    print("\nNH-15: Relative Path versus Absolute Path Using Step Up and Current Directory")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/source/repos/./repos/../repos/secret/password.txt")
    homograph(path_1, path_2)
    print("\nNH-15.b TestCase")
    path_2 = pathlib.Path("C:/users/Public/./source/repos/secret/../repos/secret/password.txt")
    homograph(path_1, path_2)
    print("\nNH-15.c TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/repos/./repos/../repos/secret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-16: Relative Path versus Relative Path with accented characters")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("./source/repós/secret/password.txt")
    homograph(path_1, path_2)
    print("\nNH-16.b TestCase")
    path_2 = pathlib.Path("./source/repos/secret/passwòrd.txt")
    homograph(path_1, path_2)
    print("\nNH-16.c TestCase")
    path_2 = pathlib.Path("./source/repos/sècret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-17: Relative Path versus Absolute Path with accented characters")
    path_1 = pathlib.Path("./source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/source/repós/secret/password.txt")
    homograph(path_1, path_2)
    print("\nNH-17.b TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/repos/secret/passwòrd.txt")
    homograph(path_1, path_2)
    print("\nNH-17.c TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/repos/sècret/password.txt")
    homograph(path_1, path_2)


    print("\nNH-18: Absolute Path versus Absolute Path with accented characters")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("C:/users/Public/source/repós/secret/password.txt")
    homograph(path_1, path_2)
    print("\nNH-18.b TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/repos/secret/passwòrd.txt")
    homograph(path_1, path_2)
    print("\nNH-18.c TestCase")
    path_2 = pathlib.Path("C:/users/Public/source/repos/sècret/password.txt")
    homograph(path_1, path_2)

    print("\nNH-19: Absolute Path versus Relative Path with accented characters")
    path_1 = pathlib.Path("C:/users/Public/source/repos/secret/password.txt")
    path_2 = pathlib.Path("./source/repós/secret/password.txt")
    homograph(path_1, path_2)
    print("\nNH-19.b TestCase")
    path_2 = pathlib.Path("./source/repos/secret/passwòrd.txt")
    homograph(path_1, path_2)
    print("\nNH-19.c TestCase")
    path_2 = pathlib.Path("./source/repos/sècret/password.txt")
    homograph(path_1, path_2)
  
    print("Tests completed...\n\n")

# Main menu
def menu():
    while True:
        print("""\nWelcome to the Homograph Test

        We will be testing to see if two paths are homographs.

        Forbidden File Path: C:/users/Public/source/repos/secret/password.txt
        Current location: C:/users/Public/

        
        Please enter one of the following:
        1. Homograph Tests
        2. Non-Homograph Test
        3. GUI Test
        4. Quit\n""")
        userinput = input(str("Enter input: "))
        if userinput == "1":
            homographs_test()
        if userinput == "2":
            nonhomographs_test()
        if userinput =="3":
            app = Application()
            app.mainloop()
        if userinput =="4":
            break

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
        first_button = tk.Button(self, text ="check path", command = lambda:canonicalization())
        first_button.pack(padx= 5, pady = 5)
        Application.text_box = tk.Text(self, height=10, width=30, bg = "light cyan")
        Application.text_box.pack(padx= 10, pady = 5)
        #fact = canonicalization
        #Application.text_box.insert(0.0, fact)

def canonicalization():

  path_1 = pathlib.Path(str(Application.first_entry.get()))
  path_2 = pathlib.Path(str(Application.second_entry.get()))

  if path_1.resolve() == path_2.resolve():
      Application.text_box.insert(0.0, f"The paths are homographs:\n {path_1.resolve()}")  
  else:
      Application.text_box.insert(0.0, f"The paths are NOT homographs \n\nPath-1: {path_1.resolve()}\n\nPath-2:{path_2.resolve()}")
    
#page_content = canonicalization
#text_box = tk.Text(root, height=10, width=20)
#text_box.insert(page_content)
app = Application()
app.mainloop()


if __name__ == "__main__":
    menu()
