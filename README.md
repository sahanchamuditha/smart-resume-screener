# 🚀 Smart Resume Screener – AI-Powered Resume Screening Platform

An end-to-end **AI-driven Resume Screening System** designed to automatically analyze, score, and rank resumes against job descriptions.  
This project demonstrates **real-world backend engineering, containerization, authentication, and AI integration** following production-ready practices.

---

## 📌 Project Overview

Recruiters often spend significant time manually screening resumes.  
The **Smart Resume Screener** automates this process by:

- Parsing resumes (PDF/DOCX)
- Extracting structured candidate data
- Matching resumes against job descriptions using AI
- Providing relevance scores for faster decision-making

🎯 **Objective:**  
Build a scalable, secure, and containerized backend system that mimics how modern AI-powered recruitment platforms work.

---

## 🏗️ System Architecture

The system follows a **containerized microservice-style backend architecture**:

- Client interacts with REST APIs
- Authentication handled using JWT
- Resume processing and AI scoring handled asynchronously
- PostgreSQL used for persistent storage
- Docker used for environment consistency


---

## 🛠️ Technologies Used

### 🔹 Backend
- **Python (FastAPI)** – High-performance REST API framework
- **JWT Authentication** – Secure stateless authentication
- **Pydantic** – Data validation and schema enforcement
- **Uvicorn** – ASGI server for FastAPI

### 🔹 Database
- **PostgreSQL** – Relational database for resumes, users, and metadata
- **SQLAlchemy** – ORM for database interaction
- **Alembic** – Database migrations

### 🔹 AI & Processing
- **Natural Language Processing (NLP)** – Resume & JD text analysis
- **Vector-based similarity scoring** – Resume relevance calculation
- **Text extraction pipelines** – Resume parsing logic

### 🔹 DevOps & Infrastructure
- **Docker** – Containerized application services
- **Docker Compose** – Multi-container orchestration
- **Git & GitHub** – Version control and collaboration
- **Environment-based configuration** – Secure secrets handling

---

## 🔐 Authentication & Security

- Stateless **JWT-based authentication**
- Secure password hashing
- Token validation middleware
- Role-ready architecture for future RBAC implementation

---

## 🔄 How the Application Works

1. **User Authentication**
   - User registers/logs in
   - JWT token issued for API access

2. **Resume Upload**
   - User uploads resume (PDF/DOCX)
   - File is parsed and stored securely

3. **Text Extraction & Processing**
   - Resume content extracted
   - Cleaned and structured data generated

4. **AI-Based Matching**
   - Resume text compared with Job Description
   - Similarity score calculated using NLP techniques

5. **Scoring & Ranking**
   - Resumes ranked based on relevance score
   - Data stored in PostgreSQL for retrieval

6. **API Response**
   - Recruiter receives structured scoring results via REST API

---

## 🚀 Advanced Concepts & Engineering Practices

- ✅ Containerized backend using Docker
- ✅ Production-style project structure
- ✅ JWT-based stateless authentication
- ✅ Clean separation of concerns (API, services, models)
- ✅ Database migrations with Alembic
- ✅ Environment-specific configurations
- ✅ AI/NLP-driven decision logic
- ✅ Scalable and cloud-ready design

---

## 📂 Project Structure (High Level)

```text
smart-resume-screener/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── services/
│   ├── auth/
│   └── main.py
├── migrations/
├── tests/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```
---

## 🧪 Testing & Validation

- API endpoint testing
- Database connectivity validation
- Container health checks
- Authentication flow testing

---

## 📦 Deployment Ready

This project is **fully containerized** and can be deployed on:

- Cloud virtual machines
- Kubernetes clusters
- CI/CD pipelines
- Any Docker-supported platform

---

## 🌟 Key Takeaways

- Designed like a **real-world backend system**
- Focused on **scalability, security, and maintainability**
- Combines **AI + Backend + DevOps** concepts in one project
- Ideal for demonstrating **production-level engineering skills**

---

## 🤝 Contributions & Feedback

Feedback, suggestions, and improvements are always welcome.  
Feel free to fork the repository and experiment further.

---

### ⭐ If you found this project useful, consider giving it a star!
