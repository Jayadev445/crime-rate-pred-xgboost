from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model
with open('xgboost_model.pkl', 'rb') as f:
    model = pickle.load(f)
#filename='model.pkl'
#model=pickle.load(open(filename, 'rb'))


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    year = int(request.form['Year'])
    month = int(request.form['Month'])
    primary_type = int(request.form['Primary Type'])
    place = float(request.form['place'])
    district = float(request.form['District'])
    community_area = int(request.form['Community Area'])
    
    # Create an input array for prediction
    input_features = np.array([[year, month, primary_type, place, district, community_area]])
    
    # Predict using the loaded model
    prediction = model.predict(input_features)
    
    # Render the prediction result
    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)