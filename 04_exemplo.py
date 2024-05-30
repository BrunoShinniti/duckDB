import duckdb
import pandas as pd
from faker import Faker
from random import randint

fake = Faker()

n_rows:int = 1_000

duckdb_con = duckdb.connect(database="database.duckdb")

duckdb_con.execute("DROP TABLE IF EXISTS pessoas;")
duckdb_con.execute("DROP TABLE IF EXISTS status;")

duckdb_con.execute("CREATE TABLE IF NOT EXISTS pessoas (id INT, name VARCHAR, email VARCHAR, city VARCHAR, last_access DATE, status_id INT);")
duckdb_con.execute("CREATE TABLE IF NOT EXISTS status (id INT, status VARCHAR);")

df_status = {
            "id": [1, 2, 3, 4, 5],
            "status": ["Bloqueado", "Alerta", "Ativado", "Ausente", "N/A"]
            }

dataframe_status = pd.DataFrame.from_dict(df_status)

duckdb_con.execute("INSERT INTO status SELECT * FROM dataframe_status;")

data = [
    {
        "id": c,
        "name": fake.name(),
        "email": fake.ascii_email(),
        "city": fake.city(),
        "last_access": fake.date_this_year(),
        "status_id": randint(1, 5)
    } for c in range(n_rows)]

dataframe = pd.DataFrame.from_dict(data)

duckdb_con.execute("INSERT INTO pessoas SELECT * FROM dataframe;")

query = "SELECT p.*, s.status FROM pessoas p LEFT JOIN status s ON p.status_id = s.id"

resultado = duckdb_con.sql(query)

print(resultado)
