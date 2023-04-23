import pyodbc
 
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=services\bd\Database1.accdb;')

cursor = conn.cursor()



# Executar um comando SQL
cursor.execute("SELECT * FROM cliente")

# Obter os resultados
results = cursor.fetchall()

# Imprimir os resultados
for row in results:
    print(row)
