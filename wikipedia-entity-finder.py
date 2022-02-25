# -*- coding: utf-8 -*-

!pip install wikipedia

import wikipedia

wikipedia.set_lang("en")

wikipedia.search("keyword")

!python -m spacy download en

!pip install spacy

import spacy

NER = spacy.load("en_core_web_sm")

text= NER(wikipedia.page("'pageName'").content)

for w in text.ents:
    print(w.text,w.label_)

spacy.displacy.render(text, style="ent",jupyter=True)

