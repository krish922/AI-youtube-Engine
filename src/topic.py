import random 

def get_topic():
    topics = [
        "Craete a short explaination of the theory of relativity in simple terms",
        "what is the theory of relativity in simple terms?",
        "What are the key principles of the theory of relativity?",
        "How does the theory of relativity explain the relationship between space and time?",
        "What are some real-world applications of the theory of relativity?",
        "How did Albert Einstein develop the theory of relativity?",
        "What are the differences between special relativity and general relativity?",
        "How does the theory of relativity impact our understanding of the universe?",
        "What are some common misconceptions about the theory of relativity?",
        "How has the theory of relativity influenced modern physics and cosmology?"
    ]
    return random.choice(topics)