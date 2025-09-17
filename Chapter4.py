import json
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

with open("exercises/en/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = spacy.blank("en")
matcher = Matcher(nlp.vocab)

# Two tokens whose lowercase forms match "iphone" and "x"
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]

# Token whose lowercase form matches "iphone" and a digit
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]

# Add patterns to the matcher and create docs with matched entities
matcher.add("GADGET", [pattern1, pattern2])
docs = []
for doc in nlp.pipe(TEXTS):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]
    print(spans)
    doc.ents = spans
    docs.append(doc)

import spacy
from spacy.tokens import Span

nlp = spacy.blank("en")

doc1 = nlp("Reddit partners with Patreon to help creators build communities")
doc1.ents = [
    Span(doc1, 0, 1, label="WEBSITE"),
    Span(doc1, 2, 3, label="WEBSITE"),
]

doc2 = nlp("PewDiePie smashes YouTube record")
doc2.ents = [Span(doc2, 2, 3, label="WEBSITE")]

doc3 = nlp("Reddit founder Alexis Ohanian gave away two Metallica tickets to fans")
doc3.ents = [Span(doc3, 0, 1, label="WEBSITE")]