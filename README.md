# 📞 PDF Click-to-Call Link Adder

A simple web app that lets you upload a PDF and add **clickable links** (like `tel:`, `mailto:`, or `https://`) to specific visible text — built using **Python** and **Streamlit**.

---

## 🚀 Features

- Drag-and-drop PDF uploader
- Add any number of text → link mappings
- Supports phone, email, and web links
- Download updated PDF with clickable zones

---

## 🔧 Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)

---

## 🖥️ How to Run Locally

```bash
git clone https://github.com/yourusername/pdf-click-to-call-app.git
cd pdf-click-to-call-app
pip install -r requirements.txt
streamlit run pdf_link_adder_app.py
