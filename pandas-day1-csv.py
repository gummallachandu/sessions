Simple Pandas Operations on CSV File

Assume we have a CSV file called employees.csv:

id,name,department,salary,hire_date
1,Alice,IT,60000,2020-01-15
2,Bob,HR,52000,2019-05-20
3,Charlie,Finance,58000,2021-03-01
4,Diana,IT,62000,2018-11-11
5,Eva,Finance,55000,2022-02-18

1. Read CSV into a DataFrame
import pandas as pd

df = pd.read_csv("employees.csv")
print(df.head())   # show first 5 rows

🔹 1. Basic Info
df.head()       # first 5 rows
df.tail()       # last 5 rows
df.shape        # (rows, columns)
df.columns      # list of column names
df.info()       # summary of columns & data types
df.describe()   # summary stats for numeric columns


👉 Used for quick inspection of your dataset.

🔹 2. Selecting Columns & Rows
df["name"]                      # select one column (Series)
df[["name", "salary"]]          # select multiple columns
df.iloc[0]                      # first row (by index)
df.loc[2, "name"]               # value in row 2, column "name"


👉 .loc is label-based, .iloc is index-based.

🔹 3. Filtering
df[df["salary"] > 55000]               # filter by condition
df[(df["salary"] > 55000) & (df["department"]=="IT")]  


👉 Equivalent to SQL WHERE.

🔹 4. Sorting
df.sort_values("salary")                # ascending
df.sort_values("salary", ascending=False)  # descending


👉 Equivalent to SQL ORDER BY.

🔹 5. Handling Missing Data
df.isnull().sum()          # count missing values per column
df.fillna(0)               # replace NaN with 0
df.dropna()                # drop rows with NaN


👉 Critical for data cleaning.

🔹 6. Creating / Modifying Columns
df["bonus"] = df["salary"] * 0.10
df["hire_date"] = pd.to_datetime(df["hire_date"])
df["year"] = df["hire_date"].dt.year


👉 New features can be derived easily.

🔹 7. Grouping & Aggregation
df.groupby("department")["salary"].mean()      # avg salary per dept
df.groupby("department")["salary"].agg(["mean","max","min"])


👉 Equivalent to SQL GROUP BY.

🔹 8. Joining & Merging
dept_info = pd.DataFrame({
    "department": ["IT","HR","Finance"],
    "location": ["NY","LA","SF"]
})

df.merge(dept_info, on="department", how="left")


👉 Equivalent to SQL JOIN.

🔹 9. Apply Functions
df["name_length"] = df["name"].apply(len)   # length of each name
df["salary_bracket"] = df["salary"].apply(lambda x: "High" if x > 58000 else "Low")


👉 Very flexible, similar to SQL CASE WHEN.

🔹 10. Value Counts & Unique
df["department"].value_counts()   # count per dept
df["department"].unique()         # unique values


👉 Quick way to analyze categorical columns.

🔹 11. Concatenation
pd.concat([df.head(2), df.tail(2)])   # stack DataFrames

🔹 12. Pivot Tables
pd.pivot_table(df, values="salary", index="department", aggfunc="mean")


👉 Excel-style pivot, powerful for analysis.

🔹 13. Exporting
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)

⚡ Quick Summary
Category	Functions
Inspecting	head(), tail(), shape, info(), describe()
Selecting
