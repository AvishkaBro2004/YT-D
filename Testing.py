import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
from pytube import YouTube

print("")
print(Back.LIGHTGREEN_EX+Fore.BLACK+"Youtube Video / MP3 Downloader")
print(Fore.LIGHTWHITE_EX+"Made By Avishka *|* ")
print("")

link =input(Fore.YELLOW+"Enter Video Link : ")
data = YouTube(link)
print(data.title)
print("")
print(Fore.CYAN+"Loading Your Video Qualities....")
video = data.streams.all()
#video = YouTube.streams.filter(only_audio=True)
vid = list(enumerate(video))
for i in vid :
    print (i)
print ("")
cho=int(input(Fore.LIGHTMAGENTA_EX+"Enter No :"))
print("")
print(Fore.GREEN+"Downloading Your Video...")

video[cho].download()
print(Back.RED+Fore.BLACK+"Download successfull")










