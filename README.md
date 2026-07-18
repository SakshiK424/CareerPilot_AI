# 🚀 CareerPilot AI – Multi-Agent Career Guidance Platform

An AI-powered Career Guidance Platform that helps students make informed career decisions through resume analysis, skill gap identification, market insights, and personalized career roadmaps using **LangGraph**, **LangChain**, and **Groq Llama 3.3**.

---

## 📌 Problem Statement

Many students struggle to choose the right career path, identify missing skills, and understand current industry trends. They often spend hours searching different websites for guidance.

CareerPilot AI solves this problem by providing personalized AI-powered career recommendations in one place.

---

## ✨ Features

- 📄 AI Resume Analysis
- 🎯 Skill Gap Analysis
- 📈 Market Trend Analysis
- 🗺️ Personalized Career Roadmap
- 🤖 AI Career Advisor (LangGraph Multi-Agent System)
- 💬 AI Career Chatbot
- 📊 Interactive Dashboard
- 📥 Download Career Report as PDF

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI Framework
- LangChain
- LangGraph

### Large Language Model
- Groq API
- Llama 3.3 70B Versatile

### Database
- SQLite

### Libraries
- PyMuPDF
- Plotly
- ReportLab
- Pandas
- Python-dotenv

---

## 📂 Project Structure

```text
career-guidance-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── pages/
├── agents/
├── services/
├── models/
├── database/
├── assets/
├── uploads/
├── reports/
└── utils/
```

---

## 🔄 Workflow

```text
User Uploads Resume
          │
          ▼
Resume Text Extraction
          │
          ▼
LangGraph Multi-Agent Workflow
          │
 ┌─────────────────────────┐
 │ Resume Agent            │
 │ Market Analysis Agent   │
 │ Roadmap Agent           │
 └─────────────────────────┘
          │
          ▼
Career Report Generation
          │
          ▼
Download PDF Report
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/SakshiK424/CareerPilot_AI
```

### Move into the project folder

```bash
cd careerguidance
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

### Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots
![homepage
](image.png)

Add screenshots here after deployment.

- Home Page
- Resume Analysis
- Skill Gap Analysis
- Market Analysis
- Career Roadmap
- AI Career Advisor
- PDF Report

---

## 📈 Future Enhancements

- User Authentication
- Resume Score Prediction
- Job Recommendation Engine
- Course Recommendation System
- Real-time Job Market APIs
- Multi-language Support
- Cloud Database Integration

---

## 👨‍💻 Authors

**Sakshi**  **Rohit**   **Mohit**

B.Tech Computer Engineering (Data Science)

J.C. Bose University of Science & Technology, YMCA

---

## ⭐ If you like this project, consider giving it a star!
