import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama
from langchain_classic.chains import load_summarize_chain

# 1. Setup the Model
def load_llm():
    return ChatOllama(
        model="llama3.2",
        temperature=0
    )

# 2. The PDF Processing Pipeline
def process_pdf(file_path):
    print(f"Loading PDF from: {file_path}")
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000, 
        chunk_overlap=200
    )
    split_docs = text_splitter.split_documents(docs)
    print(f"Split into {len(split_docs)} chunks.")

    llm = load_llm()
    
    chain = load_summarize_chain(
        llm, 
        chain_type="map_reduce",
        verbose=True
    )
    
    output = chain.invoke(split_docs)
    return output['output_text']


if __name__ == "__main__":
    try:
        if not os.path.exists("temp"):
            os.makedirs("temp")
            
        print("Imports are fixed! 'langchain_classic' is working.")
       
    except Exception as e:
        print(f"Error: {e}")