Study Reference : https://wikidocs.net/217239

# Stopwords
* Appearing frequently, but not meaningful words
* ex) I, my, me, over, is, not, 조사, 접미사....

## Delete English stopwords

```
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt

example = "Family is not an important thing. It's everything."
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example)

result = []
for word in word_tokens:
	if word not in stop_words:
		result.append(word)
```

## Delete Korean stopwords
* Delete 조사, conjunction
* Delete Noun, Adjective stopwords
* One can customize stopwords.