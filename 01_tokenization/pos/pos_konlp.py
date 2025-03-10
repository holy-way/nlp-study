from konlpy.tag import Okt
from konlpy.tag import Kkma

okt = Okt()
kkma = Kkma()

EX_SENTENCE = "열심히 코딩한 당신, 연휴에는 여행을 가봐요"

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
