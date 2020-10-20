import re
import pandas as pd

def create_new_col_dict():
    excel_clean_item_col = open_filedialog('CLEAN ITEM COL')
    df_ref_clean = pd.read_excel(excel_clean_item_col)

    new_col_dict = {}

    for item, data in df_ref_clean.iterrows():
        if data.change:
            new_col_dict[data.nav_name] = data.dss_name
    
    return new_col_dict

def change_item_col(df_old):
    new_col_dict = create_new_col_dict()

    for col, cont in df_old.iteritems():
        for nav, dyn in new_col_dict.items():
            if col == nav:
                df_old.rename(columns={col:dyn}, inplace=True)
    
    return df_old

def find_clean_website(website):
    if re.search('\www.*', str(website)):
        return website
    else:
        return ''
    

def delete_rows(df_delete, df_main, column_name):

    #find_delete_rows(df_delete)
    rows_to_delete = df_delete[column_name]

    print("{} rows will be deleted".format(len(rows_to_delete)))

    count = 0
    dropped_rows = []

    for index, data in df_main.iterrows():
        for nr in rows_to_delete:
            if (data.Nr == nr):
                df_main.drop([index], inplace=True)
                dropped_rows.append(data.Nr)
                count += 1
    
    non_dropped_rows = set(rows_to_delete).difference(set(dropped_rows))

    print("{} rows deleted and {} remaing".format(count, len(df_main.index)))
    print("{} rows not dropped".format(len(non_dropped_rows)))

    save_to_csv(non_dropped_rows, 'non_dropped.csv')

    return df_main

def save_to_csv(set, filename):
    csv_file = open(filename, 'w')

    for item in set:
        csv_file.write("{} \n".format(item))

    csv_file.close()

def data_cleaner(df, value):
    if value == 'Ja':
        return df.replace('Ja', True, regex=True)
    elif value == 'Nej':
        return df.replace('Nej', False, regex=True)
    elif value == 'TB=pris-kostnad':
        return df.replace('TB=pris-kostnad', 'Vinst=pris-kostnad', regex=True)
    elif value == 'Hemsida':
        df_final['Hemsida'] = df_final['Hemsida'].apply(find_clean_website)
    else:
        pass

if __name__ == "__main__":
    excel_old_data = open_filedialog('NAV EXPORT')
    df_old = pd.read_excel(excel_old_data)

    change_item_col(df_old)
    
