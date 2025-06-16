
from flask import Flask, render_template, request, jsonify
import json
from difflib import get_close_matches

app = Flask(__name__)

def load_knowledge_base():
    with open("knowledge_base.json", "r") as file:
        data = json.load(file)
    return data

def find_best_match(user_question, questions):
    matches = get_close_matches(user_question.lower(), questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question, knowledge_base):
    for q in knowledge_base["questions"]:
        if q["question"].lower() == question.lower():
            return q["answer"]
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("user_message", "").strip().lower()
    knowledge_base = load_knowledge_base()
    questions = [q["question"] for q in knowledge_base["questions"]]
    best_match = find_best_match(user_input, questions)
    if best_match:
        answer = get_answer_for_question(best_match, knowledge_base)
    else:
        answer = "I don't know the answer. Can you teach me?"
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)
