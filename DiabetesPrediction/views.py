from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    # Get all input values
    fields = ['pregnancies', 'glucose', 'bloodPressure', 'skinThickness', 'insulin', 'bmi', 'dpf', 'age']
    input_data = []

    for field in fields:
        value = request.GET.get(field)
        if value is None or value.strip() == '':
            return render(request, 'predict.html', {'result2': 'Please fill all the fields!'})

        try:
            input_data.append(float(value))
        except ValueError:
            return render(request, 'predict.html', {'result2': f"Invalid input for {field}. Please enter a number."})

    # Load and preprocess data
    df = pd.read_csv('/home/shubham-sharma/Downloads/Diabetes_Prediction/diabetes.csv')
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)

    # Scale user input
    input_scaled = scaler.transform([input_data])

    # Predict
    pred = model.predict(input_scaled)
    result1 = "Positive" if pred[0] == 1 else "Negative"

    return render(request, 'predict.html', {'result2': result1})
