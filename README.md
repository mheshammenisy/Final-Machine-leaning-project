## 🧠 Personality Prediction Web App
This project is a machine learning-based web app that predicts whether a person is an Introvert or Extrovert based on behavioral traits. It was created as part of the Epsilon AI Academy program and is deployed using Streamlit Cloud.

## 🔗 Live Demo:
👉 Try the App

## 📌 Project Overview
The project follows a complete machine learning pipeline:

Data preprocessing & cleaning

Exploratory Data Analysis (EDA)

Model training using RandomForestClassifier

Streamlit deployment for user interaction

The training and prediction are based on a dataset containing user behavioral traits.

## 🧰 Technologies Used
Tool	Purpose
Python 3.x	Programming language
Pandas	Data manipulation
Scikit-learn	Model building
Joblib	Model serialization
Streamlit	Web app interface
Jupyter Notebook	Data exploration and training

## 📊 Features Used for Prediction
The model uses the following 7 behavioral features:

Time_spent_Alone

Stage_fear

Drained_after_socializing

Social_event_attendance

Going_outside

Friends_circle_size

Post_frequency

These features are collected via dropdowns in the app, allowing users to test how their behavior maps to personality.

## 🧠 Model Training
The model was trained in a Jupyter Notebook:
📄 Extrover_introvertproject.ipynb

Data cleaning and encoding

Feature selection

RandomForestClassifier training

Model saved as personality11_model.pkl

Feature list saved as features11.pkl

## 🌐 Streamlit Web App
The app is built with Streamlit and provides an interactive interface for personality prediction.

## 📄 steamfinalapp.py handles:

UI input for 7 features

Loading the model and feature list

Making predictions

Displaying results with friendly feedback

## 🔗 Main Repository Source
This project is part of the Epsilon AI Final Machine Learning Project
🔗 Main Epsilon AI GitHub Repository

