import spacy

# Load the scispacy model for medical NER
nlp = spacy.load("en_core_sci_md")

def extract_medical_terms(text):
    doc = nlp(text)
    medical_terms = []
    for ent in doc.ents:
        if ent.label_ in ['DISEASE', 'TREATMENT', 'SYMPTOM', 'MEDICATION']:
            medical_terms.append(ent.text)
    return medical_terms
