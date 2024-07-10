import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="18403",
        host="127.0.0.1",
        port="5432",
        database="waste_management_system"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
