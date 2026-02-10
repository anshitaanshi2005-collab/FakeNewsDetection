
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
📊 Dataset (Kaggle)

The dataset used in this project is sourced from Kaggle:

🔗 Fake and Real News Dataset
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

Dataset Details

Fake.csv – Fake news articles

True.csv – Real news articles

Key columns:

title

text

subject

date

⚠️ Due to GitHub file size restrictions, the dataset files are not included in this repository.
Please download them from Kaggle and place them inside the data/ directory.

📈 Model Accuracy

Feature Extraction: TF-IDF Vectorization

Model Type: Machine Learning Classifier

Evaluation Metric: Accuracy

Final Accuracy: 98.21%

Accuracy: 0.9821


This high accuracy demonstrates the model’s strong ability to distinguish between fake and real news articles.

🧠 Key Features

Text preprocessing and cleaning

Stopword removal using NLTK

TF-IDF based feature extraction

Supervised machine learning classification

Trained model saved for reuse.








