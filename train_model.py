import pandas as pd
import nltk
import pickle
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Download stopwords (only first time)
nltk.download("stopwords")

# 🔥 ABSOLUTE PATH FIX
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

fake_path = os.path.join(DATA_DIR, "Fake.csv")
true_path = os.path.join(DATA_DIR, "True.csv")

# Load datasets
fake = pd.read_csv(fake_path)
true = pd.read_csv(true_path)

# Add labels
fake["label"] = 0   # Fake
true["label"] = 1   # Real

# Balance dataset
min_len = min(len(fake), len(true))
fake = fake.sample(min_len, random_state=42)
true = true.sample(min_len, random_state=42)

# Combine & shuffle
data = pd.concat([fake, true])
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

X = data["text"]
y = data["label"]

# TF-IDF
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.7,
    ngram_range=(1, 2)
)

X_vec = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save model
MODEL_DIR = os.path.join(BASE_DIR, "model")
os.makedirs(MODEL_DIR, exist_ok=True)

with open(os.path.join(MODEL_DIR, "fake_news_model.pkl"), "wb") as f:
    pickle.dump(model, f)

with open(os.path.join(MODEL_DIR, "tfidf.pkl"), "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model trained and saved successfully ")



