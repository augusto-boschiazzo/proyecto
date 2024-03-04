import spacy
from spacy.matcher import Matcher
from spacy import displacy


nlp = spacy.load("es_core_news_sm")

texto = "El día 29/02/2024 se descubrió la cura del cáncer."

fecha = [{"SHAPE": "dd/dd/dddd"}]

matcher = Matcher(nlp.vocab)

matcher.add("FECHA", [fecha])

doc = nlp(texto)

coincidencias = matcher(doc)

print("Coincidencias encontradas: ")
for match_id, start, end in coincidencias:
    print(f"{matcher.vocab.strings[match_id]}: {doc[start:end].text}")

for token in doc:
    print(token.i, token, token.dep_, token.head.i, token.head)

displacy.serve(doc, style='dep', port= 5000)