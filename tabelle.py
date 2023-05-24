import psycopg2

connection = None
my_cursor = None

try:
    connection = psycopg2.connect(host = "horton.db.elephantsql.com", user = "gmldbqwd", 
                                  password = "n4BFSabvT1NE-0fvDKjFD27lea1Z2uBU", dbname = "gmldbqwd")
    
    my_cursor = connection.cursor()

    insert_tabelle = '''CREATE TABLE IF NOT EXISTS Klassenkamerad(
                        id          int PRIMARY KEY,
                        name        varchar(40) NOT NULL,
                        nachname    varchar(40)) '''

    my_cursor.execute(insert_tabelle)

    insert_tabelle = "INSERT INTO Klassenkamerad (id, Name, Nachname. Jahrgang) VALUES (%s,%s,%s)"
    insert_value = (1,"Nikta", "Chair")

    my_cursor.execute(insert_tabelle, insert_value)

    connection.commit()

    
except Exception as error:
    print("An exception occurred")    
    print(error)

finally:
    if connection is not None:
        connection.close()
    if my_cursor is not None:
        my_cursor.close()