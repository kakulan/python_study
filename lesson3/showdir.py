import os
import os.path

def showdir(dirname, level):
    subdirs = list(os.listdir(dirname))
    for subdir in subdirs:        
        print("--"*level,subdir)
        subdir = dirname + "\\"+subdir
        if not os.path.isdir(subdir):
            continue             
        showdir(subdir, level+1)
        
dname = input("input a dirname!")

showdir(dname,0)
    
    
