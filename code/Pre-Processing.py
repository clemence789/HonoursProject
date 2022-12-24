import csv
import pandas as pd

df = pd.read_csv(r'C:\Users\cleme\Documents\1HonoursProject\code\dataset.csv')

#Put individual tweets on the same rows in csv
df=df.applymap(lambda x: x.encode('unicode_escape').\
    decode('utf-8') if isinstance(x, str) else x)

df.to_csv(r'C:\Users\cleme\Documents\1HonoursProject\code\dataset.csv')