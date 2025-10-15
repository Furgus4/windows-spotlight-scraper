import os
import shutil
from datetime import datetime

spotlight_path = "C:\\Users\\{put username here}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
spotlight_desktop_path = "C:\\Users\\{put username here}\\AppData\\Local\\Packages\\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\\LocalCache\\Microsoft\\IrisService\\7073164735893850138"
my_path = "C:\\Users\\{put username here}\\Pictures\\Windows Spotlight"
state_path = my_path + "\\state.txt" # make sure state.txt is in the windoows spotlight folder (my_path)

if __name__ == "__main__":
    s_image_names = os.listdir(spotlight_path)
    sd_image_names = os.listdir(spotlight_desktop_path)

    with open(state_path) as s:
        prev_names = s.read().split()

    index = 0
    for name in s_image_names:
        if name not in prev_names:
            image_path = spotlight_path + "\\" + name
            with open(state_path, "a") as s:
                s.write(name + "\n")
            if os.path.getsize(image_path) >= 180000: # filters out some icons
                destination = my_path + "\\" + datetime.today().strftime("%m_%d_%Y.%H_%M.") + str(index) + ".jpg"
                shutil.copy(image_path, destination)
                index += 1

    for name in sd_image_names:
        if name not in prev_names:
            image_path = spotlight_desktop_path + "\\" + name
            with open(state_path, "a") as s:
                s.write(name + "\n")
            destination = my_path + "\\" + datetime.today().strftime("%m_%d_%Y.%H_%M.") + str(index) + ".jpg"
            shutil.copy(image_path, destination)
            index += 1
