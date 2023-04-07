
# Extract Messenger Data

Python script that extract photos, videos and gif from Messenger and edit their creation date metadata with the good one

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
--> Tutorial video coming soon