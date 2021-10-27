import pandas as pd

df=pd.read_csv('./files/account.csv', ';')

print(df.shape[0])
print(df.shape[1])

print(df['account_id'].max())