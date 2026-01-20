<<<<<<< HEAD
# FakeNewsDetection
It detect fake news 
## Dataset
The dataset files are not uploaded due to GitHub file size limits.

Download the dataset from:
https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset

Place the files inside:
data/Fake.csv
data/True.csv

# Fake News Detection using Machine Learning

## 📌 Project Description
This project detects whether a news article is **Fake** or **Real** using
Machine Learning and Natural Language Processing techniques.

## 🛠 Technologies Used
- Python
- Pandas
- Scikit-learn
- Flask
- TF-IDF Vectorizer
- Logistic Regression

GitHub

📂 Project Structure
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

📊 Dataset

Fake.csv → Fake news articles

True.csv → Real news articles

📌 Note:
Due to GitHub file size limits, the dataset files are not uploaded.
You must download or place them manually inside the data/ folder.

⚙️ Model Training

To train the model, run:

python train_model.py

✔ The script:

Cleans text data

Removes stopwords

Applies TF-IDF vectorization

Trains a machine learning classifier

Saves the trained model as .pkl files

📈 Achieved Accuracy: ~98%

🚀 Running the Application

Start the Flask app using:

python app.py

Then open your browser and go to:

http://127.0.0.1:5000/
🔒 GitHub Large File Handling

The following files are ignored using .gitignore:

data/

model/

venv/

*.csv

*.pkl

This avoids GitHub push errors due to large file size restrictions.

🧠 Future Enhancements

Use deep learning models (LSTM / BERT)

Add news source credibility scoring

Deploy on cloud (Heroku / Render)

Improve UI with HTML/CSS

👩‍💻 Author

Anshita Arya
Computer Science Student

📜 License

This project is for educational purposes only.


