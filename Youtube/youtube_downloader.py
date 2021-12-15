"""Youtube module"""
import os
from pytube import YouTube



# enter link
link = input("Enter the link:  ")
yt = YouTube(link)


# Showing Details of Video
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length, "seconds")
print("Description: ", yt.description)
print("Ratings: ", yt.rating)

# Getting the highest resolution possible
yt = yt.streams.get_highest_resolution()


print("Downloading...")
yt.download()
print("Download completed!!")