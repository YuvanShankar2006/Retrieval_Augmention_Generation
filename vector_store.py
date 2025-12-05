import json
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

with open("chunks.json","r",encoding="utf-8") as f:
    chunks_data=json.load(f)

documents=[]
for item in chunks_data:
    doc=Document(
        page_content=item['text'],
        metadata=item['metadata']
    )
    documents.append(doc)
print("Intializing model.....")
model=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore=Chroma.from_documents(
    documents=documents,
    embedding=model,
    persist_directory="./chroma_db"

)
print(f"Success! Indexed {len(documents)} chunks into './chroma_db'.")