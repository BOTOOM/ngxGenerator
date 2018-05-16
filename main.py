from front_ngx import front_ngx
from  Tkinter import Tk
import Tkinter, Tkconstants, tkFileDialog
import sys

if __name__ == "__main__":
    entity = None
    if len(sys.argv) <= 1:
        root = Tk()
        root.filename = tkFileDialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("ent files","*.ent"),("all files","*.*")))
        if root.filename:
            entity=root.filename
            print("file path selected is "+ entity )            
        else:
            print "You must enter or select the file of the entity with which you want to generate the code"
            exit(1)
    else:
        entity = sys.argv[1]

    
    folder_name = raw_input("Register folder project name: \n Name: ")
    if not folder_name:
        folder_name="project"
    
    gen = front_ngx(entity, folder_name)
   


    
    