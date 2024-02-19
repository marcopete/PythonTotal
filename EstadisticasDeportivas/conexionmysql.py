import mysql.connector

config = {
    'user': 'mpuga',
    'password': '123qweasd',
    'host': 'localhost',
    'database': 'MP_DATA_UAT',
    'raise_on_warnings': True
}

try:
    connection = mysql.connector.connect(**config)

    cursor = connection.cursor()

    query = "SELECT * FROM Dim_Equipo;"
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión cerrada")
