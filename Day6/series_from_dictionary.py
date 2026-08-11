import pandas as pd
x={"math": 75, "science": 90, "english": 88}
y=pd.Series(x)
print(y)
print(y['english'])