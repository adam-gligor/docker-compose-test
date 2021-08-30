import os
import psycopg2


def test_foo():
    postgres_url = os.getenv("POSTGRES_URL")
    postgres_client = psycopg2.connect(postgres_url)

    with postgres_client.cursor() as cursor:
        cursor.execute("SELECT NOW();", ())
        db_data = cursor.fetchall()
        print(db_data[0])
        assert db_data[0]
