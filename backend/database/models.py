"""
Database models for PersonaBot.
Multi-tenant safe: every table uses bot_id for isolation.
"""
from sqlalchemy import Column, String, Text, DateTime, Integer, JSON, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector

Base = declarative_base()


class Bot(Base):
    """Bot persona table."""

    __tablename__ = "bots"

    id = Column(String, primary_key=True)
    owner_id = Column(String, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    persona_config = Column(JSON, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    documents = relationship("Document", back_populates="bot", cascade="all, delete-orphan")


class Document(Base):
    """Uploaded documents table."""

    __tablename__ = "documents"

    id = Column(String, primary_key=True)
    bot_id = Column(String, ForeignKey("bots.id"), nullable=False, index=True)
    file_name = Column(String(500), nullable=False)
    file_type = Column(String(50))
    file_size = Column(Integer)
    storage_path = Column(Text)
    metadata = Column(JSON, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    bot = relationship("Bot", back_populates="documents")
    chunks = relationship("DocumentChunk", back_populates="document", cascade="all, delete-orphan")


class DocumentChunk(Base):
    """Document chunks table."""

    __tablename__ = "document_chunks"

    id = Column(String, primary_key=True)
    document_id = Column(String, ForeignKey("documents.id"), nullable=False, index=True)
    bot_id = Column(String, nullable=False, index=True)
    chunk_index = Column(Integer, nullable=False)
    chunk_text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    document = relationship("Document", back_populates="chunks")
    embedding = relationship("DocumentEmbedding", back_populates="chunk", uselist=False, cascade="all, delete-orphan")


class DocumentEmbedding(Base):
    """Document embeddings table (pgvector)."""

    __tablename__ = "document_embeddings"

    id = Column(String, primary_key=True)
    chunk_id = Column(String, ForeignKey("document_chunks.id"), nullable=False, unique=True)
    bot_id = Column(String, nullable=False, index=True)
    embedding = Column(Vector(1536))  # OpenAI text-embedding-3-small dimension
    model_name = Column(String(100), default="text-embedding-3-small")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    chunk = relationship("DocumentChunk", back_populates="embedding")
