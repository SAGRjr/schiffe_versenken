import psycopg2

connection = None
my_cursor = None

try:
    connection = psycopg2.connect(host = "horton.db.elephantsql.com", user = "gmldbqwd", 
                                  password = "n4BFSabvT1NE-0fvDKjFD27lea1Z2uBU", dbname = "gmldbqwd")
except:
    print("An exception occurred")                              


if my_cursor:
    #ask user to put his login name
    #ask user to put his password
    #select user and password from Klassenkamerad ad check if there: select count(*) from  Klassenkamerad where Password='' and ....
    # if count(*) > 0 --> user can go on - else exit the program...

    # ask user if he wants to register new word or to play!
    # 