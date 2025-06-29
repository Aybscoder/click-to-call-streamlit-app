
import streamlit as st
import fitz  # PyMuPDF
import tempfile
import os

st.set_page_config(page_title="Click-to-Call PDF Tool", layout="centered")
st.title("📞 PDF Click-to-Call Link Adder")

st.markdown("Upload a PDF and map visible text to a clickable link (phone, email, web).")

uploaded_pdf = st.file_uploader("📄 Upload PDF", type=["pdf"])
link_entries = []

if uploaded_pdf:
    # Allow dynamic entry of link mappings
    st.subheader("🔗 Add Link Mappings")
    num_links = st.number_input("How many text+link pairs?", min_value=1, max_value=20, value=3)

    for i in range(num_links):
        with st.expander(f"Mapping #{i+1}"):
            text = st.text_input(f"Visible Text #{i+1}", key=f"text_{i}")
            link = st.text_input(f"Link (tel:, mailto:, https:) #{i+1}", key=f"link_{i}")
            if text and link:
                link_entries.append((text, link))

    if st.button("✨ Add Links and Download"):
        # Save uploaded PDF temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_input:
            temp_input.write(uploaded_pdf.read())
            input_path = temp_input.name

        # Output path
        output_path = input_path.replace(".pdf", "_linked.pdf")

        # Process the PDF
        doc = fitz.open(input_path)
        for page in doc:
            for visible_text, hyperlink in link_entries:
                matches = page.search_for(visible_text)
                for match in matches:
                    page.insert_link({
                        "kind": fitz.LINK_URI,
                        "from": match,
                        "uri": hyperlink
                    })
        doc.save(output_path)
        doc.close()

        # Offer download
        with open(output_path, "rb") as file:
            st.success("✅ Clickable PDF ready!")
            st.download_button(
                label="📥 Download Updated PDF",
                data=file,
                file_name="Clickable_PDF.pdf",
                mime="application/pdf"
            )
