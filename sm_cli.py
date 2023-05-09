


#----------------------------------------#
# command line interface for story maker #
#----------------------------------------#
import argparse
import datetime
import webbrowser
from storyMaker import download_song, addWidget

# Define command-line arguments
parser = argparse.ArgumentParser(description='StoryMaker CLI')
subparsers = parser.add_subparsers(dest='command')

# Download command
download_parser = subparsers.add_parser('download', help='Download a song from a YouTube URL')
download_parser.add_argument('url', help='The YouTube URL of the song to download')
download_parser.add_argument('--manual-mode', action='store_true', help='Use manual mode to enter song title and artist')
download_parser.add_argument('--title', help='The title of the song (only used if --manual-mode is set)')
download_parser.add_argument('--artist', help='The artist of the song (only used if --manual-mode is set)')

# Add widget command
widget_parser = subparsers.add_parser('widget', help='Add a widget to a video')
widget_parser.add_argument('video_path', help='The path to the video file')
widget_parser.add_argument('audio_start_time', help='The start time of the audio to add, in seconds')


# Define the man sub-command
man_parser = subparsers.add_parser('man', help='Display the manual page')


# Parse arguments
args = parser.parse_args()



# Display man page if no command is provided
if not args.command:
    print('StoryMaker CLI\n')
    print('The StoryMaker CLI has the following commands:\n')
    print('download - Download a song from a YouTube URL')
    print('  Usage: python sm_cli.py download <url> [--manual-mode] [--title <title>] [--artist <artist>]')
    print('  Example: python sm_cli.py download https://www.youtube.com/watch?v=dQw4w9WgXcQ --manual-mode --title "Never Gonna Give You Up" --artist "Rick Astley"\n')
  
    print('widget - Add a widget to a video')
    print('  Usage: python sm_cli.py widget <video_path> <audio_start_time>')
    print('  Example: python sm_cli.py widget my_video.mp4 30\n')
   
    print('man - Display this man page')
else:
    # Call the appropriate function based on the command
    if args.command == 'download':
        download_song(args.url, args.manual_mode, args.title, args.artist)
    elif args.command == 'widget':
        addWidget(args.video_path, args.audio_start_time)
    elif args.command == 'man':

        # Check for easter egg condition
        now = datetime.datetime.now()
        if now.hour >= 0 and now.hour < 3:
            print("Gimme, gimme, gimme a man after midnight")
            print("Won't somebody help me chase the shadows away..")
            webbrowser.open('https://youtu.be/XEjLoHdbVeE?t=70')
        else:
            print('StoryMaker CLI\n')
            print('The StoryMaker CLI has the following commands:\n')
            print('download - Download a song from a YouTube URL')
            print('  Usage: python sm_cli.py download <url> [--manual-mode] [--title <title>] [--artist <artist>]')
            print('  Example: python sm_cli.py download https://www.youtube.com/watch?v=dQw4w9WgXcQ --manual-mode --title "Never Gonna Give You Up" --artist "Rick Astley"\n')
            
            print('widget - Add a widget to a video')
            print('  Usage: python sm_cli.py widget <video_path> <audio_start_time>')
            print('  Example: python sm_cli.py widget my_video.mp4 30\n')
            
            print('man - Display this man page')
