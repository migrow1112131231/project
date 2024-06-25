import pandas as pd

df = pd.read_excel('data.xlsx')

df.columns = df.columns.str.strip()

all_cont = df['Country'].unique()