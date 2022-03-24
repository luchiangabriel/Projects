
from pytube import YouTube
import os

url = input("Enter the URL: ")
yt = YouTube(url)

print()
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length, "seconds")
# print("Description: ", yt.description)
print("Ratings: ", yt.rating)
print()
print("""
Choose an option: 1. Download video
                  2. Download audio""")
option = int(input("\nOption: "))


def download(x):
    if x == 1:
        ys = yt.streams.get_highest_resolution()
        print("Downloading...")
        ys.download()
        print("Downloaded")
    elif x == 2:
        video = yt.streams.filter(only_audio=True).first()
        print("Downloading...")
        out_file = video.download(output_path=".")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("Downloaded")
    else:
        print("\nInvalid option")
        print("""
Choose an option: 1. Download video
                  2. Download audio""")
        choice = int(input("\nOption: "))
        download(choice)


if __name__ == '__main__':
    download(option)
