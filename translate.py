import pandas as pd
from googletrans import Translator

translator = Translator()

df_translate = pd.read_excel('./swe_trans.xlsx')

words_to_translate = df_translate['String-1'].values.tolist()

translations = translator.translate(words_to_translate, src="en", dest='sv')

words_translated = []

for translation in translations:
    words_translated.append(translation.text) 

translate_dict = dict(zip(words_to_translate, words_translated))

df_translated = pd.DataFrame.from_dict(translate_dict, orient='index')

df_translated.to_excel('./translated.xlsx', encoding='UTF-16')

print('Done')