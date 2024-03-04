import spacy
from spacy.matcher import DependencyMatcher
from spacy import displacy

nlp = spacy.load("es_core_news_sm")

texto = "En el estudio de las ciencias sociales, los investigadores examinan cómo los patrones de migración afectan las dinámicas familiares. El análisis detallado de estos patrones revela tendencias que sugieren cambios en la estructura social."

doc = nlp(texto)

matcher = DependencyMatcher(nlp.vocab)

patron = [
    {
        "RIGHT_ID": "anchor_subject",
        "RIGHT_ATTRS": {"DEP": "nsubj"}
    },
    {
        "LEFT_ID": "anchor_subject",
        "REL_OP": "<",
        "RIGHT_ID": "anchor", 
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "anchor",
        "REL_OP": ">",
        "RIGHT_ID": "anchor_object",
        "RIGHT_ATTRS": {"DEP": "obj"},
    }
]

matcher.add("EXAMINAN", [patron])
matches = matcher(nlp(doc))


for j in range(len(matches)):
    print("Coincidencia numero ", j+1)
    match_id, token_ids = matches[j]
    for i in range(len(token_ids)):
        print(patron[i]["RIGHT_ID"] + ":", doc[token_ids[i]].text)