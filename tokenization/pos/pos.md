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