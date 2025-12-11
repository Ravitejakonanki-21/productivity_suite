import os
import shutil

def file_organizer_menu():
    folder = input("Enter folder path to organize: ")
    if not os.path.isdir(folder):
        print("Invalid folder!")
        return

    for file in os.listdir(folder):
        ext = file.split('.')[-1]
        dest = os.path.join(folder, ext.upper())
        os.makedirs(dest, exist_ok=True)
        shutil.move(os.path.join(folder, file), os.path.join(dest, file))

    print("Files organized successfully!")
