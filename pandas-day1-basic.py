🐼 Pandas Series vs DataFrame
Series → One-dimensional (like a single column in Excel or SQL)
import pandas as pd

# A Series: just one column
s = pd.Series([10, 20, 30, 40], name="marks")
print(s)


Output:

0    10
1    20
2    30
3    40
Name: marks, dtype: int64


👉 Key points:

Has one column (with a name: "marks")

Has an index (0,1,2,3 by default)

Behaves like a list + dictionary hybrid

DataFrame → Two-dimensional (like a full Excel sheet or SQL table)
# A DataFrame: multiple columns
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "marks": [85, 90, 78, 92]
})
print(df)


Output:

      name  marks
0    Alice     85
1      Bob     90
2  Charlie     78
3    Diana     92


👉 Key points:

Has rows & columns (2D structure)

Each column is actually a Series

A DataFrame = a collection of Series

✅ Show relationship
# A single column from DataFrame is a Series
type(df["marks"])   # <class 'pandas.core.series.Series'>

# The whole df is a DataFrame
type(df)            # <class 'pandas.core.frame.DataFrame'>
