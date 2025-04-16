import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('C:\python-projects\project_02\data\mercadolivre.sql')

df = pd.read_sql_query('SELECT * FROM notebook', conn)

conn.close()

st.title('Pesquisa de Mercado - Notebooks no mercado livre')

st.subheader('KPIS Principais')
col1, col2, col3 = st.columns(3)

total_items = df.shape[0]
col1.metric(label='Total de Notebooks', value=total_items)

unique_brands = df['brand'].nunique()
col2.metric(label='Marcas Únicas', value=unique_brands)

average_new_price = df['new_money'].mean()
col3.metric(label='Preço Médio (R$)', value=f"{average_new_price:.2f}")

st.subheader('Marcas mais encontradas até a 2ª Página')
col1, col2 = st.columns([4,2])
top_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_brands)
col2.write(top_brands)

st.subheader('Preço médio por marca')
col1, col2 = st.columns([4,2])
df_non_zero_prices = df[df['new_money'] > 0]
average_price_by_brand = df_non_zero_prices.groupby('brand')['new_money'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

st.subheader('Satisfação média por marca')
col1, col2 = st.columns([4,2])
df_non_zero_prices = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_prices.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)
