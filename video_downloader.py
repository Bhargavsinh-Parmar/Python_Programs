from pytube import YouTube

video_url = input("Enter the video link:")

yt = YouTube(video_url)

stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()


stream.download()

print("Download Complete")

