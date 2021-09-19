import os

import pandas as pd

from UserRegister import register
from Login import login
from Spendinglog import spending_log
from Budgetconfig import set_budget
from Overview import overview
import csv


class Housekeeper:

    def __init__(self):
        self.username = ""
        self.password = ""
        self.title = ""
        if not os.path.exists("UserInfo.csv"):
            with open("UserInfo.csv", "w") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['username', 'password', 'title'])
            csvfile.close()
        if not os.path.exists("Budget.csv"):
            with open("Budget.csv", "w") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['month', 'services', 'dining', 'shopping', 'transportation', 'health&fitness',
                                 'uncategorized', 'total', 'income'])
            csvfile.close()
        if not os.path.exists("Spending.csv"):
            with open("Spending.csv", "w") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['username', 'amount', 'category', 'date'])
            csvfile.close()

    def start_menu(self):

        print("I am your Housekeeper, are you my master ?")
        print("Please choose one option to continue your using")
        print("--------------------------------------------------------------------------------")
        print("1.I want to register a new user")
        print("2.I want to login")
        s = input("please input your option, you can input as 1 or 2")
        if s == "1":
            register()
            self.start_menu()
        elif s == "2":
            print("please input your username and password")
            self.username = input('username:')
            self.password = input('password:')
            if not login(self.username, self.password):
                print("wrong username or password, please try it again")
                self.start_menu()
        else:
            print("I do not understand your human words, please register or login")
            self.start_menu()

    def tools_menu(self):
        userinfo_csv = pd.read_csv('UserInfo.csv', sep=',')
        for i in range(len(userinfo_csv)):
            if str(userinfo_csv['username'][i]) == self.username:
                self.title = userinfo_csv['title'][i]
        print("Hello! " + self.username)
        print("you are a " + self.title)
        print("1.log spending")
        print("2.spending overview")
        print("3. budget config(admin user only)")
        s = input("please input your option")
        if s == "1":
            print("spending log")
            spending_log(self.username)
            self.tools_menu()
        elif s == "2":
            overview()
            self.tools_menu()
        elif s == "3" and self.title == "admin user":
            print("set this month budget...")
            set_budget()
            self.tools_menu()


if __name__ == '__main__':
    housekeeper = Housekeeper()

    housekeeper.start_menu()
    housekeeper.tools_menu()
