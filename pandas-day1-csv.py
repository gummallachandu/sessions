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

2. Inspect Data
df.shape          # rows, columns
df.columns        # list of column names
df.info()         # data types
df.describe()     # summary stats for numeric cols

3. Select Columns
df["name"]            # single column
df[["name", "salary"]]  # multiple columns

4. Filter Rows
# Employees with salary > 55k
df[df["salary"] > 55000]

# Employees in IT department
df[df["department"] == "IT"]

5. Sorting
df.sort_values("salary", ascending=False)   # highest salaries first

6. Add New Column
# Add bonus = 10% of salary
df["bonus"] = df["salary"] * 0.10
print(df)

7. Grouping & Aggregation
# Average salary by department
df.groupby("department")["salary"].mean()

8. Save Back to CSV
df.to_csv("employees_updated.csv", index=False)
