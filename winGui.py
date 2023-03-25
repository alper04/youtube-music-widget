import tkinter as tk
from tkinter import filedialog
from storyMaker import addWidget, download_song
from PIL import Image, ImageTk

class StoryMakerGUI:
    def __init__(self, master):
        self.master = master
        master.title("StoryMaker by alper04")

        # Create widgets

        self.video_label = tk.Label(master, text="Video:")
        self.video_label.grid(row=6, column=0)

        self.video_path_entry = tk.Entry(master, state='readonly', width=50)
        self.video_path_entry.grid(row=6, column=1)

        self.video_upload_button = tk.Button(master, text="Upload", command=self.upload_video, width=10)
        self.video_upload_button.grid(row=6, column=2)
  
        self.audio_label = tk.Label(master, text="Audio start time (in seconds):")
        self.audio_label.grid(row=7, column=0)

        self.audio_entry = tk.Entry(master, text="0", width=50)
        self.audio_entry.insert(0, "0")
        self.audio_entry.grid(row=7, column=1)

        self.submit_button = tk.Button(master, text="Add Widget", command=self.add_widget, width=30)
        self.submit_button.grid(row=8, column=1)

        self.url_label = tk.Label(master, text="Song URL:")
        self.url_label.grid(row=0, column=0)

        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.grid(row=0, column=1)
        self.url_entry.insert(0, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        self.manualMode_var = tk.BooleanVar()
        self.manualMode_checkbutton = tk.Checkbutton(master, text="Manual Mode", variable=self.manualMode_var)
        self.manualMode_checkbutton.grid(row=1, column=1)

        self.title_label = tk.Label(master, text="Song Title:")
        self.title_label.grid(row=2, column=0)

        self.title_entry = tk.Entry(master, width=50)
        self.title_entry.grid(row=2, column=1)

        self.artist_label = tk.Label(master, text="Song Artist:")
        self.artist_label.grid(row=3, column=0)

        self.artist_entry = tk.Entry(master, width=50)
        self.artist_entry.grid(row=3, column=1)

        self.download_button = tk.Button(master, text="Download Song", command=self.download_song, width=30)
        self.download_button.grid(row=4, column=1)

    def upload_video(self):
        # Open file dialog to select video file
        video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])

        # Update video path entry with selected file
        self.video_path_entry.configure(state='normal')
        self.video_path_entry.delete(0, tk.END)
        self.video_path_entry.insert(0, video_path)
        self.video_path_entry.configure(state='readonly')

    def add_widget(self):
        video_path = self.video_path_entry.get()
        audio_start_time = int(self.audio_entry.get())

        # Call addWidget function from storyMaker.py
        addWidget(video_path, audio_start_time)

    def download_song(self):
        url = self.url_entry.get()
        manualMode = self.manualMode_var.get()
        mTitle = self.title_entry.get()
        mArtist = self.artist_entry.get()

        # Call download_song function from storyMaker.py
        download_song(url, manualMode, mTitle, mArtist)

        # Open the image file
        

if __name__ == '__main__':
    root = tk.Tk()
    my_gui = StoryMakerGUI(root)
    root.mainloop()
