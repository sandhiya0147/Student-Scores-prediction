from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    hours = float(request.form['hours'])
    input_features = np.array([[hours]])
    prediction = model.predict(input_features)[0]
    return render_template("result.html", hours=hours, score=round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)
