import psycopg2
import os
import sys
import time
import random



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

            sSelect = "SELECT COUNT(*) from Klassenkamerad where Login='" + login_data + "' and Password='" + passwd_entr + "'" 
            my_cursor.execute(sSelect)
            result = my_cursor.fetchone()
            bLoginOK = check_table_contents(result)
            if result[0] > 0:
                print("Entry found.")
                print("Welcome " + login_data + ", nice to see you. 😊")
                bLoginOK = True

                input_option1 = input("Do you want to play (1), add a word (2), change your password (3), change your username (4), change your name (5), change your surname (6) or delete your account (7)? ")
                if input_option1 == "1":
                    print("ok")
                elif input_option1 == "2" :
                    decision1 = input("You've decided to add a word, is that correct? Yes (y) or No (n): ")
                    if decision1 == "y":
                        word_entr = input("Please enter your new word here --> ")
                        insert_tabelle = "INSERT INTO Words (Word, UserCreated) VALUES (%s,%s)"
                        insert_value = (word_entr, login_data)
                        my_cursor.execute(insert_tabelle, insert_value)

                        connection.commit()
                    else:
                        print("Bruv")

                elif input_option1 == "3":
                    decision2 = input("You've chosen to change your password. Is that correct? Yes (y) or No (n): ")
                    if decision2 == "y":
                        password_old = input("In order to proceed, please enter your old password here --> ")
                        if password_old == passwd_entr:
                            new_pass = input("Please set your new password here --> ")
                            new_pass1 = input("Please repeat your new password --> ")
                            if new_pass == new_pass1:
                                print("Your password has been changed from ", '"',password_old,'"',  ' to ', '"',new_pass, '"')
                                insert_tabelle = f"UPDATE Klassenkamerad SET Password = '{new_pass1}' WHERE login = '{login_data}'"
                                print(insert_tabelle)

                                my_cursor.execute(insert_tabelle)
                                connection.commit()
                elif input_option1 == "4":
                    print("What is that supposed to mean mate?")
                elif input_option1 == "5":
                    print("Ok then give me your birth certificate")
                elif input_option1 == "6":
                    print("No you can't do that")
                elif input_option1 == "7":
                    print("Aight bet")

            else:
                bLoginOK = False
                print("No entry found 💀💀💀")
            
            


        elif input_option == "2":
            login_data1 = input("Please set a username: ")
             #ask user to put his password
            passwd_entr1 = input("Please set a password: ")

            name_entr1 = input("Please enter your name: ")

            surname_entr1 = input("Please enter your surname: ")

            insert_tabelle = "INSERT INTO Klassenkamerad (Login, Password, Name, Nachname) VALUES (%s,%s,%s,%s)"
            insert_value = (login_data1, passwd_entr1,name_entr1,surname_entr1)
            my_cursor.execute(insert_tabelle, insert_value)
            connection.commit()
        
        



        
        
            


    else:
        print("cursor is None")
    
if __name__ == "__main__":
    main()