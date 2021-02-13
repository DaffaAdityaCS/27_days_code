from pytube import YouTube
import os

link = str(input("Link: "))
yt = YouTube(link)

name = str(input("File Name: " ))

out_donwload = yt.streams.filter(only_audio=True).first().download()

print("Donwloading....")

file = out_donwload
base = os.path.splitext(file)[0]

if name == '':
    os.rename(out_donwload, base + '.mp3')
else:
    os.rename(out_donwload, name + '.mp3')

print("Finish")