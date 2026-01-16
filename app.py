from flask import Flask, request, jsonify
import pickle

# Load model and vectorizer
with open("model/fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/tfidf.pkl", "rb") as f:
    vectorizer = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return "Fake News Detection API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    if text.strip() == "":
        return jsonify({"error": "No text provided"})

    vector = vectorizer.transform([text])

    # Probability-based prediction
    probs = model.predict_proba(vector)[0]
    fake_prob = round(probs[0] * 100, 2)
    real_prob = round(probs[1] * 100, 2)

    if real_prob > 60:
        prediction = "Real News"
    else:
        prediction = "Fake News"

    return jsonify({
        "prediction": prediction,
        "real_probability": f"{real_prob}%",
        "fake_probability": f"{fake_prob}%"
    })

if __name__ == "__main__":
    app.run(debug=True)
    c

