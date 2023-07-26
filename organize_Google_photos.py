import os
import glob
import zipfile
import shutil


# First, unzip ".zip" files, this will generate files into their corresponding year folders
work_directory = "/Users/kofressia/Library/CloudStorage/OneDrive-Personal/photos/"

os.chdir(work_directory)

for file in os.listdir(work_directory):   # get the list of files
    if zipfile.is_zipfile(file): # if it is a zipfile, extract it
        with zipfile.ZipFile(file) as item: # treat the file as a zip
           item.extractall()  # extract it in the working directory

# Second, delete unwanted files, i.e., xxx.json in a folder.
for root, dirs, files in os.walk(".", topdown = True):
    for file in filter(lambda x: x.endswith(".json"), files):
        os.remove(os.path.join(root, file))

# Third, rename files by adding photo-taken-year in front of each photo
for root, dirs, files in os.walk(".", topdown = True):
    for file in files:
        current_path = os.path.join(root, file)

        # Use split() method and split on the string in os.sep to return a list of strings of a file path
        new_prefix = current_path.split(os.sep)[-2] #this is the up-level folder for a certain photo (i.e., "Photo from 2015" or "Takeout001")

        if "Photos" in new_prefix:
            # extract the year name and store this info in my_prefix
            my_prefix = new_prefix.split(" ")[2]  # The "Photo from 2015" string is splited into three parts, and we will use the last element, 
            # "2015" as the prefix for each photo.
            
            # Separate file name and file extension
            f_name, f_ext = os.path.splitext(file)
            new_name = "{}_{}{}".format(my_prefix, f_name, f_ext)
            
            os.rename(current_path, new_name)


# The `glob` module is used to retrieve files or path names matching a specified pattern.

# Gather video files
video_files = glob.glob(os.path.join(work_directory, "*.mp4"), recursive=True) 

video_destination = "/Users/kofressia/Library/CloudStorage/OneDrive-Personal/photos/videos"

# iterate on all files to move them to destination folder
for file_path in video_files:
    dst_path = os.path.join(video_destination, os.path.basename(file_path))
    shutil.move(file_path, dst_path)


# Gather photo files
photo_files = glob.glob(os.path.join(work_directory, "*.jpg"))

photo_destination = "/Users/kofressia/Library/CloudStorage/OneDrive-Personal/photos/photo"

# iterate on all files to move them to destination folder
for file_path in photo_files:
    dst_path = os.path.join(photo_destination, os.path.basename(file_path))
    shutil.move(file_path, dst_path)
