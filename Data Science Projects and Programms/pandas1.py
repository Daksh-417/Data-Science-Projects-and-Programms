import pandas as pd
s = pd.Series([10,20,30],index = ['a','b','c'])
print(s['b'])
print(s.loc['a'])
print(s.iloc['a'])