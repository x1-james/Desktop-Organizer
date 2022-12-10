# The program creates a new folder on the Desktop called "Organized" and then creates
# subfolders for each file type. The program then moves all files on the Desktop into
# the appropriate subfolder.

import os
import shutil

# set folder name of organized directory
organized_folder_name = "Organized"

# set path to desktop directory
desktop_path = os.path.expanduser("~/Desktop")

# create new folder on the Desktop to store organized files
organized_folder_path = os.path.join(desktop_path, organized_folder_name)
if not os.path.exists(organized_folder_path):
    os.makedirs(organized_folder_path)

# create subfolders for each file type
subfolder_names = ["Compressed", "Images", "Videos",
                   "Documents", "Music", "Executable", "Text", "Report Files", "Other"]
subfolder_paths = {}

# create subfolders if they don't already exist
for subfolder_name in subfolder_names:
    subfolder_path = os.path.join(organized_folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    subfolder_paths[subfolder_name] = subfolder_path

# get a list of all files on the Desktop
desktop_files = os.listdir(desktop_path)

# move files to the appropriate organized subfolder
for file in desktop_files:

    # skip moving the organized folder
    if file == organized_folder_name:
        continue

    file_path = os.path.join(desktop_path, file)

    # check if the file is a file and not a directory
    if os.path.isfile(file_path):
        # get the file extension
        _, file_ext = os.path.splitext(file_path)
        file_ext = file_ext.lower()

        # move the file to the appropriate subfolder
        if file_ext in [".zip", ".7zip", ".rar", ".tar", ".gz", ".bz2", ".xz"]:
            shutil.move(file_path, subfolder_paths["Compressed"])
        elif file_ext in [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg"]:
            shutil.move(file_path, subfolder_paths["Images"])
        elif file_ext in [".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv"]:
            shutil.move(file_path, subfolder_paths["Videos"])
        elif file_ext in [".doc", ".docx", ".pdf", ".ppt", ".pptx", ".xls", ".xlsx"]:
            shutil.move(file_path, subfolder_paths["Documents"])
        elif file_ext in [".mp3", ".wav", ".flac", ".ogg"]:
            shutil.move(file_path, subfolder_paths["Music"])
        elif file_ext in [".py", ".pyw", ".exe", ".msi", ".bat", ".sh", ".cmd", ".r"]:
            shutil.move(file_path, subfolder_paths["Executable"])
        elif file_ext in [".twb", ".twbx", ".tfl", ".rdl"]:
            shutil.move(file_path, subfolder_paths["Report Files"])
        elif file_ext in [".txt", ".rtf", ".csv", ".xls", ".xlsx"]:
            shutil.move(file_path, subfolder_paths["Text"])
        else:
            shutil.move(file_path, subfolder_paths["Other"])

# remove empty subfolders
for subfolder_name in subfolder_names:
    subfolder_path = os.path.join(organized_folder_path, subfolder_name)
    if not os.listdir(subfolder_path):
        os.rmdir(subfolder_path)

print("Your desktop has been organized! Your files are located in: " +
      organized_folder_name)
