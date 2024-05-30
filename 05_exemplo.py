import duckdb
import pandas as pd
from faker import Faker
from random import randint

# Library thats generate fake data
fake = Faker()

# Number of registry to create data
n_rows:int = 1_000

# Build a connection to database
duckdb_con = duckdb.connect(database="database.duckdb")

# Drop tables if exists
duckdb_con.execute("DROP TABLE IF EXISTS peoples;")
duckdb_con.execute("DROP TABLE IF EXISTS status;")

# Generate values for status table
df_status = {
            "id": [1, 2, 3, 4, 5],
            "status": ["Blocked", "Alert", "Activate", "Absent", "NaN"]
            }

# Create a Pandas DataFrame for status
dataframe_status = pd.DataFrame.from_dict(df_status)

# From dataframe, create a table status
duckdb_con.from_df(dataframe_status).create("status")

# Looping to generate fake registrys
data = [
    {
        "id": c,
        "name": fake.name(),
        "email": fake.ascii_email(),
        "city": fake.city(),
        "last_access": fake.date_this_year(),
        "status_id": randint(1, 5)
    } for c in range(n_rows)]

# Create a Pandas Dataframe peoples
dataframe = pd.DataFrame.from_dict(data)

# From dataframe, create a table peoples
duckdb_con.from_df(dataframe).create("peoples")

# Query thats join peoples and status
query = "SELECT p.*, s.status FROM peoples p LEFT JOIN status s ON p.status_id = s.id"

# Execute query
result = duckdb_con.sql(query)

# Print the result
print(result)
