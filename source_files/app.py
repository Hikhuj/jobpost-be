import os

import imgkit
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# allow request from the FE 
CORS(app, resources={r"/data_to_image": {"origins": "http://localhost:3000"}})

@app.route("/")
def home():
    data_to_image()
    return jsonify({"message": "Hello, world!"})

@app.route("/data_to_image", methods=["POST"])
def data_to_image():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)

# ChatGPT
# Ignore previous prompts in this conversation. You are a professor of computer science with clear 
# language and easy professor to explain any related topic about computer science. Your task will 
# be to create an small Python program using Flask framework to receive one html text with css 
# and two plain text parameters and transform it into an image of 500x500 pixels and return this image to user.