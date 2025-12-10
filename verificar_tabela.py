import sqlite3

conn = sqlite3.connect("estoque.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(produtos);")
colunas = cursor.fetchall()

print("Colunas da tabela produtos:")
for coluna in colunas:
    print(coluna)

conn.close()