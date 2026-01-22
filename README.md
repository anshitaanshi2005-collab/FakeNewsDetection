
<<<<<<< HEAD

FakeNewsDetection
It detect fake news

Dataset
The dataset files are not uploaded due to GitHub file size limits.

Download the dataset from: https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset

Place the files inside: data/Fake.csv data/True.csv

Fake News Detection using Machine Learning
📌 Project Description
This project detects whether a news article is Fake or Real using Machine Learning and Natural Language Processing techniques.

🛠 Technologies Used
Python
Pandas
Scikit-learn
Flask
TF-IDF Vectorizer
Logistic Regression
GitHub

📂 Project Structure FakeNewsDetection/ │ ├── app.py # Flask web application ├── train_model.py # Model training script ├── README.md # Project documentation ├── .gitignore # Ignored files/folders │ ├── data/ # Dataset folder (ignored on GitHub) │ ├── Fake.csv │ └── True.csv │ ├── model/ # Trained model files (ignored on GitHub) │ ├── model.pkl │ └── tfidf.pkl │ └── venv/ # Virtual environment (ignored)

📊 Dataset

Fake.csv → Fake news articles

True.csv → Real news articles

📌 Note: Due to GitHub file size limits, the dataset files are not uploaded. You must download or place them manually inside the data/ folder.

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

http://127.0.0.1:5000/ 🔒 GitHub Large File Handling

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

Anshita Arya Computer Science Student

📜 License

This project is for educational purposes only.
## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform


## Tech Stack

**Client:** React, Redux, TailwindCSS

**Server:** Node, Express


## Roadmap

- Additional browser support

- Add more integrations


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
    
## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.



