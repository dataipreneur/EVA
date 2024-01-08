#!/usr/bin/env python
# coding: utf-8

# In[ ]:


mport openai
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from flask import Flask, request, jsonify


# Set up the OpenAI API client with your API key
openai.api_key = "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"
model_engine = "gpt-3.5-turbo"


# Define a function to generate a response to a user's message
def generate_response(user_input, max_tokens=500):
    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine=model,
        messages=[{"role": "system", "content": "You are a helpful assistant named EVA who is designed to answer questions related to electric vehicles to assist the user before taking a decison to rent a car using our application. If the user asks anything about the charging stations present nearby, politely tell the user to check the charging stations section in our application."},
         {"role": "user", "content": "How do Electric Cars Work?"},
         {"role": "assistant", "content": "Unlike traditional cars that use gasoline to fuel combustion engines, electric cars work exactly how they sound—electronically."},
         {"role": "user", "content": "How can I get to know about the charging stations nearby?"},
         {"role": "assistant", "content": "Please, use the charging stations section present in the app."}]
        prompt=user_input,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.1
    )

    # Extract the generated text from the OpenAI API response
    generated_text = response['choices'][0]['message']

    return generated_text.strip()


# Create a Flask web server instance
app = Flask(__name__)


# Define a route for handling HTTP POST requests
@app.route("/", methods=["POST"])
def handle_post_request():
    # Extract the user input from the request payload
    user_input = request.json.get("content", "")

    # Generate a response to the user's input
    response = generate_response(user_input)

    # Return the response as a JSON object
    return jsonify({"content": response})


if __name__ == "__main__":
    # Start the Flask web server
    app.run(debug=True, port=8080)

