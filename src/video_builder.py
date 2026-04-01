from moviepy import ImageClip, AudioFileClip, TextClip, CompositeVideoClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import textwrap

def create_text_image(text, width=720, height=480, font_size=40):
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # Wrap text
    lines = textwrap.wrap(text, width=25)

    line_heights = []
    line_widths = []

    # Correct width/height calculation
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        line_widths.append(w)
        line_heights.append(h)

    total_text_height = sum(line_heights) + (10 * (len(lines) - 1))

    # Frame area (match your background)
    frame_x1, frame_y1 = 50, 50
    frame_x2, frame_y2 = width - 50, height - 50

    frame_width = frame_x2 - frame_x1
    frame_height = frame_y2 - frame_y1

    # Start Y (centered inside frame)
    y = frame_y1 + (frame_height - total_text_height) // 2

    # Draw lines
    for i, line in enumerate(lines):
        w = line_widths[i]
        h = line_heights[i]

        x = frame_x1 + (frame_width - w) // 2

        draw.text((x, y), line, font=font, fill=(255, 255, 255, 255))

        y += h + 10  # move down

    return img

backgrounds = [
    "assets/blank-blue-leafy-poster_53876-118169(1).jpg",
    "assets/beautiful-flower-arrangement-neon-frame-flowers-dark-blue-background-empty-photo-frame-text-greeting-card-flat-lay-copy-space-3-d-illustration_200694-277.jpg.jpg",
    "assets/sunrise-over-snowcapped-mountains-photo2x.jpg",
    ]

def get_background(topic):
    if "food" in topic.lower():
        return "assets/pexels-dreamer-dude-724231353-18379774.jpg"
    elif "ai" in topic.lower():
        return"assets/igor-omilaev-eGGFZ5X2LnA-unsplash.jpg"
    else:
        return "assets/beautiful-flower-arrangement-neon-frame-flowers-dark-blue-background-empty-photo-frame-text-greeting-card-flat-lay-copy-space-3-d-illustration_200694-277.jpg"

    
def generate_video(script, audio_path, topic, output="video.mp4"):

    lines = [line.strip() for line in script.split("\n") if line.strip()]
    clips = []
    
    bg_path = get_background(topic)

    audio = AudioFileClip(audio_path)
    duration_per_line = audio.duration / len(lines)

    for line in lines:
        bg = ImageClip(bg_path).with_duration(duration_per_line).resized((720, 480))

        txt_image = create_text_image(line)
        txt = ImageClip(np.array(txt_image)).with_duration(duration_per_line).with_position('center')
        
        clip = CompositeVideoClip([bg, txt])
        clips.append(clip)

    video = concatenate_videoclips(clips)
    video = video.with_audio(audio)

    video.write_videofile(output,
    fps=24)

    return output