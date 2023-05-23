import psycopg2

connection = None
my_cursor = None

try:
    connection = psycopg2.connect(host = "horton.db.elephantsql.com", user = "gmldbqwd", 
                                  password = "n4BFSabvT1NE-0fvDKjFD27lea1Z2uBU", dbname = "gmldbqwd")
    


    my_cursor = connection.cursor()

    


except Exception as error:
    print("An exception occurred")    
    print(error)

finally:
    if connection is not None:
        connection.close()
    if my_cursor is not None:
        my_cursor.close()
