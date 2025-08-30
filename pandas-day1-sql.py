import pandas as pd
from sqlalchemy import create_engine

# Connect to Sakila MySQL (change creds accordingly)
engine = create_engine("mysql+pymysql://root:password@localhost/sakila")

# Load whole tables as Pandas DataFrames
films = pd.read_sql("SELECT * FROM film", engine)
actors = pd.read_sql("SELECT * FROM actor", engine)
categories = pd.read_sql("SELECT * FROM category", engine)
film_category = pd.read_sql("SELECT * FROM film_category", engine)
inventory = pd.read_sql("SELECT * FROM inventory", engine)
rental = pd.read_sql("SELECT * FROM rental", engine)
customer = pd.read_sql("SELECT * FROM customer", engine)
payment = pd.read_sql("SELECT * FROM payment", engine)


films.head()         # DataFrame of film table
films.columns        # all column names
films.shape          # rows, cols

# customers with their payments
SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM payment p
JOIN customer c ON p.customer_id = c.customer_id;

#pandas
payment = pd.read_sql("SELECT * FROM payment", engine)

cust_payments = payment.merge(customer, on="customer_id")
cust_payments[["first_name", "last_name", "amount", "payment_date"]].head()


