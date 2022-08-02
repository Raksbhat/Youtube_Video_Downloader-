from pytube import YouTube
#paste your yt video link here below in link section
link=input("Enter your link here")
yt=YouTube(link)
#printing Title of the video
print("Title: ",yt.title)
#Downloading the video
yd= yt.streams.get_highest_resolution()
yd.download(#specify the download path)
print("Thank you for using this software")
