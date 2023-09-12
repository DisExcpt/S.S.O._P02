import os
import tkinter as tk  
from tkinter import filedialog
import shutil

class folders:
    def __init__(self):
        self.root = ''
        self.dest = ''
        
    def selectRoot(self):
        root = tk.Tk()  # esto se hace solo para eliminar la ventanita de Tkinter
        root.withdraw()  # ahora se cierra
        file_path = filedialog.askdirectory()
        self.root = file_path
        return self.root+'/'
    
    def selectDestination(self):
        root = tk.Tk()  # esto se hace solo para eliminar la ventanita de Tkinter
        root.withdraw()  # ahora se cierra
        file_path = filedialog.askdirectory()
        self.dest = file_path
        self.dest += '/copy/'
        os.mkdir(self.dest)
        return self.dest
    
    def formarRute(self):
        newRute = ''
        for char in self.root:
            if(char == '\\'):
                newRute += '/'
            else:
                newRute += char
        return newRute

    def copyElements(self,root_dir,dest_dir):
        for file in os.listdir(root_dir):
            name,ext = os.path.splitext(root_dir + file)
            print(name,ext)
            if ext in ['.text', '.py']:
                name = name.split('/')
                name = name[-1]
                print(name)
                shutil.copy(root_dir+file,dest_dir+name+ '_copy' + ext)

    
    
folder = folders()

root = folder.selectRoot()
dest = folder.selectDestination()
print(root)
print(dest)

folder.copyElements(root,dest)

