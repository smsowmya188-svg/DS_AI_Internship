import pandas as pd
data=pd.Series([40,27,14,None,15,None,10])
print(data.isnull())
print(data.fillna(0))
 