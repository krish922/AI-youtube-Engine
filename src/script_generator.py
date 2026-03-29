from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.moonshot.cn/v1"
)

def generate_script(topic):

    prompt = f"""
    Create a short engaging YouTube script.

    Topic: {topic}

    Structure:
    - Hook (1 line)
    - Content (2-3 lines)
    - Ending (1 line)
    """

    response = client.chat.completions.create(
        model="kimi-k2-preview",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content