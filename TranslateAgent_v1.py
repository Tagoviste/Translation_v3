import streamlit as st
import time
import base64
from google.cloud import translate_v3 as translate

# --- CONFIGURATION ---
PROJECT_ID = "beyioku-1200-20250609123702"
LOCATION = "global"

def translate_document(uploaded_file, target_langs):
    client = translate.TranslationServiceClient()
    parent = f"projects/{PROJECT_ID}/locations/{LOCATION}"
    
    content = uploaded_file.read()
    results = {}

    # 1. Get explicit Confidence Score (via a snippet)
    # The Document API doesn't return a confidence score directly, so we check a sample.
    sample_text = content[:500].decode('utf-8', errors='ignore') if len(content) > 0 else ""
    detection_response = client.detect_language(parent=parent, content=sample_text)
    primary_detection = detection_response.languages[0]
    confidence = primary_detection.confidence
    detected_lang = primary_detection.language_code

    # 2. Translate for each requested language
    for lang in target_langs:
        start_time = time.time()
        response = client.translate_document(
            request={
                "parent": parent,
                "target_language_code": lang,
                "document_input_config": {
                    "content": content,
                    "mime_type": uploaded_file.type,
                },
            }
        )
        duration = time.time() - start_time
        
        results[lang] = {
            "bytes": response.document_translation.byte_stream_outputs[0],
            "time": duration,
            "detected": detected_lang,
            "confidence": confidence
        }
        
    return results

# --- UI SETUP ---
st.set_page_config(layout="wide", page_title="GCP Document Translator")
st.title("📂 Multi-Language Document Translator")

# Language Selection
available_langs = {"Spanish": "es", "French": "fr", "German": "de", "Chinese": "zh", "Japanese": "ja","Arabic": "ar","Albanian": "sq","Russian": "ru","English (United Kingdom)": "en-GB"}
selected_names = st.multiselect("Select Target Languages", list(available_langs.keys()), default=["Spanish"])
target_codes = [available_langs[name] for name in selected_names]

uploaded_file = st.file_uploader("Upload Document (PDF, DOCX, PPTX)", type=["pdf", "docx", "pptx"])

if uploaded_file and st.button("Translate All"):
    all_results = translate_document(uploaded_file, target_codes)
    
    for lang_code, data in all_results.items():
        st.divider()
        st.subheader(f"Results for: {lang_code.upper()}")
        
        # Metrics Row
        m1, m2, m3 = st.columns(3)
        m1.metric("Detected Language", data['detected'].upper())
        m2.metric("Confidence Score", f"{data['confidence']:.2%}")
        m3.metric("Processing Time", f"{data['time']:.2f}s")

        # Result Display & Download
        col_preview, col_down = st.columns([3, 1])
        
        with col_preview:
            # Display PDF Preview (works best for PDF)
            if uploaded_file.type == "application/pdf":
                base64_pdf = base64.b64encode(data['bytes']).decode('utf-8')
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
            else:
                st.info(f"Preview not available for {uploaded_file.type}. Please download to view.")

        with col_down:
            st.download_button(
                label=f"📥 Download {lang_code.upper()}",
                data=data['bytes'],
                file_name=f"{lang_code}_{uploaded_file.name}",
                mime=uploaded_file.type,
                key=f"btn_{lang_code}"
            )
