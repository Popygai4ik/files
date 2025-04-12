import pandas as pd

url = "https://docs.google.com/spreadsheets/d/14X69q6Hp5meGkozvJnPmnuK-ZNZmDvDHJVxRHlHXQrE/export?format=csv"
df = pd.read_csv(url)

row_204 = df.iloc[202]
s =  str(row_204).split('\n')
for res in s:
    print(str(res).replace(r'\n','  ',1).replace('NaN','Пока нету данных',1))
    print('_'*len(str(res).replace(r'\n','  ',1).replace('NaN','Пока нету данных',1)))
# print("\n🔹 204-я строка:\n", str(row_204).split('\n'))