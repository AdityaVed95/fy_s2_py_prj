import datetime
import json
import pickle
from tkinter import *
from tkinter import messagebox


class Account:

    def __init__(self):
        self.username = None
        self.password = None
        self.current_bal = None

    def signing_in(self):
        def view_balance():
            messagebox.showinfo(title='USER BALANCE', message=f'YOUR BALANCE IS {self.current_bal}')

        def sign_out():
            window_2.destroy()
            messagebox.showinfo(title='SIGN OUT', message='YOU HAVE BEEN SUCCESSFULLY SIGNED OUT !!!')

        def transfer_money():
            def confirm_function():
                flag = 1
                if name_2_entry.get() == self.username:
                    messagebox.showerror(title='Same User', message="You Can't transfer money to yourself")
                    return
                else:
                    for i in range(len(python_object_list_all_usernames)):

                        if name_2_entry.get() == python_object_list_all_usernames[i]:
                            flag = 0
                            messagebox.showinfo(title='VALIDATED', message='USER validated sucessfully')
                            if int(self.current_bal) - int(amount_entry.get()) <= 1000:
                                messagebox.showinfo(title='Insufficient Balance',
                                                    message='Inssufficient balance !! Please try again with lower amount')
                            else:
                                messagebox.showinfo(title='Successful',
                                                    message=f'{amount_entry.get()} transfered to {name_2_entry.get()} from {self.username} successfully')
                                self.current_bal = str(int(self.current_bal) - int(amount_entry.get()))
                                f4 = open(name_2_entry.get(), "rb")
                                account_object_username2 = pickle.load(f4)
                                f4.close()
                                account_object_username2.current_bal = str(
                                    int(account_object_username2.current_bal) + int(amount_entry.get()))
                                f5 = open(name_2_entry.get(), "wb")
                                pickle.dump(account_object_username2, f5)
                                f5.close()
                                f6 = open("all_transaction_history", "a")

                                string1 = "Rs.{} Transfer from {} to {} \n".format(amount_entry.get(), self.username,
                                                                                   name_2_entry.get())
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
                                transfer_window.destroy()
                    if flag == 1:
                        messagebox.showinfo(title='No User',
                                            message=f'No User with Username {name_2_entry.get()} found !!! Please check username and try again')

            transfer_window = Toplevel()
            transfer_window.title('USER WINDOW')
            transfer_window.config(background='light blue')
            transfer_window.geometry('500x300')

            f1 = open("username_existence_check", "r")
            json_object_list_all_usernames = f1.read()
            f1.close()
            python_object_list_all_usernames = json.loads(json_object_list_all_usernames)

            name_2_label = Label(transfer_window, text="Enter the Username to whom you want to transfer",
                                 font=('Times New Roman', 15))
            name_2_label.pack()
            name_2_entry = Entry(transfer_window, font=('ariel', 10))
            name_2_entry.pack()
            amount_label = Label(transfer_window, text='Enter the Amount to be transfered',
                                 font=('Times New Roman', 15))
            amount_label.pack()
            amount_entry = Entry(transfer_window, font=('ariel', 10))
            amount_entry.pack()
            confirm_button = Button(transfer_window, text='Confirm', bg='light blue', fg='black',
                                    command=confirm_function)
            confirm_button.pack()

            transfer_window.mainloop()

        window_2 = Toplevel()
        window_2.title('USER WINDOW')
        window_2.config(background='light blue')
        window_2.geometry('500x300')
        view_balance_button = Button(window_2,
                                     text='VIEW BALANCE',
                                     font=('comic sans', 20),
                                     bg='orange',
                                     fg='black',
                                     command=view_balance,
                                     width=16
                                     )
        view_balance_button.grid(row=1, column=1)

        transfer_button = Button(window_2,
                                 text='TRANSFER MONEY',
                                 font=('comic sans', 20),
                                 bg='orange',
                                 fg='black',
                                 command=transfer_money,
                                 width=16
                                 )
        transfer_button.grid(row=2, column=1)

        sign_out_button = Button(window_2,
                                 text='SIGNOUT',
                                 font=('comic sans', 20),
                                 bg='orange',
                                 fg='black',
                                 command=sign_out,
                                 width=16
                                 )
        sign_out_button.grid(row=3, column=1)

        window_2.mainloop()

    def signing_up(self):
        f1 = open('username_existence_check', "r")
        json_object_list_all_usernames = f1.read()
        f1.close()
        python_object_list_all_usernames = json.loads(json_object_list_all_usernames)

        def submit_name1():
            for i in range(len(python_object_list_all_usernames)):
                if name_entry.get() == python_object_list_all_usernames[i]:
                    messagebox.showerror(title='error', message='username taken! Try again')
                    sign_up_window.destroy()

            if int(amount_entry.get()) > 1000:
                self.current_bal = amount_entry.get()
                self.username = name_entry.get()
                self.password = pass_entry.get()
                messagebox.showinfo(title='sign up successful', message='your account has been created')
                python_object_list_all_usernames.append(self.username)
                json_object_list_all_usernames = json.dumps(python_object_list_all_usernames)
                f3 = open("username_existence_check", "w")
                f3.write(json_object_list_all_usernames)
                f3.close()
                f4 = open(self.username, "wb")
                pickle.dump(self, f4)
                f4.close()
                sign_up_window.destroy()
            else:
                messagebox.showerror(title='error', message='enter amount more than 1000')

        sign_up_window = Toplevel()
        sign_up_window.title('SIGN UP')
        sign_up_window.config(background='light green')
        sign_up_window.geometry('500x300')
        name_label = Label(sign_up_window, text='Enter The User Name of the account you want to create',
                           font=('Times New Roman', 15))
        name_label.pack()
        name_entry = Entry(sign_up_window,
                           font=('ariel', 10)
                           )

        name_entry.pack()

        pass_label = Label(sign_up_window, text='enter password for your account', font=('Times New Roman', 15))
        pass_label.pack()
        pass_entry = Entry(sign_up_window,
                           font=('ariel', 10)
                           )
        pass_entry.pack()
        amount_label = Label(sign_up_window, text='Enter The Amount in your account<min 1000 rupee>',
                             font=('Times New Roman', 15))
        amount_label.pack()
        amount_entry = Entry(sign_up_window,
                             font=('ariel', 10)
                             )

        amount_entry.pack()
        name_submit = Button(sign_up_window, text='submit', bg='light blue', fg='black', command=submit_name1)
        name_submit.pack()

        sign_up_window.mainloop()


