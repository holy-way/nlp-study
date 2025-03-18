KO_TEXT = "사과의 놀라운 효능이라는 글을 봤어. 그래서 오늘 사과를 먹으려고 했는데 사과가 썩어서 슈퍼에 가서 사과랑 오렌지 사왔어"

print(KO_TEXT.split())

from konlpy.tag import Mecab
tokenizer = Mecab(dicpath = 'C:/mecab/mecab-ko-dic')

print(tokenizer.morphs(KO_TEXT))