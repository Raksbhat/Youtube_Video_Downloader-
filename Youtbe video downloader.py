from pytube import YouTube
#paste your yt video link here below in link section
link="https://youtu.be/WNeLUngb-Xg"
yt=YouTube(link)
#printing Title of the video
print("Title: ",yt.title)
#Downloading the video
yd= yt.streams.get_highest_resolution()
yd.download()
print("Thank you for using this software")