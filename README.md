# 🧠 PersonaBot – Human Persona AI Platform

A real-time AI platform where alumni and professionals can create their own AI chatbot representing their knowledge, experience, and personality. Other users can interact with these bots via text or live voice mode.

## ✨ Features

- **Multi-Bot Creation** – Each user creates their own AI persona
- **Document Upload** – PDF, DOCX, Image (with OCR)
- **RAG Pipeline** – Chunking, embeddings, pgvector similarity search
- **Streaming Chat** – Real-time LLM responses via SSE
- **Live Voice Mode** – WebRTC + ElevenLabs TTS
- **Multi-Tenant** – Full data isolation per bot (`WHERE bot_id = ?`)
- **Cloud-Ready** – Docker + Nginx + Vercel deployment

## 🏗️ Architecture

```
Frontend (Next.js + TypeScript - Vercel)
         |
     Nginx (AWS EC2)
         |
     FastAPI (Docker)
         |
------------------------------
| RAG | Voice | Auth | Chat |
------------------------------
         |
     Supabase + pgvector
         |
   LLM Provider + ElevenLabs
```

## 📁 Project Structure

```
persona_ai_capstone/
├── frontend/          # Next.js 14+ App (TypeScript + Tailwind CSS)
│   ├── src/app/       # App Router pages
│   ├── src/           # Components, hooks, services
│   └── public/        # Static assets
│
├── backend/           # FastAPI Backend (Python)
│   ├── api/           # Routes, schemas, middleware
│   ├── core/          # Config, security, utils
│   ├── database/      # Models, queries, RLS
│   ├── rag/           # Ingestion, chunking, embeddings, retrieval
│   ├── voice/         # STT, TTS, WebRTC, streaming
│   └── workers/       # Background processing
│
├── nginx/             # Nginx reverse proxy config
├── docker-compose.yml # Docker services
├── Dockerfile         # Backend container
└── .env.example       # Environment template
```

## 🚀 Quick Start

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn api.main:app --reload --port 8000
```

### Docker
```bash
docker-compose up --build
```

## 🔧 Environment Setup

1. Copy `.env.example` to `.env`
2. Fill in your Supabase, OpenAI, and ElevenLabs credentials
3. Run the development servers

## 📅 Implementation Timeline

| Month | Focus |
|-------|-------|
| 1 | Foundation & Setup |
| 2 | RAG Core Pipeline |
| 3 | Chat Mode (Streaming) |
| 4 | Live Voice Mode |
| 5 | Production & Testing |

## 📄 License

MIT
