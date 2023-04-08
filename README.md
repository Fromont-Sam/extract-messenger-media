
# Extract Messenger Media

This script is designed to help you manage and organize your Messenger media files by allowing you to easily extract them from Messenger and set their creation dates to the correct values. This can be realy useful to import these photos in Google Photos keeping their timeline

With this script, you can extract all photos, videos, and gifs from your Messenger conversations and save them to your local drive. It also edit their creation date metadata to ensure that they are correctly sorted and displayed in your photo library. This feature is particularly useful if you have transferred your Messenger media to a new device or have lost the original creation date information.

The script is easy to use and comes with detailed documentation to help you get started. You can customize the script to extract only specific types of media files or to edit only the creation dates of files that meet certain criteria. The script also includes error handling to ensure that your files are not accidentally deleted or overwritten.

I welcome your feedback and suggestions for future updates to the script.

## How does it works ?

### Step 1 : Download Facebook Personnal Data
To run this scrip you'll need first to ask a copy of your personnal data to Facebook.
You can do this in Settings -> Your Facebook Information -> Download your information.
You'll need to download in JSON

### Step 2 : Extract the data into a single folder
Once the Facebook data files are available, you can download them and extract their content into the same output folder.
You should have in this folder a subfolder called **'/messages/'**
You can copy this subfolder into the root of this project

### Step 3 : Run the script
Now that you have all the data related to your Messsenger messages, you can run the script.
(Check before that you have correctly installed all the libs necessary for this script)

 - Processed conversation will be copied in the '/done' folder
 - Processed media with updated date metadat will be generated into the '/output' folder
	 - You'll have a separate subfolder for all kind of medias : ["photos", "videos", "gifs"]
 - If in any case some conversation generated errors you'll find them into the '/error' folder

## Presentation
[![YouTube Video](https://i.imgur.com/3ACqlg1.png)](https://www.youtube.com/watch?v=DplYiPPI7TQ)
