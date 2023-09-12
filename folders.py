import os
from io import open
import tkinter as tk  
from tkinter import filedialog
from shutil import copy
import random
# from distutils.dir_util import copy_tree

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
        folderList = []
        
        for file in os.listdir(root_dir):
            name,ext = os.path.splitext(root_dir + file)  
            if ext in ['']:
                folderList.append(name) 
            else:
                # falta hacer que modifique los textos
                name = name.split('/')
                name = name[-1]
                copy(root_dir + file, dest_dir + name + '_copy' + ext)
                # print(dest_dir + name + '_copy' + ext)
                # print('\n')
                archive = open(dest_dir + name + '_copy' + ext)
                self.getData(archive,dest_dir,name,ext)
                



        for i in range(len(folderList)):
            aux = folderList[i].split('/')
            aux = aux[-1]
            os.mkdir(dest_dir+aux)
            self.copyElements(folderList[i]+'/',dest_dir+aux+'/')
    
    def getData(self,file,dest_dir,name,ext):
        try:
            arc = file.readlines()
            lista = []
            for line in arc:
                for char in line:
                    if(char.isdigit()):
                        randuppercase = chr(random.randint(ord('A'), ord('Z')))
                        char = randuppercase
                        lista.append(char)
                        # lista.append(randuppercase)
                    elif(char.isalpha() and char != ''):
                        randnum = random.randint(0,15)
                        char = str(randnum)
                        lista.append(randnum)
                    elif(char == '\n'):
                        lista.append('\n')
                    else:
                        lista.append('')
            string = ''.join(map(str,lista))
            res = open(dest_dir+'aux'+ext, 'w')
            res.write(string + '\n')
            res.close()
            file.close()
            os.rename(dest_dir+'aux'+ext,dest_dir+name+'_mod'+ext)
            # os.remove(file)
        except print(0):
            file.close()


