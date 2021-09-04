from pytube import YouTube


link =input("Enter the link: ")

yt = YouTube(link)

print("Video name is : ")
print(yt.title)
print("\n")

filters=yt.streams.filter(progressive=True,file_extension='mp4')


stream=filters.get_highest_resolution()

#yt.streams.get_audio_only().download()

print("MetaData : ")
print(stream)
print("\n")

print("Downloading .........")
stream.download()
print("Download complete")
