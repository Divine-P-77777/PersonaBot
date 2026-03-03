-- Row Level Security (RLS) Policies for Supabase
-- Ensures multi-tenant data isolation

-- Enable RLS on all tables
ALTER TABLE bots ENABLE ROW LEVEL SECURITY;
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE document_chunks ENABLE ROW LEVEL SECURITY;
ALTER TABLE document_embeddings ENABLE ROW LEVEL SECURITY;

-- Bots: owners can CRUD their own bots, everyone can read
CREATE POLICY "Users can read all bots" ON bots
    FOR SELECT USING (true);

CREATE POLICY "Users can manage own bots" ON bots
    FOR ALL USING (auth.uid()::text = owner_id);

-- Documents: only bot owners can manage, read via bot access
CREATE POLICY "Bot owners can manage documents" ON documents
    FOR ALL USING (
        bot_id IN (SELECT id FROM bots WHERE owner_id = auth.uid()::text)
    );

CREATE POLICY "Anyone can read documents" ON documents
    FOR SELECT USING (true);

-- Chunks: same as documents
CREATE POLICY "Bot owners can manage chunks" ON document_chunks
    FOR ALL USING (
        bot_id IN (SELECT id FROM bots WHERE owner_id = auth.uid()::text)
    );

CREATE POLICY "Anyone can read chunks" ON document_chunks
    FOR SELECT USING (true);

-- Embeddings: same as documents
CREATE POLICY "Bot owners can manage embeddings" ON document_embeddings
    FOR ALL USING (
        bot_id IN (SELECT id FROM bots WHERE owner_id = auth.uid()::text)
    );

CREATE POLICY "Anyone can read embeddings" ON document_embeddings
    FOR SELECT USING (true);
