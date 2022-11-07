from pytube import YouTube
# define where the video will be stored
Download_Directory = "/Users/Orain/Dowloads/Video"
# the user will enter the download link
video_url = input("youtube.com/....")
# creating an instance of the video
video_obj = YouTube(video_url)
stream = video_obj.stream.get_highest_resolution()
# download the video into the prescribed path
stream.download(Download_Directory)


