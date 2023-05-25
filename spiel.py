import psycopg2
import os
import sys


def getConnection():
    connection = None
    my_cursor = None
    try:
        connection = psycopg2.connect(host = "horton.db.elephantsql.com", user = "gmldbqwd", 
                                  password = "n4BFSabvT1NE-0fvDKjFD27lea1Z2uBU", dbname = "gmldbqwd")
    except:
        print("An exception occurred")                              

    my_cursor = connection.cursor()
    return connection, my_cursor

    #select user and password from Klassenkamerad and check if there: select count(*) from  Klassenkamerad where Password='' and ....
def check_table_contents(result):

    #my_cursor = connection.cursor
    #my_cursor.execute("SELECT COUNT(*) FROM your_table")
    #result = my_cursor.fetchone()
    bLoginOK = False
    # if count(*) > 0 --> user can go on - else exit the program...
    if result[0] > 0:
        print("Eintrag gefunden.")
        bLoginOK = True
    else:
        bLoginOK = False
        print("Kein Eintrag vorhanden.")

    # wenn result >0... dann bLoginOK = True
 
    # ask user if he wants to register new word or to play! 
    return bLoginOK


def main():
    # get connection to the DB
    connection, my_cursor = getConnection()
    if my_cursor:
        input_option = input("Do you want to log in (1) or register (2)? ")

        if input_option == "1":
            login_data = input("Enter your username: ")
             #ask user to put his password
            passwd_entr = input("Enter your password: ")
        elif input_option == "2":
            login_data1 = input("Enter a username: ")
             #ask user to put his password
            passwd_entr1 = input("Enter a password: ")
        
        sSelect = "SELECT COUNT(*) from Klassenkamerad where Login='" + login_data + "' and Password='" + passwd_entr + "'" 
        print(sSelect)
        my_cursor.execute(sSelect)
        result = my_cursor.fetchone()
        bLoginOK = check_table_contents(result)
        print(str(result))
        
            


    else:
        print("cursor is None")
    
if __name__ == "__main__":
    main()