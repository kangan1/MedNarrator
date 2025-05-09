from transformers import pipeline

# Load a Hugging Face model for medical text generation (e.g., BioGPT or similar)
explanation_model = pipeline("text-generation", model="mistral-7b")

def explain_terms_with_rag(medical_terms):
    explanations = {}
    for term in medical_terms:
        # Generate explanation using the LLM for each medical term
        explanation = explanation_model(f"Explain this medical term to a layperson: {term}")
        explanations[term] = explanation[0]['generated_text']
    return explanations
