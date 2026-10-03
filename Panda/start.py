import pandas as pd

marks = pd.Series([78, 85, 92, 67, 90])

print(marks)



marks = pd.Series([78, 85, 92, 67, 90])

print(marks)
print(marks[2])





marks = pd.Series(
    [78, 85, 92, 67, 90],
    index=["Ali", "Dani", "Ahmed", "Sara", "Usman"]
)

print(marks)
print(marks["Dani"])


import pandas as pd

marks = pd.Series([78, 85, 92, 67, 90])

print("Sum:", marks.sum())
print("Average:", marks.mean())
print("Highest:", marks.max())
print("Lowest:", marks.min())


import pandas as pd

marks = pd.Series([78, 85, 92, 67, 90])

print(marks[marks >= 80])


import pandas as pd

data = {
    "Name": ["Ali", "Dani", "Ahmed", "Sara"],
    "Age": [20, 21, 19, 22],
    "Marks": [78, 92, 65, 88]
}

df = pd.DataFrame(data)

print(df)

print(df["Name"])
print(df["Marks"])



print(df.iloc[0])
print(df.iloc[2])





