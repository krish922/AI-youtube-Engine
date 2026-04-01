from gtts import gTTS

def generate_voice(script, lang="en", output="voice.mp3"):
    tts = gTTS(text=script, lang=lang, slow=False)
    tts.save(output)
    return output