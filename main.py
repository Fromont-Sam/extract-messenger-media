import os
import json
import re
from datetime import datetime
import filedate
import shutil
import uuid
import string
import time

# Define the regex pattern to match the JSON file names
pattern = re.compile(r'message_.*\.json')

# Directories
input_dir = os.path.join("messages", "inbox")
output_dir = 'output'
output_dir_photos = os.path.join(output_dir, "videos")
output_dir_videos = os.path.join(output_dir, "photos")
output_dir_gifs = os.path.join(output_dir, "gifs")
done_dir = 'done'
error_dir = 'error'

# Move and rename files to the output folder
def move_to_output(old_path, media_type, title, creation_timestamp):
    # Store old path
    new_path = old_path
    # Create the filename pattern and remove char that can't be in folder name
    creation_date = datetime.fromtimestamp(creation_timestamp)
    creation_date_str = creation_date.strftime('%Y%m%d%H%M%S')
    file_extension = os.path.splitext(old_path)[1]
    title = re.sub(r'[<>:"/\\|?*]', '', title)
    title = title.strip()
    # Some conversation can have a complete not printable title
    if len(title.strip()) == 0:
        title = "unknown"
    new_file_name = title + "_" + creation_date_str + "_" + str(uuid.uuid4()) + file_extension
    # Move the new file
    new_path = os.path.join(output_dir, media_type, new_file_name)
    shutil.copy(old_path, new_path)
    return new_path

# Change "created, modified and accessed" date of the provided file
def change_metadata_date(new_path, creation_timestamp):
    # Convert the Unix timestamp to a datetime object
    creation_date = datetime.fromtimestamp(creation_timestamp)
    # Convert the new date and time to a string
    creation_date_str = creation_date.strftime('%Y.%m.%d %H:%M:%S')
    
    # Change metadata
    file_path = filedate.File(new_path)
    file_path.set(
        created = creation_date_str,
        modified = creation_date_str,
        accessed = creation_date_str
    )
    filedate.File(new_path)

# Create folders
if not os.path.exists(output_dir):
        os.makedirs(output_dir)
if not os.path.exists(output_dir_photos):
        os.makedirs(output_dir_photos)
if not os.path.exists(output_dir_videos):
        os.makedirs(output_dir_videos)
if not os.path.exists(output_dir_gifs):
        os.makedirs(output_dir_gifs)
if not os.path.exists(done_dir):
        os.makedirs(done_dir)                                      

# Loop over all subdirectories and files in the root directory
for subdir, dirs, files in os.walk(input_dir):
    # Loop over all JSON files in the current subdirectory
    for filename in files:
        if pattern.match(filename):
            # Construct the full path to the JSON file
            file_path = os.path.join(subdir, filename)
            
            # Load the JSON data from the file
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Remove all non printable characters from the title
            title = data['title']
            printable_chars = set(string.printable)
            title = ''.join(filter(lambda x: x in printable_chars, title))
            # Start extracting and log data file
            print("->" + title + " extract started...")
            print("Data file : " + file_path)
            count = 0
            try:
                # Loop over all messages then media types (photos, videos, gifs)
                for message in data['messages']:
                    for media_type in ["photos", "videos", "gifs"]:
                        if media_type in message:
                            for media in message[media_type]:
                                # Retrieve media uri and creation timestamp
                                path = media['uri']
                                # For gifs this value can be empty
                                if 'creation_timestamp' in media:
                                    creation_timestamp = media['creation_timestamp']
                                else:
                                    current_timestamp = int(time.time())
                                # Check if the media is present
                                if os.path.exists(path):
                                    # Move media to output folder
                                    new_path = move_to_output(path, media_type, title, creation_timestamp)
                                    # Change metadata of the moved media
                                    change_metadata_date(new_path, creation_timestamp)
                                    count += 1
                # Move entire conversation folder to "done" folder
                shutil.move(subdir, done_dir)
                print("->" + title + " extract ended with a total of " + str(count) + " media(s)")
            except Exception as ex:
                # Move entire conversation folder to "error" folder
                if not os.path.exists(error_dir):
                    os.makedirs(error_dir)
                shutil.move(subdir, error_dir)
                print("->" + title + " extract ended with error : " + str(ex))