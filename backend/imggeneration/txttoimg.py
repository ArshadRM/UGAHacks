import requests

import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now import the method
from llm.llm import ask_ollama

def query_tti(prompt: str, negative_prompt: str):
    url = "http://win-arsh:7860/sdapi/v1/txt2img"  # Replace with your actual image generation API endpoint

    # JSON data to be sent in the POST request, contains our stable diffusion parameters
    data = {
        "prompt": prompt + "pixels, pixel art,  <lora:pixelbuildings128-v2:1>, (white background)",
        "negative_prompt": "text,watermark,blurry, deformed, depth of field,realistic, 3d render, outline, worst quality, low quality, lowres,out of focus, watermark, signature, logo, text, repeating patterns",
        "styles": ["string"],
        "steps": 20
    }

    # "Authorization": "Bearer YOUR_API_KEY"  # Add your API key here
    headers = {
        "Content-Type": "application/json",  # Set the content type as JSON
    }

    # Sending POST request with the JSON data
    try:
        response = requests.post(url, json=data, headers=headers)
        
        # Check if the response is successful
        if response.status_code == 200:
            response_data = response.json()
            # Assuming the response contains an image URL or base64 encoded image
            if 'images' in response_data:
                print("Image generated successfully!")
                # Example: If the response contains the image as a URL
                #print("Image URL:", response_data['images'][0])  # base64 image

                image_data = response_data['images'][0] #store image data in base64 to pass up to client
                return image_data 
        else:
            print(f"Failed with status code {response.status_code}: {response.text}")
            return -1
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {str(e)}")

def generate_image(prompt: str):
    # Generate the positive and negative prompts from the query
    response = ask_ollama("llama3.2:latest", 
                          f"Make one long and comprehensive Stable Diffusion image prompt about {prompt}. All image prompts must be 30 adjectives in a comma list. All prompts must be about physical object that represent {prompt}. Each object must be more complex than the last one. Respond with the prompt itself")
    
    # Print only the response content
    if "choices" in response and response["choices"]:
        posneg = response["choices"][0]["message"]["content"]
        # Split the response into lines
        # lines = posneg.split("\n")

        # Extract values
        # positive_prompt = lines[0].replace("Positive: ", "").strip()
        # negative_prompt = lines[1].replace("Negative: ", "").strip()
        
        image_base64 = query_tti(posneg, "")
        return image_base64
    else:
        print("No valid positive and negative prompt generation response found.")

def generate_upgrades(topic: str):
    response = ask_ollama("jsonllama32", f"""

    Make 5 pixel art Stable Diffusion image prompts about {topic}. All image prompts must be 15 adjectives in a comma list. All prompts must be about physical objects that represent {topic}. Each object must be more complex than the last one. All responses must be in this JSON format.

[
    {
    "object": "Temple Ruins",
        "prompt": "Ancient Egyptian temple ruins, crumbling stone structures, worn sandstone facades, weathered hieroglyphics"

    },
    {
    "object": "cathedral",
        "prompt": "Majestic Gothic cathedral, intricate stone carvings, stained glass windows, ornate Gothic arches"
    }
] 

""")

    print(response)
