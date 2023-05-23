import psycopg2

connection = None
my_cursor = None

try:
    connection = psycopg2.connect(host = "horton.db.elephantsql.com", user = "gmldbqwd", 
                                  password = "n4BFSabvT1NE-0fvDKjFD27lea1Z2uBU", dbname = "gmldbqwd")
    my_cursor = connection.cursor()
except:
    print("An exception occurred")                              
print(str(connection))
print(str(my_cursor))
if my_cursor:
    my_cursor.execute("SELECT * FROM XXX")
    connection.close()
