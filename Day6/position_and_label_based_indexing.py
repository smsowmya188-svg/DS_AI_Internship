import pandas as pd
marks=pd.Series([85,90,78],index=['math','science','english'])
print(marks['math'])
print(marks[['math','english']])
print(marks.index[2],":",marks.iloc[2])
