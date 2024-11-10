import pyodbc

conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=cafe-test.database.windows.net;DATABASE=cafe')
cursor = conn.cursor()

print("Connected")
