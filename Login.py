import pandas as pd


def login(username: str, password: str):
    print("loading...")
    userinfo_csv = pd.read_csv('UserInfo.csv', sep=',')
    user_list = userinfo_csv['username']
    for i in range(len(userinfo_csv)):
        if str(user_list[i]) == username and str(userinfo_csv['password'][i]) == password:
            return True
    return False


if __name__ == "__main__":
    print(login(username='tom', password='123456'))
