import bpy
import os
import sys
from pathlib import Path
from video_sourcing import csv_search_terms

# Global constants
FPS = 30  # set frame rate (frames per second)
CWD = Path.cwd()

# Load predefined conditions
shot = csv_search_terms()
durations_list = [int(v[2]) for (k, v) in shot.items()]  # duration of each shot
subtitles_list = [v[0] for (k, v) in shot.items()]  # subtitle for each shot

# Initial Settings and Calculations
bpy.context.scene.render.fps = FPS
bpy.context.scene.frame_end = sum(durations_list) * FPS

# Load context
scene = bpy.context.scene
scene.sequence_editor_create()
seq = scene.sequence_editor.sequences


# Add new clip
def load_clips() -> None:
    """Load video clips into Blender for editing."""
    current_frame = 0

    for current_shot in range(1, len(durations_list) + 1):
        path = CWD / "videos" / f"shot_{current_shot}.mp4"
        shot_name = f"shot{current_shot}"

        seq.new_movie(name=shot_name,
                      filepath=str(path),
                      channel=1,
                      frame_start=current_frame)

        # Set start position (optional) and required duration
        seq[shot_name].animation_offset_start = 4 * FPS  # all videos are sub-clipped to start at 4 seconds.
        seq[shot_name].frame_final_duration = durations_list[current_shot - 1] * FPS
        current_frame += seq[shot_name].frame_final_duration


# Add subtitle
def add_subtitles() -> None:
    """Add predefined subtitles into Blender."""
    current_frame = 0

    for current_shot in range(1, len(durations_list) + 1):
        sub_name = f"shot{current_shot}_sub"

        seq.new_effect(name=sub_name,
                       frame_start=current_frame,
                       frame_end=current_frame + (durations_list[current_shot-1] * FPS),
                       channel=2,
                       type='TEXT')

        seq[sub_name].text=subtitles_list[current_shot-1]
        seq[sub_name].use_shadow = True
        seq[sub_name].use_box = True
        seq[sub_name].blend_type = 'ALPHA_OVER'
        seq[sub_name].font_size = 50
        seq[sub_name].wrap_width = 0.6
        seq[sub_name].location[0] = 0.5
        seq[sub_name].location[1] = 0.1

        current_frame += seq[sub_name].frame_final_duration


if __name__ == "__main__":
    load_clips()
    add_subtitles()
