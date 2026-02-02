
---

# 🌐 GCP Multi-Language Document Translator

An enterprise-grade document translation tool built with **Streamlit** and **Google Cloud Translation AI (v3)**. This application allows users to upload structured documents, automatically detect source languages with confidence scores, and translate them into multiple target languages simultaneously while preserving the original layout.

## ✨ Features

* **Automatic Language Detection:** Identifies the source language and provides a percentage-based confidence score.
* **Layout Preservation:** Supports `PDF`, `DOCX`, `PPTX`, and `XLSX`, keeping fonts, images, and tables in place.
* **Multi-Language Processing:** Translate a single document into several target languages in one workflow.
* **Real-time Preview:** Integrated PDF viewer to see results instantly without leaving the browser.
* **Processing Metrics:** Displays exact API processing time and metadata for every translation.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Backend API:** [Google Cloud Translation AI (v3)](https://www.google.com/search?q=https://cloud.google.com/translate/docs/advanced/translating-documents-v3)
* **Environment:** Python 3.9+

---

## 🚀 Getting Started

### 1. Prerequisites

* A **Google Cloud Project** with billing enabled.
* Enable the Translation API:
```bash
gcloud services enable translate.googleapis.com

```


* A **Service Account Key** (JSON) with the `Cloud Translation User` role.

### 2. Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/your-username/gcp-translator-app.git
cd gcp-translator-app
pip install -r requirements.txt

```

### 3. Environment Setup

Set your Google Cloud credentials in your terminal session:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-file.json"

```

### 4. Configuration

Update the following variables in the `app.py` script:

* `PROJECT_ID`: Your unique GCP Project ID.
* `LOCATION`: Typically `us-central1` or `global`.

### 5. Run the App

```bash
streamlit run app.py

```

---

## 📊 How it Works

1. **File Parsing:** The app reads the raw bytes of the uploaded file.
2. **Detection Snippet:** To provide a **Confidence Score**, the app sends a 500-character snippet to the detection engine first.
3. **Advanced Translation:** The full document is sent to the `translate_document` endpoint. GCP handles the parsing of the file structure (like PDF layers).
4. **Base64 Encoding:** For live previews, the translated bytes are encoded to Base64 and rendered via an `iframe`.

---

## 📝 Supported Formats

| Format | Extension | Preview Support |
| --- | --- | --- |
| **Portable Document** | `.pdf` | ✅ Yes |
| **Word Document** | `.docx` | 📥 Download Only |
| **PowerPoint** | `.pptx` | 📥 Download Only |
| **Excel Sheet** | `.xlsx` | 📥 Download Only |

---

## 🔒 Security & Privacy

This application does **not** store your documents. Files are processed in-memory and sent via encrypted TLS to Google Cloud. After the session is closed or the page is refreshed, the data is cleared from the Streamlit server memory.

---

