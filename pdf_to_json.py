import docx
import pdfplumber
import csv
import json
from openpyxl import Workbook
import os

def pdf_parser(file_path):
    text_content=[]
    with pdfplumber.open(file_path) as pdf:
        for i,page in enumerate(pdf.pages):
            text=page.extract_text()
            if text:
                text_content.append({
                    "page_number":i+1,
                    "content":text,
                    "source":os.path.basename(file_path)
                })
    return text_content

with open("output.json","w",encoding="utf-8")as f:
    json.dump(pdf_parser(r"C:\Users\ASUS\Desktop\Data_Science\RAG\a_pdf_document.pdf"),f,ensure_ascii=False,indent=4)

with open("output.csv","w",newline="\n",encoding="utf-8")as f:
    writer=csv.DictWriter(f,fieldnames=["page number","content","source"])
    writer.writeheader()
    writer.writerows(pdf_parser(r"C:\Users\ASUS\Desktop\Data_Science\RAG\a_pdf_document.pdf"))

data=pdf_parser(r"C:\Users\ASUS\Desktop\Data_Science\RAG\a_pdf_document.pdf")
path="output.xlsx"
wb=Workbook()
ws=wb.active
ws.title="output"
ws.append(["page_number","content","source"])
for row in data:
    ws.append([row["page_number"],row["content"],row["source"]])
wb.save(path)
