
# Fake News Detection System 📰🔍

## 📌 Project Overview

The **Fake News Detection System** is a Machine Learning–based application that classifies news articles as **Fake** or **Real** using Natural Language Processing (NLP) techniques.
It uses text preprocessing, TF-IDF vectorization, and a supervised learning model to achieve high accuracy.

This project is suitable for **academic submissions**, **mini projects**, and **learning ML + NLP pipelines**.

---

## 🎯 Objectives

* Detect fake news automatically using machine learning
* Apply NLP techniques to real-world text data
* Build an end-to-end ML workflow (training → testing → prediction)
* Deploy the trained model using a Flask web application

---

## 🛠️ Technologies Used

* **Python 3.12**
* **Pandas, NumPy**
* **Scikit-learn**
* **NLTK**
* **Flask**
* **TF-IDF Vectorizer**
* **Git & GitHub**

---

## 📂 Project Structure

```
FakeNewsDetection/
│
├── app.py               # Flask web application
├── train_model.py       # Model training script
├── README.md            # Project documentation
├── .gitignore           # Ignored files/folders
│
├── data/                # Dataset folder (ignored on GitHub)
│   ├── Fake.csv
│   └── True.csv
│
├── model/               # Trained model files (ignored on GitHub)
│   ├── model.pkl
│   └── tfidf.pkl
│
└── venv/                # Virtual environment (ignored)
```

---

## 📊 Dataset

* **Fake.csv** → Fake news articles
* **True.csv** → Real news articles

📌 **Note:**
Due to GitHub file size limits, the dataset files are **not uploaded**.
You must download or place them manually inside the `data/` folder.

---

## ⚙️ Model Training

To train the model, run:

```bash
python train_model.py
```

✔ The script:

* Cleans text data
* Removes stopwords
* Applies TF-IDF vectorization
* Trains a machine learning classifier
* Saves the trained model as `.pkl` files

📈 **Achieved Accuracy:** ~98%

---

## 🚀 Running the Application

Start the Flask app using:

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🔒 GitHub Large File Handling

The following files are **ignored** using `.gitignore`:

* `data/`
* `model/`
* `venv/`
* `*.csv`
* `*.pkl`

This avoids GitHub push errors due to large file size restrictions.

---

## 🧠 Future Enhancements

* Use deep learning models (LSTM / BERT)
* Add news source credibility scoring
* Deploy on cloud (Heroku / Render)
* Improve UI with HTML/CSS

---

## 👩‍💻 Author

**Anshita Arya**
Computer Science Student

---

## 📜 License

This project is for **educational purposes only**.

---

✅ *If you want, I can also:*

* Simplify this for college submission
* Add screenshots section
* Create a report or PPT
* Fix GitHub push completely

Just tell me 👍
