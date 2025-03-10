import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt

stop_words_list = stopwords.words('english')
print('불용어 개수 : ', len(stop_words_list))
print('불용어 10개 출력 : ', stop_words_list[:10])

