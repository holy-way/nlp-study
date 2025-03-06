from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

text = "I am actively looking for Ph.D. students. and you are a Ph.D. student."

tokenized_sentece = word_tokenize(text)

print('단어 토큰화 : ', tokenized_sentece)
print('품사 태깅 : ', pos_tag(tokenized_sentece))
