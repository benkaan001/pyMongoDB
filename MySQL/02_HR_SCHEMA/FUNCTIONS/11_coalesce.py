import mysql.connector
from config import get_database

def get_shipping_address(query):
    connection=get_database()
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print(record)
        connection.commit()
    except mysql.connector.Error as error:
        print(f".......ERROR....{error}")
    finally:
        cursor.close()
        connection.close()
        print(".......Connection closed SUCCESSFULLY!")

# create a shipping address
# replace NULL state_province values with country_id

address_query = """
                SELECT CONCAT(street_address, ",", city, ",", COALESCE(state_province, country_id), ",",country_id)
                as shipping_address
                FROM locations;

                """

get_shipping_address(address_query)

# ('1297 Via Cola di Rie,Roma,IT,IT',)
# ('93091 Calle della Testa,Venice,IT,IT',)
# ('2017 Shinjuku-ku,Tokyo,Tokyo Prefecture,JP',)