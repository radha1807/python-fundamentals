from pathlib import Path

docs = Path ('documents')
docs.mkdir(exist_ok = True)

(docs /'intro.txt').write_text(
    'RAG stands for retrieval augmented generation.',   encoding='utf-8')
(docs / 'chunking.txt').write_text(
    'Chunking splits documents into pieces. Chunk size affects retrieval quality.',
    encoding='utf-8'
)

def chunk_text(text):
    chunks = [s.strip() for s in text.split('.') if s.strip()]
    return chunks

print('processing all documents:\n')

for file_path in Path ('documents').rglob('*.txt'):
    content = file_path.read_text(encoding='utf-8')
    chunks = chunk_text(content)
    
    print(f"File : {file_path.name}")
    print(f"Chunks: {len(chunks)}")
    for i, chunk in enumerate(chunks, 1):
        print(f"  [{i}] {chunk}")
    print()
    

    