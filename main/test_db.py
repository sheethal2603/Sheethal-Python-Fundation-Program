from util import get_connection

def test_connection():
    try:
        conn = get_connection()
        if conn:
            print(" Connection successful")
        else:
            print(" Connection failed")
    except Exception as e:
        print(" Error connecting to DB:", e)

    