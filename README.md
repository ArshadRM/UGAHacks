### trivi.study - The locally hosted AI-powered trivia generator.

## Team members

 - Allistair Hakim
 - Raghav Vikramprabhu
 - Arshad Mamarathar

## Inspiration

Utilize locally hosted AI projects and give more uses to consumer-grade computer hardware. In a way, we wanted to democratize the use of large AI generation models by using our own devices and not being forced to use expensive enterprise-grade solutions.
 
## What it does

This project automatically generates trivia training questions, answers, and images. However, all artificial intelligence algorithms are run on personally owned consumer-grade hardware. If your computer can run video games, it can run AI! There are zero communications sent or API tokens spent on commercial AI platforms (e.g. Gemini, Meta, OpenAI, or Deepseek). 

## How we built it

We used a frontend hosted by Github Pages, and a custom backend REST API hosted on our own hardware. Most importantly, open source AI model managers and models such as Ollama and Stable Diffusion to run this application.

## Challenges that we ran into

 - Getting communicating data between all the models correctly 
 - Dealing with AI hallucinations (especially with getting valid JSON outputs from an LLM)
 - Networking the local AI to work with public web-hosting

## Accomplishments we're proud of / What we learned

 - We created a trivia question generation 
 - Learned how to use Ollama and Stable Diffusion
 - Effectively hosted local language and image generation models with our own hardware.
 - We learned how to make AI generated content in response to each user's inputted trivia topic.

## Public Frameworks, Technologies, and Resources used for running the app.

 - Ollama : Offline language model AI manager
 - Open WebUI : Feature-rich offline LLM frontend / API

 - Stable Diffusion WebUI Forge : Offline image generation
 - Civit-ai : Repository for Image-Generation Models
 - Localtunnel : Easily share a web service on local developments
 
 - Flask : Python framework for easy API endpoint creation
 - Python : A simple yet robust programming language
 - Github : Frontend that hosts the webpage, and code manager for collaboration