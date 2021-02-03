from pytube import YouTube
from pytube import Playlist

url = input(str("input_Link: "))
ytd = YouTube(url).streams.first().download()
print(ytd)


