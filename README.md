
---

# 🌐 GCP Multi-Language Document Translator

An enterprise-grade document translation tool built with **Streamlit** and **Google Cloud Translation AI (v3)**. This application allows users to upload structured documents, automatically detect source languages with confidence scores, and translate them into multiple target languages simultaneously while preserving original layouts.

## ✨ Features

* **Automatic Language Detection:** Identifies the source language and provides a percentage-based confidence score.
* **Layout Preservation:** Supports `PDF`, `DOCX`, `PPTX`, and `XLSX`, keeping fonts, images, and tables in place.
* **Multi-Language Processing:** Translate a single document into several target languages in one workflow.
* **Real-time Preview:** Integrated PDF viewer to see results instantly without leaving the browser.
* **Security-First Auth:** Uses **Application Default Credentials (ADC)**—no service account keys required.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Backend API:** [Google Cloud Translation AI (v3)](https://www.google.com/search?q=https://cloud.google.com/translate/docs/advanced/translating-documents-v3)
* **Auth Strategy:** Google Application Default Credentials (ADC)
* **Environment:** Python 3.9+

---

## 🚀 Getting Started

### 1. Prerequisites

* A **Google Cloud Project** with billing enabled.
* Enable the Translation API:
```bash
gcloud services enable translate.googleapis.com

```



### 2. Authentication (ADC)

This project uses **Application Default Credentials**. Follow these steps based on your environment:

**Local Development:**
Ensure you have the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install) installed, then run:

```bash
gcloud auth application-default login

```

*This allows the application to securely use your own Google identity to access the Translation API.*

**Production (Cloud Run / GCE):**
Assign a Service Account with the `Cloud Translation User` role directly to the resource. No environment variables are needed.

### 3. Installation

```bash
git clone https://github.com/your-username/gcp-translator-app.git
cd gcp-translator-app

```

### 4. Configuration

Update the following variables in the `app.py` script:

* `PROJECT_ID`: Your unique GCP Project ID.
* `LOCATION`: Typically `global`.

### 5. Run the App

```bash
streamlit run app.py

```

---

## 📊 How it Works

1. **Identity Handshake:** The Google Client Library searches for credentials via ADC (local user login or attached service account).
2. **Detection Snippet:** To provide a **Confidence Score**, the app sends a 500-character snippet to the detection engine first.
3. **Advanced Translation:** The full document is sent to the `translate_document` endpoint. GCP handles the parsing of complex file layers.
4. **Base64 Encoding:** Translated bytes are encoded and rendered via an `iframe` for immediate browser preview.

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

By utilizing **ADC**, this app adheres to the principle of least privilege. It does **not** store documents or static keys. All processing occurs in-memory, and data is transmitted via encrypted TLS directly to Google Cloud's secure endpoints.

---

