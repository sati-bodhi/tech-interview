import video_sourcing as vs
import glob
import os


def files_exist(filepath):
    """Check if files with a certain filename pattern exist.
    Wildcards can be used in the filepath string. """

    for filepath_object in glob.glob(filepath):
        if os.path.isfile(filepath_object):
            return True

    return False


def fix_duration(start_time=4) -> None:
    """Calculate video start and end times for sub-clipping.
    Start time has been arbitrarily fixed at 4 seconds for all videos,
    and can be changed by adding a numeric argument to the function call."""

    shot = vs.csv_search_terms()
    durations_list = [v[2] for (k, v) in shot.items()]
    os.chdir("./videos")

    if files_exist("fixed_shot*.mp4"):
        os.system("rm fixed_shot*.mp4")
    else:
        pass

    for i, duration in enumerate(durations_list):
        # Set all videos to start at 4 seconds
        os.system(f"ffmpeg -i shot_{i+1}.mp4 -ss {start_time} -t {duration} -c copy fixed_shot_{i+1}.mp4")


if __name__ == "__main__":

    fix_duration()
