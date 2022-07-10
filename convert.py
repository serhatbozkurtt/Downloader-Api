from pytube import YouTube
import os


#link2 = input("Link: ")
link =  "https://www.youtube.com/watch?v=Ab5g3Ug7ysM"
#directory = input("Directory: ")

try:
    yt = YouTube(link)
except:
    print("Invalid link")
    exit()

mp3 = yt.streams.filter(only_audio=True).first()

print("Downloading...")


s = "namekontr3"
#output = mp3.download( filename='namekontr1%s.mp3'%s)
output = mp3.download( filename='%s.mp3' %s)


#base, ext = os.path.splitext(output)
#to_mp3 = base + ".mp3"
#os.rename(output, to_mp3)

print("Download complete")



