import pandas as pd
import sqlite3
from datetime import datetime

# loading data from json to pandas Dataframe
df = pd.read_json('C:/python-projects/project_02/data/data.json')

# adding new column call '_source'
df['_source'] = 'https://lista.mercadolivre.com.br/notebook'

# Adding new column call '_datatime'
df['_datetime'] = datetime.now()

# treating Nones
df['old_money'] = df['old_money'].fillna('0')
df['new_money'] = df['new_money'].fillna('0')
df['reviews_rating_number'] = df['reviews_rating_number'].fillna('0')
df['reviews_amount'] = df['reviews_amount'].fillna('0')

# Cleaning some string data from the dataframe
df['old_money'] = df['old_money'].astype(str).str.replace('.', '', regex=False)
df['new_money'] = df['new_money'].astype(str).str.replace('.', '', regex=False)
df['reviews_amount'] = df['reviews_amount'].astype(str).str.replace('[\(\)]', '', regex=True)

# Converting string data to number
df['old_money'] = df['old_money'].astype(float)
df['new_money'] = df['new_money'].astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].astype(float)
df['reviews_amount'] = df['reviews_amount'].astype(int)

# Filtering price for products that is lower than 1.000 or higher than 10.000

df = df[
    (df['old_money'] >= 1000) & (df['old_money'] <= 10000) & 
    (df['new_money'] >= 1000) & (df['new_money'] <= 10000)
] 

# Connecting to database 
conn = sqlite3.connect('data/mercadolivre.sql')

# saving dataframe in the database
df.to_sql('notebook', conn, if_exists='replace', index=False)

# closing the connection with the database
conn.close()

