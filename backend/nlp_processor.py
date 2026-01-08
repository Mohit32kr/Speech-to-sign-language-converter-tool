import spacy

nlp = spacy.load("en_core_web_sm")

def process_text(text):
    doc = nlp(text)
    keywords = []

    for token in doc:
        if token.pos_ not in ["AUX", "DET", "PUNCT"]:
            keywords.append(token.text.lower())

    return " ".join(keywords)
