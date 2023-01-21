import re

from config import REGEX


class Cleaner:

    def clean_data(self, sentence: str) -> str:
        cleaned_sentence = re.sub(REGEX, ' ', sentence)
        cleaned_sentence = cleaned_sentence.lower()
        return cleaned_sentence
