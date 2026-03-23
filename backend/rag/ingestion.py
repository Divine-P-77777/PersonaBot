import io
import fitz  # PyMuPDF
import easyocr
import numpy as np
from PIL import Image
from backend.rag.chunking import chunk_text
from backend.rag.embeddings import get_embeddings
from backend.database.connection import get_supabase_client

# Initialize EasyOCR reader (singleton-ish)
_ocr_reader = None


def get_ocr_reader():
    """Get or create EasyOCR reader instance."""
    global _ocr_reader
    if _ocr_reader is None:
        _ocr_reader = easyocr.Reader(['en'])
    return _ocr_reader


def pdf_to_ocr_text(file_content: bytes) -> str:
    """Extract text from PDF using OCR page-by-page."""
    doc = fitz.open(stream=file_content, filetype="pdf")
    reader = get_ocr_reader()
    full_text = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        # Increase resolution for better OCR
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        img_data = pix.tobytes("ppm")
        img = Image.open(io.BytesIO(img_data))

        # Convert PIL image to numpy array for EasyOCR
        img_np = np.array(img)
        ocr_result = reader.readtext(img_np, detail=0, paragraph=True)
        page_text = " ".join(ocr_result)
        full_text.append(page_text)

    doc.close()
    return "\n\n".join(full_text)


async def ingest_document(bot_id: str, file_name: str, file_content: bytes):
    """Orchestrate the full document ingestion pipeline."""
    # 1. OCR Extract
    text = pdf_to_ocr_text(file_content)

    # 2. Chunk
    chunks = chunk_text(text)

    # 3. Embed
    embeddings_manager = get_embeddings()
    embeddings = embeddings_manager.embed_documents(chunks)

    # 4. Store in Supabase
    supabase = get_supabase_client()

    records = []
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        records.append({
            "bot_id": bot_id,
            "content": chunk,
            "embedding": embedding,
            "metadata": {
                "source": file_name,
                "chunk_index": i
            }
        })

    # Batch insert into document_chunks
    result = supabase.table("document_chunks").insert(records).execute()
    return len(chunks)
