"""Youtube module"""
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
ys = yt.streams.get_highest_resolution()


print("Downloading...")
ys.download()
print("Download completed!!")