def main():
    def sign_in_function():
        def validate():
            f1 = open("username_existence_check", "r")
            json_object_list_all_usernames = f1.read()
            f1.close()
            python_object_list_all_usernames = json.loads(json_object_list_all_usernames)
            flag = 1
            for i in range(len(python_object_list_all_usernames)):
                if name_entry.get() == python_object_list_all_usernames[i]:
                    messagebox.showinfo(title="user validated", message="your account has been validated")
                    f2 = open(name_entry.get(), "rb")
                    name_object = pickle.load(f2)
                    f2.close()

                    if name_object.password == pass_entry.get():
                        flag = 0
                        sign_in_window.destroy()
                        name_object.signing_in()

                    else:
                        messagebox.showinfo(title="incorrect password", message="password entered is incorrect")
                        return

            if flag == 1:
                messagebox.showerror(title="no user",
                                     message='no user with this username found!! please check your username and try again')
                return

        sign_in_window = Toplevel()
        sign_in_window.title('SIGN IN')
        sign_in_window.config(background='light green')
        sign_in_window.geometry('500x300')
        name_label = Label(sign_in_window, text='Enter The User Name of your account', font=('Times New Roman', 15))
        name_label.pack()
        name_entry = Entry(sign_in_window,
                           font=('ariel', 10)
                           )

        name_entry.pack()

        pass_label = Label(sign_in_window, text='enter password of your account', font=('Times New Roman', 15))
        pass_label.pack()
        pass_entry = Entry(sign_in_window,
                           font=('ariel', 10)
                           )
        pass_entry.pack()
        acc_signin_button = Button(sign_in_window, text='SIGN IN', bg='light blue', fg='black'
                                   , command=validate
                                   )
        acc_signin_button.pack()

        sign_in_window.mainloop()

    def sign_up_function():
        account_object = Account()  # create account object

        account_object.signing_up()

    def exit_function():
        messagebox.showinfo(title='SOMAIYA BANKS', message='THANKYOU FOR BANKINNG WITH US')
        window_1.destroy()

    window_1 = Tk()
    window_1.geometry('500x300')
    window_1.title('SOMAIYA BANKS')
    window_1.config(background='light green')
    #    icon = PhotoImage(file='bank-getty.png')
    #    window_1.iconphoto(True, icon)
    welcome_label = Label(window_1, text='Welcome to SOMAIYA BANKS', font=('cambria', 29))
    welcome_label.grid()
    sign_in_button = Button(window_1,
                            text='SIGN IN',
                            font=('comic sans', 30),
                            bg='light blue',
                            fg='black',
                            command=sign_in_function,
                            width=10
                            )
    sign_in_button.grid(row=1, column=0)

    sign_up_button = Button(window_1,
                            text='SIGN UP',
                            font=('comic sans', 30),
                            bg='light blue',
                            fg='black',
                            command=sign_up_function,
                            width=10
                            )
    sign_up_button.grid(row=2, column=0)

    exit_button = Button(window_1,
                         text='EXIT',
                         font=('comic sans', 30),
                         bg='light blue',
                         fg='black',
                         command=exit_function,
                         width=10
                         )
    exit_button.grid(row=3, column=0)

    window_1.mainloop()


if __name__ == '__main__':
    main()
