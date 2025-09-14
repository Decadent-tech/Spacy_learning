# Import spaCy
import spacy

# Create a blank English nlp object
nlp = spacy.blank("en")

# Created by processing a string of text with the nlp object
doc = nlp("Hello world!")

# Iterate over tokens in a Doc
for token in doc:
    print(token.text)

# Index into the Doc to get a single Token
token = doc[1]

# Get the token text via the .text attribute
print(token.text)

# A slice from the Doc is a Span object
span = doc[1:3]

# Get the span text via the .text attribute
print(span.text)


doc1 = nlp("It costs $5.")
print("Index:   ", [token.i for token in doc1])
print("Text:    ", [token.text for token in doc1])

print("is_alpha:", [token.is_alpha for token in doc1])
print("is_punct:", [token.is_punct for token in doc1])
print("like_num:", [token.like_num for token in doc1])

nlp = spacy.load("en_core_web_sm")

doc = nlp("She ate the pizza")

# Iterate over the tokens
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)


for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)



# Process a text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)

print("GPE:" , spacy.explain("GPE"))
print("NNP:" , spacy.explain("NNP"))
print("dobj:" , spacy.explain("dobj"))