import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="laboratory_catalog",
        user="postgres",
        password="postgres123"
    )

    print("CONNECTED")

except Exception as e:
    print(e)