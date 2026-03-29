from moviepy import ImageClip, AudioFileClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def generate_video(script, audio_path, output="video.mp4"):

    # Create image
    img = Image.new("RGB", (720, 480), color=(20, 20, 20))
    draw = ImageDraw.Draw(img)

    # Load font (this works reliably)
    font = ImageFont.load_default()
    lines = script.split('.')
    display_text = "\n".join(lines[:3])
    # Draw text
    draw.text((50, 150), display_text, font=font, fill="white")
    color = (15, 15, 40)

    # Convert to numpy array
    frame = np.array(img)

    # Create video clip
    image_clip = ImageClip(frame)

    audio = AudioFileClip(audio_path)

    video = image_clip.with_duration(audio.duration).with_audio(audio)

    video.write_videofile(output, fps=24)

    return output