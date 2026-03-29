from src.topic import get_topic
from src.script_generator import generate_script
from src.voice_generator import generate_voice
from src.video_builder import generate_video

def run_pipeline():
    topic = get_topic()
    script = generate_script(topic)

    audio = generate_voice(script)

    video = generate_video(script, audio)

    script = generate_script(topic)

    return topic, script, audio, video