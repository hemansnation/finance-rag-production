import pytest

from rag_pipeline import load_and_chunk_pdf

def test_chunking():
    chunks = load_and_chunk_pdf('data/sample_10k.pdf')
    
    assert len(chunks) > 0
    assert all(isinstance(chunk.page_content, str) for chunk in chunks)