from pytube import YouTube

video_url = input("Enter the video link: ")
yt = YouTube(video_url)

print(f"Title: {yt.title}")
print(f"Views: {yt.views}")

# Fetch the highest resolution progressive stream
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
print(f"Downloading: {yt.title}")
stream.download()
print("Download completed!")
