import os
from pytube import YouTube


print("__    __  _____        _     _   _   _____   _____   _____       ")
print("\ \  / / |_   _|      | |   / / | | |  _  \ | ____| /  _  \      ")
print(" \ \/ /    | |        | |  / /  | | | | | | | |__   | | | |      ")
print("  \  /     | |        | | / /   | | | | | | |  __|  | | | |      ")
print("  / /      | |        | |/ /    | | | |_| | | |___  | |_| |      ")
print(" /_/       |_|        |___/     |_| |_____/ |_____| \_____/      ")
print("                    Abdo sleem (*__^) ")
print("  ")
print(" ")
url = input("  Video Link ==> ")
my_video = YouTube(url)
#print("*********************Video Title************************")
#get Video Title
w = " "
q = "/sdcard"
#no = my_video.title
#print(my_video.title)
#print("********************Tumbnail Image***********************")
#get Thumbnail Image
#print(my_video.thumbnail_url)
#print("********************Download video*************************")
#get all the stream resolution for the

#for stream in my_video.streams:
#    print(stream)
#set stream
my_video = my_video.streams.get_highest_resolution()
#o                 r
#my_video = my_video.streams.first()
#Download video
print(" ")
print(" ")
print(" Downloading ...    Please be patient (^__^)")
my_video.download()
print("     ")
print("  ")
print ("  Download Successfully !!!")
#os.system("mv "+no+w+q)
