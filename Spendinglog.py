import pandas as pd
import datetime


def spending_log(username: str):
    print("loading...")
    spending_csv = pd.read_csv('Spending.csv', sep=',')
    category_list = ['services', 'dining', 'shopping', 'transportation', 'health&fitness', 'uncategorized']
    while not input("please input start to start log spending or exit to save and exit") == "exit":
        amount = input("please input spending amount")
        category = input("please choose your category from:" + str(category_list))
        now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        spending_csv = spending_csv.append(
            {'username': username, 'amount': amount, 'category': category, 'date': now_time}, ignore_index=True)
    spending_csv.to_csv('Spending.csv', sep=',', na_rep='NULL', columns=['username', 'amount', 'category', 'date'], index=False)

    
if __name__ == '__main__':
    spending_log('tom')
