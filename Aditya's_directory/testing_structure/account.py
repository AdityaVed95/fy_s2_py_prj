# creating a savings account
import json
import pickle
import datetime


class Account:

    def __init__(self):
        self.username = None
        self.password = None
        self.current_bal = None
        # self.is_active = "y"
        # self.account_id = "auto_generate"
        # self.is_kyc_done = "y"

        # self.transactions = []
        # self.transactions.append(TransactionEntry())

    def signing_up(self):

        # logic to check for username existence and avoiding same usernames
        temp_username = ""

        f1 = open("username_existence_check", "r")
        json_object_list_all_usernames = f1.read()
        f1.close()
        python_object_list_all_usernames = json.loads(json_object_list_all_usernames)

        while True:

            flag = 1
            print("Enter The User Name of the account you want to create:")
            temp_username = input()

            for item in python_object_list_all_usernames:
                if temp_username == item:
                    print("Sorry!!! This Username already exists")
                    print("Please try again")
                    flag = 0
                    break

            if flag == 0:
                continue

            if flag == 1:
                break

        self.username = temp_username

        # writing the new username to username_existence_check file

        # f2 = open("username_existence_check", "r")
        # json_object_list_all_usernames = f2.read()
        # f2.close()
        #
        # python_object_list_all_usernames = json.loads(json_object_list_all_usernames)

        python_object_list_all_usernames.append(self.username)
        json_object_list_all_usernames = json.dumps(python_object_list_all_usernames)

        f3 = open("username_existence_check", "w")
        f3.write(json_object_list_all_usernames)
        f3.close()

        print("Hurray!! You now have a unique Username !!")
        print("Enter the password for your Current Account")
        self.password = input()

        print("Enter the balance of your Current Account (Please enter more than Rs.1000)")
        temp_balance = 0
        while True:
            temp_balance = float(input())
            if temp_balance <= 1000:
                print("Please enter more than Rs.1000")
                print("Please try again")
            else:
                break
        self.current_bal = temp_balance

        # also check for the fact that two users with same username should not exist
        # now we have two options:
        # store the object of that account into a file so that all the details regarding
        # the object is stored in that file

        # or:

        # create a dictionary containing user name as key and account object
        # as the value
        # question is how to store dictionary, so that even after the program ends,
        # the dictionary is not lost
        # the answer to above question is by: using json format

        # I think storing the object to a file is a better option

    def signing_in(self):
        print("Enter Password to Sign in to your account")

        while True:
            password_input = input()
            if password_input == self.password:
                print("Password Authentication Successful")
                break
            else:
                print("Incorrect Password Input")
                print("Please try again")

        print("{} has successfully logged into his/her account".format(self.username))

        # at this point it has been confirmed that the username exists
        # now let us ask for the password and confirm is the password matches the username
        # check if the password entered is the same as self.password
        # if not then ask user to retype the password
        # once password is correct:
        # sign in is successful
        # now get back to from where this fxn was called

    def transferring_money(self):

        f1 = open("username_existence_check", "r")
        json_object_list_all_usernames = f1.read()
        f1.close()
        python_object_list_all_usernames = json.loads(json_object_list_all_usernames)

        print("Enter the username to whom you want to transfer money")
        while True:
            username_2 = input()
            flag = 0
            for item in python_object_list_all_usernames:
                if username_2 == item:
                    if username_2 == self.username:
                        print("Sorry You cannot transfer money to yourself")
                        print("Please input another username")
                    else:
                        print("Successfully validated the existence of the account to which money is to be transferred")
                        flag = 1
                        break

            if flag == 1:
                break

            elif flag == 0:
                print("Sorry! The username to which the money is to be transferred Does NOT exit")
                print("Please try again")

        print("Enter the amount to be transferred to ", username_2)

        while True:
            amount_transfer = float(input())
            if self.current_bal - amount_transfer > 1000:
                print("Sufficient Balance to proceed transaction")
                break
            elif self.current_bal - amount_transfer < 1000:
                print("Insufficient Balance found in {} 's account ".format(self.username))
                print("Please Note that minimum of Rs.1000 should be your current balance")
                print("Please try again")

        print("Congratulations!! Transaction successful")

        # updating current balance of username_1
        self.current_bal = self.current_bal - amount_transfer

        # creating changes in the file of user_name2:
        f4 = open(username_2, "rb")
        account_object_username2 = pickle.load(f4)
        f4.close()

        account_object_username2.current_bal = account_object_username2.current_bal + amount_transfer

        f5 = open(username_2, "wb")
        pickle.dump(account_object_username2, f5)
        f5.close()

        f6 = open("all_transaction_history", "a")

        string1 = "Rs.{} Transfer from {} to {} \n".format(amount_transfer, self.username, username_2)
        f6.write(string1)

        e = datetime.datetime.now()
        string2 = "Time of occurrence of Transaction:\n"
        string3 = e.strftime("%d/%m/%Y\n")
        string4 = e.strftime("%I:%M:%S %p\n")
        f6.write(string2)
        f6.write(string3)
        f6.write(string4)
        f6.write("================================\n")
        f6.close()

        # take the username and check if it exists, if not then ask to re-enter
        # if yes then moving on
        # ask the amount to be transferred
        # check if after removing that amount: the remaining amount is more than or equal to 1000rs
        # if yes then remove that much amount from senders account, so bascically update the balance of
        # senders account object and then make sure that the updated balance is also written to the file in which
        # all that object is stored
        # after this add money to the receivers account and make sure that the updated balance of the reciever
        # is written to the file which contains the object
        # now go back to the calling function

    def viewing_account_balance(self):
        print("The Balance of your account is:", self.current_bal)
