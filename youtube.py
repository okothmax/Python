import os
import youtube
# define where the video will be stored
Download_Directory = "/Users/Orain/Dowloads/Video"
# the user will enter the download link
video_url = input("enter the url: ")
# creating an instance of the video
video_obj = youtube(video_url)
stream = video_obj.stream.get_highest_resolution()
# download the video into the prescribed path
stream.download(Download_Directory)