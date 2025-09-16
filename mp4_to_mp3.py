# let's covert mp4 into mp3
import os 
import subprocess
files=os.listdir("video")
for file in files:
    video_name=file.split(".mp4")[0]
    print(video_name)
    subprocess.run(["ffmpeg","-i",f"video/{file}",f"video_mp3/{video_name}.mp3"])
    