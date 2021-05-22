from flask import Flask, render_template, request
from decouple import config
from utils import naive_bayes_predict


app = Flask(__name__)
app.config["SECRET_KEY"] = config('SECRET_KEY')
app.config['JSON_SORT_KEYS'] = False


@app.route("/", methods=["GET", "POST"])
def index():
    result = {}


    if request.method == "POST":
        my_text = request.form.get("word").strip().lower()


        p = naive_bayes_predict(my_text)
        if p > 0:
            # the predicted class is 1
            result[p] = "Your input text is positive and the score is: "
        else:
            # otherwise the predicted class is 0
            result[p] = "Your input text is negative and the score is: "
        

    return render_template("index.html", result=result)


