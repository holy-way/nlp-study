import urllib.request
import pandas as pd
from konlpy.tag import Mecab
from nltk import FreqDist
import numpy as np
import matplotlib.pyplot as plt

urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings.txt", filename="ratings.txt")
data = pd.read_table('ratings.txt')

print(data[:10])

print('전체 샘플의 수 : {}'.format(len(data)))

sample_data = data[:100]

sample_data['document'] = sample_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", regex=True)

print(sample_data[:10])

stopwords = [
'의','가','이','은','들',
'는','좀','잘','걍','과',
'도','를','으로','자','에',
'와','한','하다',
'을','때','부터','수'
]

tokenizer = Mecab(dicpath = 'C:/mecab/mecab-ko-dic')
tokenized = []

for sentence in sample_data['document']:
	temp = tokenizer.morphs(sentence)
	temp = [word for word in temp if not word in stopwords]
	tokenized.append(temp)

print(tokenized[:10])

vocab = FreqDist(np.hstack(tokenized))
print('단어 집합의 크기 : {}'.format(len(vocab)))

print(vocab['재밌'])

vocab_size = 500
vocab = vocab.most_common(vocab_size)
print('단어 집합의 크기 : {}'.format(len(vocab)))