import os
import shutil
from datetime import datetime

lockscreen_path = "... stuff here \\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_{something here}\\LocalState\\Assets"

# can have subfolders
desktop_path = "... stuff here \\AppData\\Local\\Packages\\MicrosoftWindows.Client.CBS_{something here}\\LocalCache\\Microsoft\\IrisService"

my_path = "folder you want everything coppied to"
state_path = my_path + "\\state.txt" # arbitrary location

def copy_and_rename_images(folder_path, folder_destination, index=0):
    image_names = os.listdir(folder_path)

    with open(state_path) as s:
        past_names = s.read().split()

    for name in image_names:
        if name not in past_names:
            print(index)
            with open(state_path, "a") as s:
                s.write(name + "\n")
            image_path = folder_path + "\\" + name
            destination = folder_destination + "\\" + datetime.today().strftime("%m_%d_%Y.%H_%M.") + str(index) + ".jpg"
            shutil.copy(image_path, destination)
            index += 1
    return index

def main():
    sub_desktop_folders = []

    # get first level of sub_folders
    stopper = False
    for data in os.walk(desktop_path):
        if not stopper:
            sub_desktop_folders = data[1]
        stopper = True

    global_index = 0

    for folder in sub_desktop_folders:
        folder_path = desktop_path + "\\" + folder
        global_index = copy_and_rename_images(folder_path, my_path, global_index)

    copy_and_rename_images(lockscreen_path, my_path, global_index)

if __name__ == "__main__":
    main()
