import nltk
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from tensorflow.keras.preprocessing.text import text_to_word_sequence

ex_str = "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."

print('word_tokenize :',
	word_tokenize(ex_str)
)

print('WordPunctTokenizer :',
	WordPunctTokenizer().tokenize(ex_str)
)

print('text_to_word_sequence : ',
	text_to_word_sequence(ex_str)
)