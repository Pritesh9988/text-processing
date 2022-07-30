import pandas as pd
df = pd.read_excel("text.xlsx")
df.head()

df_is = df['text'].str.lower().str.contains(' is ')
df_is
df1 = df[df_is]
df1

df_not = df1['text'].str.lower().str.contains(' my |pakistan')
df_not
df2 = df1[df_not]
df2

df_final = dff = df1[~df1.isin(df2)].dropna()
df_final

df_final.to_excel("result.xlsx")
df_final