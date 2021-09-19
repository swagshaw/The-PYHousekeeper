"""
Sign up your user
every user have three items: Username,Password,Title
"""
import pandas as pd
import re


def register():
    print("Register now")
    userinfo_csv = pd.read_csv('UserInfo.csv', sep=',')
    if not userinfo_csv['title'].empty:
        print("your family already have an admin user, please register a general user")
        print("please input your username, 3-12 characters, no numbers")
        username = input('username:')
        num = re.findall(r'd+', username)
        length_u = len(username)
        while num or length_u < 3 or length_u > 12:
            print('input error username, please input again')
            print("please input your username, 3-12 characters, no numbers")
            username = input('username:')
            num = re.findall(r'd+', username)
            length_u = len(username)
        print("please input your password, 6-12 characters")
        password = input('password:')
        length_p = len(password)
        while length_p < 6 or length_p > 12:
            print('input error password, please input again')
            print("please input your password, 6-12 characters")
            password = input('password:')
            length_p = len(password)
        title = 'general user'
        s = {'username': username, 'password': password, 'title': title}
        userinfo_csv = userinfo_csv.append(s, ignore_index=True)
        print(userinfo_csv.to_string())
    else:
        print("please register an admin user")
        username = input('username:')
        num = re.findall(r'd+', username)
        length_u = len(username)
        while num or length_u < 3 or length_u > 12:
            print('input error username, please input again')
            print("please input your username, 3-12 characters, no numbers")
            username = input('username:')
            num = re.findall(r'd+', username)
            length_u = len(username)
        print("please input your password, 6-12 characters")
        password = input('password:')
        length_p = len(password)
        while length_p < 6 or length_p > 12:
            print('input error password, please input again')
            print("please input your password, 6-12 characters")
            password = input('password:')
            length_p = len(password)
        title = 'admin user'
        s = {'username': username, 'password': password, 'title': title}
        userinfo_csv = userinfo_csv.append(s, ignore_index=True)
        print(userinfo_csv.to_string())
    userinfo_csv.to_csv('UserInfo.csv', sep=',', na_rep='NULL', columns=['username', 'password', 'title'], index=False)


if __name__ == '__main__':
    register()
