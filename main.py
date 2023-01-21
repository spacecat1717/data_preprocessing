import pandas as pd

from config import FILE_PATH, HEAD
from preprocessing import Preprocessor

preprocessor = Preprocessor()


df = pd.read_excel(FILE_PATH)
df['preprocessed'] = df[HEAD].apply(lambda sentence: preprocessor.data_preprocessing(sentence))
df.to_excel(FILE_PATH)

