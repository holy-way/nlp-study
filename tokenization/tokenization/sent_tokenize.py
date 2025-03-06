import nltk
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize

text = "His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to make sure no one was near."

print('문장 토큰화1 : ', sent_tokenize(text))

text = "I am actively looking for Ph.D. students. and you are a Ph.D student"

print('문장 토큰화2 : ', sent_tokenize(text))

