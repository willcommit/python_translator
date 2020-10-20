import pandas as pd

df_translate = pd.read_excel('./translated_workfile.xlsx')

english_words = df_translate['Engelska'].values.tolist()

swedish_words = df_translate['Svenska'].values.tolist()

mixed_list = []


for index in range(len(english_words)):
    mixed_list.append(english_words[index])
    mixed_list.append(swedish_words[index])

df_translated = pd.DataFrame(mixed_list)

df_translated.to_excel('./final.xlsx', encoding='UTF-16')

print('Done')