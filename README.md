# Chat Completion Project

This project provides a server-side implementation for generating responses to user inputs using OpenAI's GPT-4 model. The server is built with Python and Flask, and a simple web client is provided to interact with the server.

## Server

The server has two endpoints: `/stream_chat` and `/chat`. Both endpoints accept POST requests with the fields "consigne", "texte", and optionally "model" and "system".

The server uses the OpenAI's API to generate responses to the user inputs. The default model is "gpt-4", but this can be specified in the request.

The server takes care of creating prompts from user inputs, making requests to the OpenAI API, and parsing the responses. The responses are sent back to the client as a stream of text.

The server code can be found in the files `main.py` and `generatechatcompletion.py`.

## Client

The client is a simple web page with a form for user input. The form has two fields: "consigne" and "texte". When the form is submitted, a POST request is made to the server, and the server's response is displayed in a div on the page.

The client code is JavaScript embedded in an HTML page.

## Getting Started

To run the server, install the required Python packages with `pip install -r requirements.txt`, and then run `python main.py`. You'll need to provide your OpenAI API key in an environment variable.

To view the client, simply open the HTML page in a web browser.

## Authors

Michel Levy Provencal
