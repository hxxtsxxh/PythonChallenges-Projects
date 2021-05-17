import time

from pytube import YouTube

link_input = input("Enter the youtube link: ")
video = YouTube(link_input)  # put link in the Youtube class
video_min = video.length / 60
video_hour = video.length / 3600
video_sec = video.length
ys = video.streams.get_highest_resolution()

# Title of the video
print("Title: ", video.title)

# Number of views of video
print("Number of views: ", video.views)

# Length of video
if video_sec > 3600:
    print("Length of video: ", video_hour, "hours")
elif 3600 > video_sec > 60:
    print("Length of video: ", video_min, "minutes")
else:
    print("Length of video: ", video_sec, "seconds")

# Rating of video
print("Rating: ", video.rating)

print('')

print("Downloading...")
time.sleep(1)
ys.download('C:/Users/heet1/Downloads')  # type directory name in parenthesis
print('Complete! File saved in [ Downloads ]')
