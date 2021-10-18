import os

path = "C:\\Users\\alexa\\OneDrive\\Documentos\\Python tutorial\\text.txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
       print("That is a file")
    elif os.path.isdir(path):
        print("That is a dictionay")
    else:
        print("That location doesn't exist")
