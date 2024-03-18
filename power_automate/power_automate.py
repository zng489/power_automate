import pandas as pd
import re


df = pd.read_csv('pokemon.csv')
df['Name'][0]
df.to_csv('qweqw.csv')
print(df['Name'][0])