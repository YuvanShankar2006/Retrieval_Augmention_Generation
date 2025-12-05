import json
import uuid
import re
from langchain_text_splitters import RecursiveCharacterTextSplitter

def clean_text(text):
    text = re.sub(r"'", "", text)
    text = re.sub(r'\n\s*\d+\s*\n', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ". ", " ", ""],
    length_function=len,
    is_separator_regex=False
)
try:
    with open('output.json', 'r', encoding="utf-8") as f:
        raw_data = json.load(f)
except FileNotFoundError:
    print("Error: 'output.json' file not found.")
    raw_data = []

chunked_dataset = []

# 4. Process
for page in raw_data:
    # A. Clean the text first to avoid splitting on garbage
    clean_content = clean_text(page.get('content', ''))
    
    # B. Use LangChain to split
    # create_documents expects a list of texts; we pass a list of one text
    docs = splitter.create_documents([clean_content])
    
    # C. Format for your JSON output
    for doc in docs:
        chunked_dataset.append({
            "id": str(uuid.uuid4()),
            "text": doc.page_content,
            "metadata": {
                # Merge existing page metadata with any new metadata
                "page": page.get('page number', 'unknown'),
                "source": page.get('source', 'unknown'),
                # LangChain can handle document-level metadata if needed later
            }
        })

print(f"Successfully created {len(chunked_dataset)} high-quality chunks.")

# 5. Save
with open('chunks.json', 'w', encoding="utf-8") as f:
    json.dump(chunked_dataset, f, ensure_ascii=False, indent=4)