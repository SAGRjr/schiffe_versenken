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
        ladebalken()
        input_option = input("Do you want to log in (1) or register (2)? ")
        

        if input_option == "1":
            
            login_data = input("Enter your username: ")
             #ask user to put his password
            passwd_entr = input("Enter your password: ")
            ladebalken()

            sSelect = "SELECT COUNT(*) from Klassenkamerad where Login='" + login_data + "' and Password='" + passwd_entr + "'" 
            my_cursor.execute(sSelect)
            result = my_cursor.fetchone()
            bLoginOK = check_table_contents(result)
            if result[0] > 0:
                print("Welcome back " + login_data + ", nice to see you. ")
                bLoginOK = True

                input_option1 = input("Do you want to play (1), add/delete/review words (2), change your password (3), change your username (4) or delete your account (5)? ")

                if input_option1 == "1":
                    ladebalken()
                    decision4 = input("You've chosen to play. Proceed (y/n) ")
                    if decision4 == "y":
                        ladebalken()
                        print("Nothing here yet 💀")
                    elif decision4 == "n":
                        ladebalken()
                        print("Nothing here either 👿")

                elif input_option1 == "2":
                    ladebalken()
                    dcsn = input("Would you like to add (1), delete (2) or just review (3) words? ")
                    if dcsn == "1":
                        ladebalken()
                        decision1 = input("You've decided to add a word, is that correct? (y/n): ")
                        if decision1 == "y":
                            ladebalken()
                            word_entr = input("Please enter your new word here --> ")
                            insert_tabelle = "INSERT INTO Words (Word, UserCreated) VALUES (%s,%s)"
                            insert_value = (word_entr, login_data)
                            my_cursor.execute(insert_tabelle, insert_value)
                            connection.commit()     
                            print('The word', '"'+word_entr+'" has succesfully been added to '+login_data+"'s list.")

                        elif decision1 == "n":
                            ladebalken()
                            print("Returning to start.")
                            main()
                        else:
                            ladebalken()
                            print("I guess that works as well")
                            main()

                    elif dcsn == "2":
                        ladebalken()
                        dcsn1 = input("You've decided to delete a word, is that correct? (y/n): ")
                        if dcsn1 == "y":
                            ladebalken()

                            del_word = input("Please enter the Word you want to delete: ")
                            insert_tabelle = f"SELECT Word FROM Words WHERE Word = '{del_word}'"
                            my_cursor.execute(insert_tabelle)
                            result = my_cursor.fetchone()
                            time.sleep(0.1)
                            ladebalken()
                            

                            if result is not None:
                                insert_tabelle = f"SELECT UserCreated FROM Words WHERE UserCreated = '{login_data}'"
                                my_cursor.execute(insert_tabelle)
                                result = my_cursor.fetchone()
                                if result is not None:

                                    insert_tabelle = f"DELETE FROM Words WHERE Word = '{del_word}'"
                                    my_cursor.execute(insert_tabelle)
                                    connection.commit()
                                    print('The word', '"'+del_word+'" has succesfully been removed from '+login_data+"'s list.")
                                else:
                                    print("Word not found, please make sure to not include any typing errors.")
                            else:
                                print("Word not found, please make sure to not include any typing errors.")

                        elif(dcsn1 == "n"):
                            print("Returning to start.")
                            ladebalken()
                            main()
                        else:
                            ladebalken()
                            print("I guess that works as well")
                            main()

                    elif dcsn == "3":
                        show_list = f"SELECT Word FROM Words WHERE UserCreated = '{login_data}'"
                        my_cursor.execute(show_list)
                        user_list = my_cursor.fetchall()
                        if user_list:
                            ladebalken()
                            column_name = [desc[0] for desc in my_cursor.description]
                            print("Here are all of the words registered in",login_data+"'s list:")
                            

                            for row in user_list:
                                print(row)
                        else:
                            ladebalken()
                            print("The are no words registered in",login_data+"'s list.")
                    else:
                        print("Returning to start")
                        ladebalken()
                        main()

                elif input_option1 == "3":
                    ladebalken()
                    decision2 = input("You've chosen to change your password. Is that correct? (y/n): ")
                    if decision2 == "y":
                        ladebalken()
                        password_old = input("In order to proceed, please enter your old password here --> ")
                        if password_old == passwd_entr:
                            new_pass = input("Please set your new password here --> ")
                            new_pass1 = input("Please repeat your new password --> ")
                            if new_pass == new_pass1:
                                print("Your password has been changed from ", '"'+password_old+'"',  ' to ', '"'+new_pass+'"')
                                insert_tabelle = f"UPDATE Klassenkamerad SET Password = '{new_pass1}' WHERE Login = '{login_data}'"

                                my_cursor.execute(insert_tabelle)
                                connection.commit()
                    elif decision2 == "n":
                        ladebalken()
                        print("Returning to start.")
                        main()
                    else:
                        print("Returning to start.")
                        ladebalken()
                        main()

                elif input_option1 == "4":
                    # print("In order to change your username, you should be made aware that all of your entries will be replaced with the new user. ")
                    decision3 = input("Proceed? (y/n)")
                    if decision3 == "y":
                        passwd_entr2 = input("Please enter your password here --> ")
                        if passwd_entr2 == passwd_entr:
                            new_name = input("Please enter your new username here --> ")
                            print("Your username has been changed from",'"'+login_data+'" to','"'+new_name+'"')
                            insert_tabelle = f"UPDATE Words SET usercreated = '{new_name}' WHERE usercreated = '{login_data}'"
                            my_cursor.execute(insert_tabelle)
                            connection.commit()
                            time.sleep(0.5)
                            insert_tabelle = f"UPDATE Klassenkamerad SET Login = '{new_name}' WHERE Password = '{passwd_entr}'"
                            my_cursor.execute(insert_tabelle)
                            connection.commit()


                    elif decision3 == "n":
                        print("Returning to start.")
                        ladebalken()
                        main()

                    else:
                        print("Returning to start.")
                        ladebalken()
                        main()

                elif input_option1 == "5":
                    print("Are you sure you want to delete your account and your entire information?")
                    del_acc = input("Proceed? (y/n): ")
                    if del_acc == "y":
                        reqst = input("Please enter your username --> ")
                        reqst1 = input("Please enter your password --> ")
                        if reqst == login_data and reqst1 == passwd_entr:
                            insert_tabelle = f"DELETE FROM Words WHERE UserCreated = '{login_data}'"
                            my_cursor.execute(insert_tabelle)
                            connection.commit()
                            time.sleep(0.5)
                            insert_tabelle = f"DELETE FROM Klassenkamerad WHERE Login = '{login_data}'"
                            my_cursor.execute(insert_tabelle)
                            connection.commit()

                            
                    elif del_acc == "n":
                        print("Returning to start.")
                        ladebalken()
                        main()
                    else:
                        print("Returning to start.")
                        ladebalken()
                        main()

            else:
                bLoginOK = False
                print("No entry found 💀💀💀")
                print("Password or username might be wrong, please try again")
                main()
                
            
            


        elif input_option == "2":
            ladebalken()
            login_data1 = input("Please set a username: ")
             #ask user to put his password
            passwd_entr1 = input("Please set a password: ")

            name_entr1 = input("Please enter your name: ")

            surname_entr1 = input("Please enter your surname: ")

            insert_tabelle = "INSERT INTO Klassenkamerad (Login, Password, Name, Nachname) VALUES (%s,%s,%s,%s)"
            insert_value = (login_data1, passwd_entr1,name_entr1,surname_entr1)
            my_cursor.execute(insert_tabelle, insert_value)
            connection.commit()
            ladebalken()
        else:
            print("Please try again")
            main()
        
        



def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()
        
        
number_to_find = random.randint(3, 7)


def ladebalken():
    # A List of Items
    items = list(range(0, number_to_find))
    l = len(items)

    # Initial call to print 0% progress
    printProgressBar(0, l, prefix = 'Loading:', suffix = 'Completed!', length = 50)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.1)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = 'Loading:', suffix = 'Completed!', length = 50)

    
if __name__ == "__main__":
    main()


