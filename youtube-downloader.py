from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = yt.streams.get_by_resolution('720p')
        highest_res_stream.download(save_path)
        print("Video Downloaded Successfully")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")

    return folder



if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    vid_url = input("Enter the URL of the video: ")
    save_dir = open_file_dialog()
    
    if not save_dir:
        print("No folder selected. Exiting...")
        exit()
    else:
        download_video(vid_url, save_dir)