-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Multi-tenant document chunks table
-- Optimized for Nomic V2 (768 dimensions)
CREATE TABLE IF NOT EXISTS document_chunks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    bot_id UUID NOT NULL,
    content TEXT NOT NULL,
    metadata JSONB DEFAULT '{}',
    embedding VECTOR(768),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index for similarity search
CREATE INDEX IF NOT EXISTS document_chunks_embedding_idx ON document_chunks 
USING hnsw (embedding vector_cosine_ops);

-- Multi-tenant filtering index
CREATE INDEX IF NOT EXISTS document_chunks_bot_id_idx ON document_chunks (bot_id);

-- Similarity search function with multi-tenant filtering
CREATE OR REPLACE FUNCTION match_document_chunks(
    query_embedding VECTOR(768),
    match_count INT DEFAULT 5,
    p_bot_id UUID DEFAULT NULL
) RETURNS TABLE (
    id UUID,
    content TEXT,
    metadata JSONB,
    similarity FLOAT
) LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT
        document_chunks.id,
        document_chunks.content,
        document_chunks.metadata,
        1 - (document_chunks.embedding <=> query_embedding) AS similarity
    FROM document_chunks
    WHERE (p_bot_id IS NULL OR document_chunks.bot_id = p_bot_id)
    ORDER BY document_chunks.embedding <=> query_embedding
    LIMIT match_count;
END;
$$;
