import pandas as pd
from numpy.ma.core import where

marks = pd.Series([10,29,38]
                  ,["dani","alo","patalo"])

print(marks)
print(type(marks))
# print(marks[2])
print(marks["alo"])
print(marks.iloc[2])


print("sum",marks.sum())
print("mean",marks.mean())
print("min",marks.min())
print("max",marks.max())




print("filtering",where(marks.notnull()))
print("filtering",where(marks>=11))
print(marks[marks >= 11])

mark = pd.Series([10,30,20,50,70,80,40,40])
print(marks.sort_values())
print(marks.sort_values(ascending=False))
print(marks.sort_values(ascending=False))



data = {
    "name": ["Dani","ali","ahmed","sara"],



}