import psycopg2

connection = None
my_cursor = None

try:
    connection = psycopg2.connect(host = "horton.db.elephantsql.com", user = "gmldbqwd", 
                                  password = "n4BFSabvT1NE-0fvDKjFD27lea1Z2uBU", dbname = "gmldbqwd")
    
    my_cursor = connection.cursor()

    insert_tabelle = '''CREATE ROW IF NOT EXISTS Klassenkamerad(
                        ID          SERIAL PRIMARY KEY,
                        Login       varchar(40) UNIQUE,
                        Password    varchar(120) NOT NULL,
                        Name        varchar(40) DEFAULT '' NOT NULL,
                        Nachname    varchar(40) DEFAULT '' NOT NULL,
                        Games       INTEGER DEFAULT 0 NOT NULL,
                        Wins        INTEGER DEFAULT 0 NOT NULL,
                        Mistakes    INTEGER DEFAULT 0 NOT NULL
                        ) 
                    '''

    my_cursor.execute(insert_tabelle)

    insert_tabelle = '''CREATE TABLE IF NOT EXISTS Words(
                        ID          SERIAL PRIMARY KEY,
                        Word           varchar(40) UNIQUE,
                        UserCreated    varchar(40) DEFAULT '' NOT NULL
                        ) 
                    '''
    my_cursor.execute(insert_tabelle)


    #insert_tabelle = "INSERT INTO Klassenkamerad (Login, Password, Name, Nachname) VALUES (%s,%s,%s,%s)"
    #insert_value = ("DestyTM", "my_pass","Nikita","Stuhl")
    #my_cursor.execute(insert_tabelle, insert_value)
    #insert_value = ("SAGRjr", "my_pass1","Andreas","Chaidaridis")
    #my_cursor.execute(insert_tabelle, insert_value)

    insert_tabelle = "INSERT INTO Words (Word, UserCreated) VALUES (%s,%s)"
    insert_value = ("Informatik", "DestyTM")
    my_cursor.execute(insert_tabelle, insert_value)
    insert_value = ("Schach", "SAGRjr")
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