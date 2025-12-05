from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

model_id = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=512,
    temperature=0.1
)
llm = HuggingFacePipeline(pipeline=pipe)

# Prompt
prompt = ChatPromptTemplate.from_template("""
Use ONLY the following context to answer the question. 
If you don't know, say "I don't know".

<context>
{context}
</context>

Question: {question}
Answer:
""")

# Build RAG pipeline using Runnable graph
rag_chain = (
    RunnableParallel(
        context=retriever, 
        question=RunnablePassthrough()
    )
    | prompt
    | llm
)

# Interactive loop
print("\n--- RAG Ready ---")
while True:
    q = input("\nQuestion: ")
    if q.lower() == "exit":
        break

    answer = rag_chain.invoke(q)
    print("\nAnswer:", answer)
