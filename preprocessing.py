from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer


from data_cleaning import Cleaner


class Preprocessor:

    def __init__(self):
        self._stop_words = stopwords.words('russian')
        self._stop_words.append('здравствуйте')
        self._stop_words.append('привет')
        self._stop_words.append('подскажите')
        self._stop_words.append('пожалуйста')
        self._lemmatizer = WordNetLemmatizer()
        self._cleaner = Cleaner()

    def _tokenize(self, sentence: str) -> list:
        tokens = word_tokenize(sentence)
        return tokens

    def _remove_stop_words(self, tokens: list) -> list:
        tokens = [word for word in tokens if word not in self._stop_words]
        return tokens

    def _lemmatization(self, tokens: list) -> list:
        tokens = [self._lemmatizer.lemmatize(word) for word in tokens]
        return tokens

    def data_preprocessing(self, sentence: str) -> str:
        data = self._tokenize(self._cleaner.clean_data(sentence))
        lst = self._lemmatization(self._remove_stop_words(data))
        res = ' '.join(lst)
        return res
