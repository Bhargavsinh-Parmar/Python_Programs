YouTube Video Downloader
This is a simple Python program that downloads YouTube videos in the highest resolution available.

Features

Downloads YouTube videos in MP4 format
Automatically selects the highest resolution available
Requirements

Python 3.x
pytube library

Installation

Clone the repository:

git clone https://github.com/yourusername/YouTube-Video-Downloader.git
cd YouTube-Video-Downloader

Install the required libraries:

pip install pytube


Run the script:

python downloader.py

Enter the YouTube video URL when prompted:

Enter the video link: https://www.youtube.com/watch?v=dQw4w9WgXcQ

The download will start automatically, and you will be notified once it's complete:
Download Complete


Code Explanation




from pytube import YouTube

# Get the video URL from the user
video_url = input("Enter the video link:")

# Create a YouTube object
yt = YouTube(video_url)

# Filter the streams to get the highest resolution MP4
stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

# Download the video
stream.download()

print("Download Complete")



The program uses the pytube library to handle the YouTube video download.
It prompts the user to input a YouTube video URL.
It filters the available video streams to find the highest resolution MP4 format.
Finally, it downloads the video and notifies the user upon completion.


Contributing
If you have any suggestions or improvements, feel free to open an issue or submit a pull request.
