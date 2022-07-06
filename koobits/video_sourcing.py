from pypexels import PyPexels
from requests import Session
import os
from pathlib import Path
import csv
from collections import defaultdict
from typing import List, Tuple, Dict

BASE_URL = "https://pexels.com/video/"
PEXELS_API_KEY = "563492ad6f91700001000001f32296cf42f2439e9801b8071c775e5a"


def video_search(query, choice=0, per_page=5) -> Tuple[str, int]:
    """Calls API to search pexels.com for videos.
    Use 'choice' parameter to select video of choice.
    First video (id=0) is the default. """

    api = PyPexels(api_key=PEXELS_API_KEY)

    video_query = api.videos_search(
        query=query,
        orientation="landscape",
        size="medium",
        per_page=per_page)

    choices = []
    for video in video_query.entries:
        choices.append((video.id, video.user.get('name'), video.url, video.duration))

    print(f"The following videos have been found based on the search query '{query}': ")
    print(("Video ID", "Videographer", "URL", "Duration of video"))
    print(*choices, sep="\n")
    print()
    print("-"*100, f"\n")

    data_url = BASE_URL + str(choices[choice][0]) + "/download"
    duration = choices[choice][3]

    return data_url, duration


def video_dl(data_url, shot_id=0) -> None:
    """Downloads selected video from pexels.com"""

    with Session() as session:
        video_data = session.get(data_url)
        print(f"""{video_data.headers.get('content-type')} file will be downloaded
        from {data_url} into the 'videos' folder...\n""")

    # Create videos subdirectory if it does not exist.
    if os.path.isdir("videos"):
        pass
    else:
        os.mkdir("videos")

    working_directory = Path(os.getcwd())
    path = working_directory / "videos" / f"shot_{shot_id}.mp4"

    with path.open("wb") as outfile:
        outfile.write(video_data.content)

    print("Done!")
    print()
    print("="*100, f"\n")


def csv_search_terms() -> Dict[str, List[str]]:
    columns = defaultdict(list)
    with open("video_edit.csv", "r") as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        # print(csv_reader)
        for i, row in enumerate(csv_reader):

            if i == 3:
                break

            # Consolidate columns
            for (k, v) in row.items():
                columns[k].append(v)

        columns.pop("Shot Number")

        return columns


def get_video_data(per_page=5):
    """Loop through search terms to get video data."""
    shot = csv_search_terms()
    for i in range(1, len(shot)+1):
        query = shot[str(i)][1]
        duration = shot[str(i)][2]

        url, actual_duration = video_search(query)

        for j in range(1, per_page):
            # Pick next candidate if actual duration is shorter than requirement.
            if int(duration) > actual_duration:
                url, actual_duration = video_search(query, j, per_page)
            else:
                break

        video_dl(url, i)


if __name__ == "__main__":

    get_video_data()
