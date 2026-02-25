
import os
dir = r"H:\Gamut\Projects\project-folder-organizer\test_input"
if os.path.isdir(dir):
    print("yes")
    
    
for folders in os.listdir(dir):
    path = os.path.join(dir, folders)

    print(path)
    if os.path.isdir(path):
        print("yes")
