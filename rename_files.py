#Lesson 1 Use functions.  rename_files.py
import os
#define a function to rename a file
def rename_files():
        file_list = os.listdir(r"H:\config\Desktop\GitHub\Python\prank")
        saved_path = os.getcwd()
        os.chdir(r"H:\config\Desktop\GitHub\Python\prank")
        for file_name in file_list:
                print "renaming "+file_name+"\tto\t"+file_name.translate(None,"0123456789")
                os.rename(file_name,file_name.translate(None,"0123456789"))
        os.chdir(saved_path)
# and here is where that function is called.
print "Operating System is ["+os.name+"]"
rename_files()
print("files renamed")
