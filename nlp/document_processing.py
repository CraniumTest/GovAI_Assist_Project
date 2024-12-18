import spacy
# Load the English NLP model
nlp = spacy.load('en_core_web_sm')

def summarize(text):
    # Dummy summarization
    doc = nlp(text)
    return " ".join([sent.text for sent in doc.sents][:2])

if __name__ == "__main__":
    text = "Your document text here."
    print(summarize(text))
