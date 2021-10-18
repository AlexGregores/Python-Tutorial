import os

path = " empty_folder"

try:
    os.remove(path)
    os.rmdir(path)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print('You do not have permission to delete that' )
else:
    print(path+"was delete")