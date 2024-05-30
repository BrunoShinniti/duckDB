import pandas as pd
import duckdb

churn = pd.read_csv("./dataset/Churn.csv", sep=';')

query = """
    SELECT
        CreditScore,
        Geography,
        Age
    FROM churn
    WHERE Gender = 'Female'
    ORDER BY Age
"""

db = duckdb.sql(query)

print(db)