# import pandas as pd
# from numpy.ma.core import where
#
# marks = pd.Series([10,29,38]
#                   ,["dani","alo","patalo"])
#
# print(marks)
# print(type(marks))
# # print(marks[2])
# print(marks["alo"])
# print(marks.iloc[2])
#
#
# print("sum",marks.sum())
# print("mean",marks.mean())
# print("min",marks.min())
# print("max",marks.max())
#
#
#
#
# print("filtering",where(marks.notnull()))
# print("filtering",where(marks>=11))
# print(marks[marks >= 11])
#
# mark = pd.Series([10,30,20,50,70,80,40,40])
# print(marks.sort_values())
# print(marks.sort_values(ascending=False))
# print(marks.sort_values(ascending=False))
#
#
#
#
#
# marks = pd.Series(
#     [10, 29, 38],
#     index=["dani", "alo", "patalo"]
# )
#
# print(marks.sort_values())
#
# data = {
#     "Name": ["Ali", "Dani", "Ahmed", "Sara"],
#     "Age": [20, 21, 19, 22],
#     "Marks": [0, 92, 65, 88]
# }
#
# df = pd.DataFrame(data)
# print(df)
# # print(type(df))
# # print(df.head())
# # print(df.tail())
# # print(df.describe())
# # print(df.describe(include="all"))
# # print(df["Name"])
# # print(df.iloc[0])
# print(df[df["Marks"].notnull()])
# print(df[df["Marks"] >= 80])
# print(df[df["Age"] >=21])
# print(df[(df["Age"] <= 22) & (df["Marks"].notnull())])
# df["passed"] = df["Marks"]>= 50
# print(df)
# df["Marks + 5"] = df["Marks"] + 5
# print(df)
#
# import pandas as pd
#
# df = pd.DataFrame({
#     "Name": ["Ali", "Dani", "Ahmed", "Sara"],
#     "Marks": [78, None, 65, 88],
#     "Age": [20, 21, None, 22]
# })
#
# print(df)
# print(df.isnull().sum())
# df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
# print(df)
# print(df.isnull().sum())


import pandas as pd

df = pd.DataFrame({
    "Name": ["Ali", "Dani", "Ahmed", "Sara"],
    "Marks": [78, None, 65, 88],
    "Age": [20, 21, None, 22]
})

df.to_csv("students.csv", index=False)
print("csv file svaed")
new_df = pd.read_csv("students.csv")
print(new_df)