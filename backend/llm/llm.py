import requests

api_key = "sk-08db4e2ba41848eb9235b1b52610bcfb"

def ask_ollama(model: str, message: str, server_url: str = "http://win-arsh:3000/api/chat/completions", api_key: str = api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    }

    try:
        response = requests.post(server_url, json=data, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": "Failed to get a response",
                "status_code": response.status_code,
                "message": response.text
            }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    
def generate_questions(topic: str, api_key: str = api_key):
    question = """Give me 10 multiple choice questions and answers about """ + topic + """ in this JSON format don't say anything else.
    [
    {
      question: "What is 2 + 2?",
      answer: "4",
      options: ["3", "4", "5", "6"]
    },
    {
      question: "Which planet is closest to the Sun?",
      answer: "Mercury",
      options: ["Venus", "Mercury", "Mars", "Earth"]
    },
    {
      question: "What is the capital of France?",
      answer: "Paris",
      options: ["London", "Berlin", "Paris", "Madrid"]
    },
    {
      question: "How many continents are there?",
      answer: "7",
      options: ["5", "6", "7", "8"]
    }
  ]
    """
    response = ask_ollama("jsonllama32", question)

    # Print only the response content
    if "choices" in response and response["choices"]:
        return response["choices"][0]["message"]["content"]
    else:
        return "No valid response found."