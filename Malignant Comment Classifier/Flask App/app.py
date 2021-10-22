from flask import Flask, render_template, request
import pickle

# Load the Multinomial Naive Bayes model and TFIDF object from disk
filename = "model_toxic_NB.pkl"
classifier = pickle.load(open(filename, "rb"))
tv = pickle.load(open("tf-transform.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form["message"]
        data = [message]
        vector = tv.transform(data).toarray()
        my_prediction = classifier.predict(vector)
        return render_template("results.html", prediction=my_prediction)





if __name__ == "__main__":
    app.run(debug=True)