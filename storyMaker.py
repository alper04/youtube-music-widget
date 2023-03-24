
def addWidget(video_path, audio_path, audio_start_time):

    from moviepy.editor import VideoFileClip, AudioFileClip, ImageClip, CompositeVideoClip
    from PIL import Image
    import wand.image

    with wand.image.Image(filename='updated.svg') as img:
        img.format = 'png'
        img.save(filename='image.png')

    # Load the video and audio clip
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

   

    width, height = video_clip.size
    # Open the image
    image = Image.open('image.png')
    temp_size = (int(width/2.5), int(image.height/image.width*width/2.5))
    image_temp = image.resize(temp_size)


    # Define the new width and height of the image
    new_width = width
    new_height = height

    # Create a new transparent image with the new dimensions
    new_image = Image.new('RGBA', (new_width, new_height), (0, 0, 0, 0))

    # Paste the original image onto the new image, shifted to the top left corner
    new_image.paste(image_temp, (width - int(width/10) - int(width/2.5), int(width/10)))

    # Save the new image
    new_image.save('output_image.png')




    clip2 = ImageClip("output_image.png", duration = video_clip.end)
    
     # Extract the desired portion of the audio clip
    audio_clip = audio_clip.subclip(audio_start_time, audio_start_time + video_clip.end)

    # Set the audio of the video clip to the extracted audio clip
    #final_clip2 = final_clip.set_audio(audio_clip)
    
    # creating a composite video
    final_clip = (CompositeVideoClip([video_clip, clip2])).set_audio(audio_clip)

    # Write the final clip to a file
    final_clip.write_videofile("output.mp4")

    print("Audio and video combined successfully!")







def download_song(url):

    import requests
    from io import BytesIO
    from pytube import YouTube
    from PIL import Image
    import re

    # Create a Pytube YouTube object with the music video URL
    yt = YouTube(url)

    # Get the first available audio stream
    audio_stream = yt.streams.filter(only_audio=True).first()
    yt.thumbnail_url

    # Download the audio stream to a file named "song.mp4"
    audio_stream.download(filename="song.mp3")
    

    # Get the thumbnail URL for the highest resolution thumbnail available
    thumbnail_url = yt.thumbnail_url.split("?")[0]

    print("Audio downloaded successfully!")


    # Download the thumbnail image
    response = requests.get(thumbnail_url)
    thumbnail_image = Image.open(BytesIO(response.content))

    
    # Get the size of the image
    width, height = thumbnail_image.size

    # Find the minimum size of the width and height
    min_size = min(width, height)

    # Calculate the coordinates for the crop box
    left = (width - min_size) // 2
    top = (height - min_size) // 2
    right = (width + min_size) // 2
    bottom = (height + min_size) // 2

    # Crop the image to the square aspect ratio
    thumbnail_image = thumbnail_image.crop((left, top, right, bottom))


    # Save the cropped thumbnail image to a file
    thumbnail_image.save("thumbnail.jpg")

    print("Thumbnail downloaded and cropped successfully!")


    # Get the video title and artist name
    title = yt.title.replace(yt.author, "")
    title = re.sub(r"[^\w\s]", "", title)

    video_title = title[:17] + "..." if len(title) > 17 else title 
    artist_name = yt.author[:17] + "..." if len(yt.author) > 17 else yt.author

    # Print the formatted video title and artist name
    print(f"{video_title} - {artist_name}")

    with open('template.svg', 'r') as f:
        svg_str = f.read()

    svg_str = svg_str.replace('str1', video_title).replace('str2', artist_name)

    with open('updated.svg', 'w') as f:
        f.write(svg_str)





