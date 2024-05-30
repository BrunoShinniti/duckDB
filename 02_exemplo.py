import duckdb
import random

con = duckdb.connect(database=':memory:')

con.execute("CREATE TABLE estudantes (nome VARCHAR, nota FLOAT);")

con.execute(f"INSERT INTO estudantes VALUES('Bragi the Skerry-rider', {round(random.uniform(0, 10), 2)});")
con.execute(f"INSERT INTO estudantes VALUES('Kari the Jovial', {round(random.uniform(0, 10), 2)});")
con.execute(f"INSERT INTO estudantes VALUES('Ragna the Lore-keeper', {round(random.uniform(0, 10), 2)});")
con.execute(f"INSERT INTO estudantes VALUES('Knuch the Troll-conqueror', {round(random.uniform(0, 10), 2)});")
con.execute(f"INSERT INTO estudantes VALUES('Ketill the Stone-singer', {round(random.uniform(0, 10), 2)});")
con.execute(f"INSERT INTO estudantes VALUES('Leif the Ice-veined', {round(random.uniform(0, 10), 2)});")

resultado = con.execute("SELECT * FROM estudantes;").fetchall()

con.execute("COPY estudantes TO 'estudantes.csv' (HEADER, DELIMITER ',');")

resultado = con.execute("SELECT * FROM read_csv_auto('estudantes.csv')").fetchall()

print(resultado)
