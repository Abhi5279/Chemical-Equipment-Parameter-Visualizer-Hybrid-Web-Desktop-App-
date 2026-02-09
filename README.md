🧪 Chemical Equipment Parameter Visualizer

Hybrid Web + Desktop Analytics Application

A hybrid analytics application that enables users to upload chemical equipment datasets (CSV), perform rule-based risk analysis, compute a health score, and visualize insights through both Web and Desktop interfaces using a shared backend API.

🎥 Demo Video

📎 https://drive.google.com/file/d/1EQ5kUmkZQyyFxJGrKAOPXUDqlslFUnUq/view?usp=drive_link

📌 Overview

Single Django REST API backend

Web frontend built with React

Desktop application built with PyQt5

Deterministic and explainable analytics (no black-box ML)

Consistent results across web and desktop platforms

🏗 Tech Stack

Backend

Python, Django, Django REST Framework

Pandas, SQLite

ReportLab (PDF generation)

Web Frontend

React (Vite), Tailwind CSS

Chart.js, Axios

Desktop Frontend

PyQt5, Matplotlib

Requests

✨ Features

CSV upload & validation

Rule-based equipment risk classification

Dataset health score calculation

Interactive dashboards and charts

Upload history (last 5 datasets)

PDF report generation

Token-based authentication

Shared backend for web & desktop clients

📊 Risk Analysis Logic (Explainable)

Each equipment is evaluated using predefined safety thresholds.

Inputs

Flowrate

Pressure

Temperature

(Optional) Equipment Type

Logic

IF pressure > safe_limit
OR temperature > safe_limit
OR flowrate outside safe range
→ HIGH RISK
ELSE → NORMAL


Dataset Summary Example

{
  "high_risk": 6,
  "normal": 9
}

🧮 Health Score Calculation

The health score represents overall dataset condition.

health_score = (normal_equipment / total_equipment) × 100


Example

Total equipment: 15

Normal: 9

Health Score = 60

▶️ Running the Project
Backend
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Backend URL: http://127.0.0.1:8000

Web App
cd frontend-web
npm install
npm run dev


Web URL: http://localhost:5173

Desktop App
cd frontend-desktop
pip install -r requirements.txt
python main.py

📂 Project Structure
chemical-equipment-visualizer/
├── backend/
├── frontend-web/
├── frontend-desktop/
└── README.md

🚀 Notes

Designed for safety-critical analytics

Logic is fully explainable and auditable

Architecture supports future ML integration

📌 License

For academic and demonstration purposes.
