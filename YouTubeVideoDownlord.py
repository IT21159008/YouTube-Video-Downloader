from pytube import YouTube

link = input("Enter the video link: ")
yt = YouTube(link)

downloader = yt.streams.get_highest_resolution()
print("Downloading...")

downloader.download(filename="video.mp4")
print("Download completed")
