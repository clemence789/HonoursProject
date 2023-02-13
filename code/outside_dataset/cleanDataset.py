import pandas as pd

df = pd.read_csv(r'code\outside_dataset\outsideDataset.csv', encoding='utf-8') #read csv with saved tweets
df.columns = ['Score', 'ID', 'Date', 'Query', 'Username', 'Text'] #add columns to dataframe

df.to_csv(r'code\outside_dataset\outsideDataset.csv')