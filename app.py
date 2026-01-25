from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained pipeline
with open("sentiment_analysis.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    user_text = ""

    if request.method == "POST":
        user_text = request.form["text"]
        prediction = model.predict([user_text])[0]
        prediction = prediction.capitalize()
               
    return render_template("index.html", prediction=prediction, user_text=user_text)

if __name__ == "__main__":
    app.run(debug=True)
