from account import Account
import pickle
import json


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
            f4 = open(account_object.username, "wb")
            pickle.dump(account_object, f4)
            f4.close()
            print("Congratulations !! Sign Up is completed successfully")




        elif response1 == 2:

            f1 = open("username_existence_check", "r")
            json_object_list_all_usernames = f1.read()
            f1.close()
            python_object_list_all_usernames = json.loads(json_object_list_all_usernames)

            temp_user_name = ""
            print("Enter username of your account")
            while True:
                flag = 0
                temp_user_name = input()
                for item in python_object_list_all_usernames:
                    if item == temp_user_name:
                        flag = 1
                        break

                if flag == 1:
                    break

                elif flag == 0:
                    print("The Entered User Name doesn't exist")
                    print("Please Try Again")

            print("Existence of your account has been confirmed")
            user_name = temp_user_name
            f2 = open(user_name, "rb")
            account_object_sign_in_mode = pickle.load(f2)
            f2.close()
            account_object_sign_in_mode.signing_in()

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

                if response2 == 1:
                    account_object_sign_in_mode.viewing_account_balance()
                    # call the viewing_account_balance function of the account object = account1
                    # account1.viewing_account_balance()

                if response2 == 2:
                    account_object_sign_in_mode.transferring_money()
                    # let the person who is transferring money be username_1
                    # call the transferring_money function of the account object = account1
                    # account1.transferring_money()
                    # money is transferred now

                    # creating changes in the file of the user_name1

                    f3 = open(account_object_sign_in_mode.username, "wb")
                    pickle.dump(account_object_sign_in_mode, f3)
                    f3.close()

                if response2 == 3:
                    break


        elif response1 == 3:
            print("Thank You for Banking with us")
            break


if __name__ == "__main__":
    main()
