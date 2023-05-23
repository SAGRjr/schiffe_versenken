import psycopg2

connection = None
my_cursor = None

try:
    connection = psycopg2.connect(host = "horton.db.elephantsql.com", user = "gmldbqwd", 
                                  password = "n4BFSabvT1NE-0fvDKjFD27lea1Z2uBU", dbname = "gmldbqwd")
    
    my_cursor = connection.cursor()

    tabelle = """CREATE TABLE IF NOT EXIST Klassenkamerad(
                        id          int PRIMARY KEY,
                        Name        varchar(40) NOT NULL,
                        Nachname    varchar(40) NOT NULL,
                        Jahrgang    int)"""
    
    my_cursor.execute(tabelle)

    connection.commit()

    
except Exception as error:
    print("An exception occurred")    
    print(error)

finally:
    if connection is not None:
        connection.close()
    if my_cursor is not None:
        my_cursor.close()