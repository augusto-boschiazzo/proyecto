import spacy

nlp = spacy.load("es_core_news_sm")
lemmatizer = nlp.get_pipe("lemmatizer")

text = "En el ámbito de la electrónica."
doc = nlp(text)

text_filtered = [token.text for token in doc if not token.is_stop]

print(text_filtered)