from ollama import Client

client = Client(host="http://127.0.0.1:11434")


def generate_script(topic, lang="en"):

    # 🌍 Language control
    if lang == "hi":
        instruction = "Write in Hindi."
    elif lang == "es":
        instruction = "Write in Spanish."
    else:
        instruction = "Write in English."

    
    prompt = f"""
    {instruction}

    Create a short engaging YouTube script.

    Topic: {topic}

    Rules:
    - Strong hook
    - Short sentences
    - 2–3 lines content
    - Simple language
    - Engaging ending

    Format:
    Hook
    Content
    Ending
    """

    try:
        # 🧠 Call Ollama
        response = client.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}]
        )

        script = response.message.content

        # ⚠️ Safety check
        if not script:
            print("⚠️ Empty response from model")
            return "Here’s something interesting you might not know. Stay curious and keep exploring."

        script = script.strip()

        
        script = script.replace("Title:", "")
        script = script.replace("Hook:", "")
        script = script.replace("Content:", "")
        script = script.replace("Ending:", "")

        return script

    except Exception as e:
        print("❌ Script generation error:", e)

        return "Here’s something interesting you might not know. Stay curious and keep exploring."