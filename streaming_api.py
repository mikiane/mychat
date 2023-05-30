# -*- coding: utf-8 -*-
'''
Filename: server.py
Author: Michel Levy Provencal
Description: This Flask application handles two types of chat requests: streaming chat and standard chat. If no 'model' parameter is specified, it defaults to "gpt-4".

Modifications: The code has been updated to include a default model if no 'model' parameter is specified in the request.
'''

# Import a module to generate chat responses
import generatechatcompletion

# Import os module for interacting with the operating system
import os

# Import Flask and related modules for building a web server
from flask import Flask, Response, request, jsonify

# Import a module to handle Cross-Origin Resource Sharing (CORS)
from flask_cors import CORS

# Create a new Flask web server application
app = Flask(__name__)

# Enable CORS for the Flask app for all routes and a specific origin
CORS(app, resources={r"/*": {"origins": "https://ai.brightness.agency"}})

# Define a route for streaming chat, accepting POST requests
@app.route('/stream_chat', methods=['POST'])
def stream_chat():
    # Get the JSON data from the POST request
    data = request.get_json()

    # Retrieve individual data points from the JSON, defaulting 'model' to 'gpt-4' if it's not provided
    consigne = data.get('consigne')
    texte = data.get('texte')
    model = data.get('model', 'gpt-4')  # Default to 'gpt-4' if no model is provided

    # Import module to unescape URL-encoded strings
    from urllib.parse import unquote

    # Decode any URL-encoded strings in the data
    consigne = unquote(consigne)
    texte = unquote(texte)

    # Generate a chat completion and return it as a server-sent event
    return Response(generatechatcompletion.generate_chat_completion(consigne, texte, model), content_type='text/event-stream')

# Define a route for standard chat, accepting POST requests
@app.route('/chat', methods=['POST'])
def chat():
    # Get the JSON data from the POST request
    data = request.get_json()

    # Retrieve individual data points from the JSON, defaulting 'model' to 'gpt-4' if it's not provided
    consigne = data.get('consigne')
    texte = data.get('texte')
    system = data.get('system')
    model = data.get('model', 'gpt-4')  # Default to 'gpt-4' if no model is provided

    # Import module to unescape URL-encoded strings
    from urllib.parse import unquote

    # Decode any URL-encoded strings in the data
    consigne = unquote(consigne)
    texte = unquote(texte)

    # Generate a chat and return it as a server-sent event
    return Response(generatechatcompletion.generate_chat(consigne, texte, system, model), content_type='text/event-stream')

# If this script is run directly, start the Flask server
if __name__ == '__main__':
    # Run the application with debug mode enabled
    app.run(debug=True)

    # Uncomment the following lines to run the app on a specific port
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
