import nltk
import spacy
from nltk.tokenize import word_tokenize

spacy_en = spacy.load('en_core_web_sm')
nltk.download('punkt')

EN_TEXT = "A Dog Run back corner near spare bedrooms"

def tokenize(en_text):
	return [tok.text for tok in spacy_en.tokenizer(en_text)]

print(tokenize(EN_TEXT))
print(word_tokenize(EN_TEXT))
print(EN_TEXT.split())
print(list(EN_TEXT))