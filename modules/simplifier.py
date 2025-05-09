from transformers import pipeline

# Load a text summarization or simplification model
simplification_model = pipeline("summarization", model="t5-small")

def simplify_text(text):
    # Simplify the text by summarizing it
    simplified = simplification_model(text)
    return simplified[0]['summary_text']
