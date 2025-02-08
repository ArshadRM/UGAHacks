import requests

api_key = "sk-08db4e2ba41848eb9235b1b52610bcfb"

def ask_ollama(api_key: str, model: str, message: str, server_url: str = "http://win-arsh:3000/api/chat/completions"):
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
    question = f"Give me 10 multiple choice questions and answers about {topic} in a JSON format don't say anything else."
    response = ask_ollama(api_key, "llama3.2:latest", question)

    # Print only the response content
    if "choices" in response and response["choices"]:
        return response["choices"][0]["message"]["content"]
    else:
        return "No valid response found."
