# creating a savings account
import json


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

        f3 = open("username_existence_check", "w")
        f3.write(python_object_list_all_usernames)
        f3.close()

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
        pass
        # at this point it has been confirmed that the username exists
        # now let us ask for the password and confirm is the password matches the username
        # check if the password entered is the same as self.password
        # if not then ask user to retype the password
        # once password is correct:
        # sign in is successful
        # now get back to from where this fxn was called

    def transferring_money(self):
        print("Enter the username to whom you want to transfer money")
        # take the username and check if it exists(check if the file exists with that name as that of the
        # username), if not then ask to re-enter
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
        print("The Balance of your account is:", self.password)
