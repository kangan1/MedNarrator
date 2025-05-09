import streamlit as st
from modules.extract_summary import extract_text_from_pdf
from modules.medterm_highlighter import extract_medical_terms
from modules.rag_explainer import explain_terms_with_rag
from modules.simplifier import simplify_text

st.set_page_config(page_title="MedNarrator", layout="wide")
st.title("🩺 MedNarrator – Discharge Summary Simplifier")

uploaded_file = st.file_uploader("Upload a discharge summary (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        text = extract_text_from_pdf(uploaded_file)
    
    st.subheader("🔍 Extracted Text")
    st.text_area("Discharge Summary Text", value=text, height=300)

    with st.spinner("Identifying medical terms..."):
        med_terms = extract_medical_terms(text)
    st.markdown("**Detected Medical Terms:**")
    st.write(med_terms)

    with st.spinner("Explaining terms using medical knowledge base..."):
        explained_terms = explain_terms_with_rag(med_terms)
    st.markdown("**Layperson Explanations:**")
    for term, explanation in explained_terms.items():
        st.write(f"- **{term}**: {explanation}")

    with st.spinner("Simplifying full summary..."):
        simplified = simplify_text(text)
    st.subheader("🧾 Simplified Summary for Patients")
    st.text_area("Patient-Friendly Version", value=simplified, height=300)
