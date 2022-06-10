from account import Account


# store

def main():
    print("Welcome")

    while True:

        print("Press 1 to sign up")
        print("Press 2 to sign in")
        print("Press 3 to exit the Application")

        response1 = int(input())

        if response1 == 1:
            account_object = Account()  # create account object
            account_object.signing_up()

        elif response1 == 2:
            print("Enter username")
            usr_name = input()
            # now validate if usr name exists(check if the file name exists), if yes then
            # move ahead , if not then go back and ask usr name again
            # now store the object of that user name into a variable
            # account1 = <object of that user name>
            # <object of that user name> has to be stored in a file and then
            # retrieved from there
            # now call the sign in function of the account "object"

            # sign in is done

            while True:
                print("Press 1 to View balance")
                print("Press 2 to Transfer money")
                print("Press 3 to Sign Out")

                response2 = int(input())

                if response2 == 3:
                    break

                if response2 == 1:
                    pass
                    # call the viewing_account_balance function of the account object = account1
                    # account1.viewing_account_balance()

                if response2 == 2:
                    pass
                    # call the transferring_money function of the account object = account1
                    # account1.transferring_money()
                    # money is transferred now


        elif response1 == 3:
            print("Thank You for Banking with us")


if __name__ == "__main__":
    main()
