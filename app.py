import streamlit as st
import os
from pipeline import process_pdf  

# 1. Page Configuration
st.set_page_config(page_title="Local PDF Summarizer", page_icon="🤖")

# 2. The Title and Description
st.title("Local PDF Summarizer")
st.markdown("Powered by Llama 3.2")
st.write("Upload a PDF to get a concise summary")

# 3. File Uploader Widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# 4. The Logic
if uploaded_file is not None:
    st.info(f"File '{uploaded_file.name}' uploaded successfully.")
    
    temp_path = os.path.join("temp", uploaded_file.name)
    
    if not os.path.exists("temp"):
        os.makedirs("temp")
        
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    if st.button("Summarize Document"):
        
        with st.spinner("Thinking... (This may take a moment based on your GPU)"):
            try:
                summary = process_pdf(temp_path)
                
          
                st.success("Summarization Complete!")
                st.markdown("Summary:")
                st.write(summary)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
            
            finally:
                
                if os.path.exists(temp_path):
                    os.remove(temp_path)

st.markdown("---")
st.caption("Running locally on NVIDIA RTX 3050 | 4GB VRAM Optimized")