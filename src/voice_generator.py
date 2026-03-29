from gtts import gTTS

def generate_voice(script,filename="output.mp3"):

    clean_script = script.replace("\n"," ")

    tts= gTTS(text=script,lang='hi', slow=False)
    tts.save(filename)

    return filename 