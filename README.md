flowchart LR
%% Client Layer
User[👤 User / Recruiter<br/>Browser / Swagger UI]

    %% API Layer
    subgraph API["FastAPI Backend (Docker Container)"]
        Auth[🔐 JWT Authentication]
        ResumeAPI[📄 Resume Upload API]
        JobAPI[🧾 Job Description API]
        RankAPI[📊 Ranking & Matching API]
    end

    %% NLP Layer
    subgraph NLP["AI / NLP Processing"]
        Parser[📑 PDF & DOCX Parser]
        NLPProc[🧠 spaCy Skill Extraction]
        Embed[🔢 Embedding Generator<br/>(Sentence Transformers)]
        Similarity[📐 Cosine Similarity Engine]
    end

    %% Database Layer
    subgraph DB["PostgreSQL Database (Docker Container)"]
        Users[(Users)]
        Resumes[(Resumes)]
        Jobs[(Jobs)]
        Embeddings[(Embeddings)]
        Scores[(Match Scores)]
    end

    %% Flow
    User -->|HTTP Requests| Auth
    Auth --> ResumeAPI
    Auth --> JobAPI
    Auth --> RankAPI

    ResumeAPI --> Parser
    Parser --> NLPProc
    NLPProc --> Embed
    Embed --> Embeddings

    JobAPI --> Embed

    RankAPI --> Similarity
    Similarity --> Scores

    %% DB Connections
    Auth --> Users
    ResumeAPI --> Resumes
    JobAPI --> Jobs
    Embed --> Embeddings
    RankAPI --> Scores

    %% Deployment
    subgraph Deployment["Deployment Environment"]
        Docker[🐳 Docker & Docker Compose]
        Cloud[☁️ Azure / AWS]
    end

    API --> Docker
    DB --> Docker
    Docker --> Cloud
