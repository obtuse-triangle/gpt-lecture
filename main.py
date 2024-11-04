from flask import Flask, render_template, request, jsonify
from simple_ask import response_gpt
from summarize import summarize
from image_gpt import get_image

from for_project import refrigeratorSummarize

app = Flask(__name__)


@app.route("/")
def index():
  return "Hello World!"


@app.route("/ask", methods=["POST"])
def ask_gpt():
  request_data = request.get_json()
  data = {"response": response_gpt(request_data['ask'])}
  return jsonify(data)


@app.route("/summarize", methods=["POST"])
def summarize_gpt():
  request_data = request.form
  print(request_data)

  data = {"response": summarize(request_data['text'])}
  return jsonify(data)


@app.route("/image", methods=["POST"])
def image():
  request_data = request.get_json()
  topic = request_data["topic"]
  mood = request_data["mood"]
  result = get_image(topic, mood)
  data = {"response": result}
  return jsonify(data)


@app.route("/refrigeratorSummarize", methods=["POST"])
def refrigerator():
  request_data = request.get_json()
  text = request_data["text"]
  data = {"response": refrigeratorSummarize(text)}
  return jsonify(data)


if __name__ == "__main__":
  app.run(host="127.0.0.1", debug=True, port=5001)
