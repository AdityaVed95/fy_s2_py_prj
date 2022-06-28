# import pickle
#
# f1 = open("ady", "rb")
# object1 = pickle.load(f1)
# print(object1.username)
# print(object1.password)
# print(object1.current_bal)
# f1.close()
# print(type(object1.password))


import json
import pickle
from tkinter import *
from tkinter import messagebox


class Account:

    def _init_(self):
        self.username = None
        self.password = None
        self.current_bal = None

    def signing_up(self):

        # logic to check for username existence and avoiding same usernames

        f1 = open('username_existence_check', "r")
        json_object_list_all_usernames = f1.read()
        f1.close()
        python_object_list_all_usernames = json.loads(json_object_list_all_usernames)

        sign_up_window = Toplevel()
        sign_up_window.title('SIGN UP')
        sign_up_window.config(background='light green')

        def submit_name1():

            for item in python_object_list_all_usernames:
                if str(name_entry.get()) == item:
                    messagebox.showerror(title='error', message='username taken! Try again')
                    sign_up_window.destroy()
                else:
                    while (TRUE):
                        if int(amount_entry.get()) > 1000:
                            self.current_bal = amount_entry.get()
                            self.username = name_entry.get()
                            self.password = pass_entry.get()
                            messagebox.showinfo(title='sign up successful', message='your account has been created')
                            sign_up_window.destroy()
                        else:
                            messagebox.showerror(title='error', message='enter amount more than 1000')

        sign_up_window.geometry('500x500')
        name_label = Label(sign_up_window, text='Enter The User Name of the account you want to create')
        name_label.pack()
        name_entry = Entry(sign_up_window,
                           font=('ariel', 10),
                           )

        name_entry.pack()

        pass_label = Label(sign_up_window, text='enter password for your account')
        pass_label.pack()
        pass_entry = Entry(sign_up_window,
                           font=('ariel', 10),
                           )
        pass_entry.pack()
        amount_label = Label(sign_up_window, text='Enter The Amount in your account<min 1000 rupee>')
        amount_label.pack()
        amount_entry = Entry(sign_up_window,
                             font=('ariel', 10),
                             )

        amount_entry.pack()
        name_submit = Button(sign_up_window, text='submit', bg='light blue', fg='black', command=submit_name1)
        name_submit.pack()

        sign_up_window.mainloop()


def main():
    def sign_in_function():
        pass

    def sign_up_function():
        account_object = Account()  # create account object

        account_object.signing_up()
        f4 = open(account_object.username, "wb")
        pickle.dump(account_object, f4)
        f4.close()
        messagebox.showinfo(title='SIGN UP', message="Congratulations !! Sign Up is completed successfully")

    def exit_function():
        # need to add thankyou message box
        messagebox.showinfo(title='SOMAIYA BANKS', message='THANKYOU FOR BANKINNG WITH US')
        window_1.destroy()

    window_1 = Tk()
    window_1.geometry('500x500')
    window_1.title('SOMAIYA BANKS')
    window_1.config(background='light green')
    # icon = PhotoImage(file='C:\\Users\\LENOVO\Desktop\\python_project\\New folder\\bank-getty.png')
    # window_1.iconphoto(True, icon)

    sign_in_button = Button(window_1,
                            text='SIGN IN',
                            font=('comic sans', 30),
                            bg='light blue',
                            fg='black',
                            command=sign_in_function,
                            # width=7
                            )
    sign_in_button.grid(row=1, column=1)

    sign_up_button = Button(window_1,
                            text='SIGN UP',
                            font=('comic sans', 30),
                            bg='light blue',
                            fg='black',
                            command=sign_up_function,
                            # width=7
                            )
    sign_up_button.grid(row=1, column=2)

    exit_button = Button(window_1,
                         text='EXIT',
                         font=('comic sans', 30),
                         bg='light blue',
                         fg='black',
                         command=exit_function,
                         # width=7
                         )
    exit_button.grid(row=1, column=3)

    window_1.mainloop()


if __name__ == '__main__':
    main()
