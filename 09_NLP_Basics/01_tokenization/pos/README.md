Studying NLP From https://wikidocs.net/217237

## Part-of-speech tagging

* Same word can be used in various meanings.
* The part-of-speech of the word is useful to understand the exact meaning in the senetence.

## KoNLPY pos tagging
* We can use Korean pos taggers
	* Okt(Open Korea Text)
	* Mecab
	* Komoran
	* Hannanum
	* Kkma

* Korean Pos Taggers Features
	* morphs - slicing words into morpheme units
	* pos - tag the part-of-speech for each morphemes  
	* nouns - extract only nouns


## Code & Result
### Code
```
# Okt
print('OKT 형태소 분석 : ',
	okt.morphs(EX_SENTENCE))

print('OKT 품사 태깅 : ',
	okt.pos(EX_SENTENCE))

print('OKT 명사 추출 : ',
	okt.nouns(EX_SENTENCE))

# Kkma
print('꼬꼬마 형태소 분석 : ',
	kkma.morphs(EX_SENTENCE))

print('꼬꼬마 품사 태깅 : ',
	kkma.pos(EX_SENTENCE))

print('꼬꼬마 명사 추출 : ',
	kkma.nouns(EX_SENTENCE))

```

### Result
```
OKT 형태소 분석 :  ['열심히', '코딩', '한', '당신', ',', '연휴', '에는', '여행', '을', '가봐요']
OKT 품사 태깅 :  [('열심히', 'Adverb'), ('코딩', 'Noun'), ('한', 'Josa'), ('당신', 'Noun'), (',', 'Punctuation'), ('연휴', 'Noun'), ('에는', 'Josa'), ('여행', 'Noun'), ('을', 'Josa'), ('가봐요', 'Verb')]
OKT 명사 추출 :  ['코딩', '당신', '연휴', '여행']

꼬꼬마 형태소 분석 :  ['열심히', '코딩', '하', 'ㄴ', '당신', ',', '연휴', '에', '는', '여행', '을', '가보', '아요']
꼬꼬마 품사 태깅 :  [('열심히', 'MAG'), ('코딩', 'NNG'), ('하', 'XSV'), ('ㄴ', 'ETD'), ('당신', 'NP'), (',', 'SP'), ('연휴', 'NNG'), ('에', 'JKM'), ('는', 'JX'), ('여행', 'NNG'), ('을', 'JKO'), ('가보', 'VV'), ('아요', 'EFN')]
꼬꼬마 명사 추출 :  ['코딩', '당신', '연휴', '여행']
```