# Crime Rate Prediction using XGBoost

Crime Rate Prediction Using XGBoost, comparing XGBoost based on accuracy with different models like KNN, decision trees and SVM models.

## Project Summary

This project aims to predict the likelihood of criminal incidents based on historical crime data using the **XGBoost** machine learning algorithm. By analyzing attributes such as time, location, and type of crime, the model forecasts crime occurrence rates, which can assist city planners, law enforcement, and public policy researchers in proactive crime prevention and resource allocation.

The project also includes a **Flask-based web application** that allows users to input features like year, month, type of crime, district, and area to receive real-time crime rate predictions.

---

## Objectives

- Clean and preprocess crime dataset for modeling.
- Train an **XGBoost Regressor** to predict crime rate or frequency.
- Evaluate the model using standard regression metrics.
- Deploy the model using a simple Flask web interface for interactive use.

---

## Tools & Technologies

- **Programming Language**: Python
- **Libraries Used**:
  - `XGBoost` – Machine learning model
  - `pandas`, `numpy` – Data manipulation
  - `Flask` – Web framework for model deployment
  - `pickle` – Model serialization
  - `scikit-learn` – Data preprocessing and evaluation
- **Frontend**: HTML (via `index.html` and `result.html` templates)
- **Deployment**: Localhost via Flask server

---

## Project Structure

├── CrimePredXGB.ipynb # Jupyter notebook for data analysis and model training
├── app.py # Flask application backend
├── xgboost_model.pkl # Trained and serialized XGBoost model
├── templates/
│ ├── index.html # Form input UI
│ └── result.html # Prediction result page
└── README.md # Project documentation

## How to run the app

### 1. Install Dependencies
```bash
pip install flask xgboost scikit-learn numpy pandas
```
### 2. Run the Flask app
```bash
python app.py
```
### 3. Open in browser

Once the Flask server is running, open your web browser and go to:

http://127.0.0.1:5000/


You’ll see the home page with a form. Fill in the required crime-related features and submit the form to receive a predicted crime rate based on the trained XGBoost model.

---

### Future Enhancements

Here are some potential improvements for this project:

-  Add dropdown menus with labeled options for categorical inputs (e.g., crime type).
-  Integrate real-time dashboards using Plotly, Dash, or Streamlit.
-  Visualize crime rates on an interactive map using geographic coordinates.
-  Upgrade the model with deep learning (e.g., LSTM for time-series trends).
-  Deploy the app on cloud platforms (Heroku, AWS, or Render).
-  Connect to real-world crime databases for live predictions.
-  Include authentication and admin panels for secure usage.
