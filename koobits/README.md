# Blender Video Editing Workflow Automation

This is a mini project which is created to satisfy part of the [KooBits](https://www.koobits.com) tech interview requirement.

## Interview Question: 

### Web site Search API and Blender Integration 

Write a piece of code that enables: ( You can use your favourite language for this task )


    Automatic searching and downloading of video clips based on the predefined keywords & durations in the google sheet below.
    Automatic loading the downloaded video clips & the transcripts into blender timeline.


Google Sheet Link: ( Pls make a separate copy if necessary )

https://docs.google.com/spreadsheets/d/1SvvY2nAHRcYM_J6kz3mmKFuPlmKWusl9jaO0-DWZ_0g/edit?usp=sharing

P.S. You can modify the keywords to find better matching clips to the subtitles.

-----

## Usage

### 1. Clone this repository in your selected directory.

`git clone https://github.com/sati-bodhi/koobits`

### 2. Run `setup.py`

`python setup.py`

This would invoke the following commands to install required modules and kick-start the video download process.

`python3 -m pip install -r requirements.txt`

`python3 video_sourcing.py`

`video_sourcing.py` is a script that utilizes the [Pexels API](https://www.pexels.com/api/documentation/) to search for videos specified under the `video_edit.csv` file.
The `video_search` function under this modules allows for choosing out of 5 search results for each search term, which are printed on screen, by specifying its `choice` argument.
Videos will be downloaded into the `videos` subfolder.

### 3. Start Blender and load `bridge.py` into the scripting console.
### 4. Run `bridge.py` in the Blender text editor.

This would invoke `blender_integration.py`, which loads the downloaded video clips into the Blender sequencer, sub-clipping them into the durations specified in `video_edit.csv`. 
Subtitles for each video clip, also found in `video_edit.csv`, are automatically added to the video editor screen. 
