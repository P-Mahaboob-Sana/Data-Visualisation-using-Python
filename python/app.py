from flask import Flask, render_template,request
import openai

openai.api_key ="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"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quiz", methods=["POST", "GET"])
def quiz():
    if (request.method == "POST"):
        print(request.form)
        topic = request.form["topic"]
        questions = request.form["ques"]
        choices = request.form["choices"]
        difficulty = request.form["diff"]

    #     response = openai.ChatCompletion.create(
    #     model = "gpt-3.5-turbo",
    #     messages = [
    #         {
    #             "role": "system", 
    #             "content": f"Hey chat gpt prepare a quiz on this topic :{topic} and prepare {questions} number of choices for each of them keep {choices} number of choices, also keep the difficulty level {difficulty} , reply in the form of an object, make sure that response object contains topic, questions array contain, choices and answers"
    #         }
    #     ],
    #     #temperature creates random questions
    # temperature = 0.7
    #     )
    #     print(response)
    #     qiuz_content = request['choices'][0]['message'['content']]
    #     print(qiuz_content )
    qiuz_content = ""
    return render_template("quiz.html", qiuz_content= qiuz_content)

app.run(debug=True)