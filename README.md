

```markdown
# 🩺 Diabetes Prediction Web App

This is a simple web application built with **Django** and **Machine Learning** that predicts whether a person is likely to have diabetes based on medical input data.

## 🚀 Features

- Predicts diabetes using Logistic Regression
- Clean, dark-themed user interface
- Real-time prediction with form input
- Color-coded result display:
  - 🟢 **Positive** → Green
  - 🔴 **Negative** → Red

## 🧪 Tech Stack

- **Python**
- **Django**
- **Pandas**
- **Scikit-learn**
- **HTML/CSS** (for UI)

## 🗂️ Project Structure

```

DiabetesPrediction/
├── DiabetesPrediction/
│   ├── **init**.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
│   ├── home.html
│   └── predict.html
├── static/ (optional)
├── views.py
├── urls.py
├── diabetes.csv
└── manage.py

````

## 🖥️ Screenshots

*(You can add a screenshot here of your web app interface)*

## 🧠 Machine Learning Model

- Model: **Logistic Regression**
- Dataset: [`diabetes.csv`](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- Scaled using: `StandardScaler`
- Evaluation: Trained on 80% of the dataset with test accuracy measured via `accuracy_score`

## 📝 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/diabetes-prediction-django.git
   cd diabetes-prediction-django
````

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Visit `http://127.0.0.1:8000` in your browser.

## 📦 Requirements

* Python 3.8+
* Django 4.0+
* pandas
* scikit-learn

## 📌 Note

Make sure to place the `diabetes.csv` file inside your project directory where `views.py` can access it.

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

**Created by [Shubham Sharma](www.linkedin.com/in/shubham-sharma611)**
Let’s connect and build together! 🤝

```
