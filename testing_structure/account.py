# creating a savings account
from transaction_entry import TransactionEntry


class Account:

    def __init__(self):
        self.username = None
        self.password = None
        self.current_bal = None
        self.is_active = "y"
        self.account_id = "auto_generate"
        self.is_kyc_done = "y"

        self.transactions = []
        # self.transactions.append(TransactionEntry())

    def signing_up(self):
        pass

        # now we have two options:
        # store the object of that account into a file so that all the details regarding
        # the object is stored in that file

        # or:

        # create a dictionary containing user name as key and account object
        # as the value
        # question is how to store dictionary, so that even after the program ends,
        # the dictionary is not lost

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