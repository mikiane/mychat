# -*- coding: utf-8 -*-
'''
Filename: generatechatcompletion.py
Author: Michel Levy Provencal
Description: This file defines two functions, generate_chat_completion and generate_chat, that use OpenAI's API to generate chat responses. It uses environmental variables for API keys and includes a default model of "gpt-4" if no model is specified in the function parameters.
'''

import openai  # Import the openai API package
import os  # Import os module for interacting with the operating system
from dotenv import load_dotenv  # Import dotenv module for loading .env files

# Load the environment variables from the .env file
load_dotenv(".env")

# Set the OpenAI API key from the environment variables
openai.api_key = os.environ['OPEN_AI_KEY']

# Function to generate chat completions
def generate_chat_completion(consigne, texte, model="gpt-4"):
    prompt = str(consigne + " : " + texte)  # Construct the prompt from the given consigne and texte
    # Call the OpenAI API to create a chat completion
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {'role': 'system', 'content': "Je suis un assistant parlant parfaitement le français et l'anglais capable de corriger, rédiger, paraphraser, traduire, résumer, développer des textes. "},
            {'role': 'user', 'content': prompt }
        ],
        temperature=0,
        stream=True
    )
    # For each part of the response
    for chunk in response:
        # If the part contains a 'delta' and the 'delta' contains 'content'
        if 'delta' in chunk['choices'][0] and 'content' in chunk['choices'][0]['delta']:
            content = chunk['choices'][0]['delta']['content']  # Extract the content
            yield f"{content}"  # Yield the content as a string

# Function to generate chat
def generate_chat(consigne, texte, system, model="gpt-4"):
    prompt = str(consigne + " : " + texte)  # Construct the prompt from the given consigne and texte
    # Call the OpenAI API to create a chat
    
    prompt = prompt[-10000:]
    if model == "gpt-4":
        prompt = prompt[-10000:]
    if model == "gpt-3.5-turbo-16k":
        prompt = prompt[-40000:]
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {'role': 'system', 'content': system },
            {'role': 'user', 'content': prompt }
        ],
        temperature=0,
        stream=True
    )
    # For each part of the response
    for chunk in response:
        # If the part contains a 'delta' and the 'delta' contains 'content'
        if 'delta' in chunk['choices'][0] and 'content' in chunk['choices'][0]['delta']:
            content = chunk['choices'][0]['delta']['content']  # Extract the content
            print(content)
            yield f"{content}"  # Yield the content as a string
