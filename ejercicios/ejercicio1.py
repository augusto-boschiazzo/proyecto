import spacy
from spacy import displacy

nlp = spacy.load("es_core_news_sm")

texto = "El presidente de la 'compañía XYZ', Juan Pérez, anunció hoy en una conferencia de prensa que la empresa ha alcanzado un acuerdo para adquirir a su competidor principal, Google. La transacción está valuada en 1.5 mil millones de dólares y se espera que se complete a finales de este año."

doc = nlp(texto)

for en in doc.ents:
    print(f"Entidad encontrada: {en}")

for token in doc:
    print(token, token.dep)

# Visualizar las entidades con displacy
options = {"compact": True, "color": "blue"}
displacy.serve(doc, style="ent", options=options, port= 5003)

