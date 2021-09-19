import datetime

import pandas as pd
import re

budget_csv = pd.read_csv('Budget.csv', sep=',')
userinfo_csv = pd.read_csv('UserInfo.csv', sep=',')
spending_csv = pd.read_csv('Spending.csv', sep=',')


def overview():
    now_month = datetime.datetime.now().strftime('%Y-%m')
    print("this month is " + now_month)
    month_expenditure = 0
    expenditure_list = {'services': 0, 'dining': 0, 'shopping': 0, 'transportation': 0, 'health&fitness': 0,
                        'uncategorized': 0}
    for i in range(len(spending_csv)):
        if re.search(pattern=str(now_month), string=spending_csv['date'][i]):
            month_expenditure = month_expenditure + int(spending_csv['amount'][i])
            for item in expenditure_list:
                if item == spending_csv['category'][i]:
                    expenditure_list[item] += spending_csv['amount'][i]
    print("month_expenditure is  " + str(month_expenditure))
    month = datetime.datetime.now().strftime('%m')
    print(expenditure_list)
    total_budget = 0
    budget_list = {'services': 0, 'dining': 0, 'shopping': 0, 'transportation': 0, 'health&fitness': 0,
                   'uncategorized': 0}
    for i in range(len(budget_csv)):
        if "0" + str(budget_csv['month'][i]) == month:
            total_budget = budget_csv['total'][i]
            print(budget_csv['total'][i])
            for item in budget_list:
                budget_list[item] = budget_csv[item][i]
    print("this month total budget is " + str(total_budget))
    print(budget_list)
    if total_budget < month_expenditure:
        print("\033[31m warning! expenditure is more than budget this month \033[0m")
    elif (month_expenditure / total_budget) > 0.9:
        print("\033[33m warning! budget is used more that 90% \033[0m")
    else:
        print("\033[33m keep going , you still have some budget \033[0m")

    for item in budget_list:
        if budget_list[item] < expenditure_list[item]:
            print("checking in " + item)
            print("\033[31m warning! expenditure is more than budget this month \033[0m")
        elif (budget_list[item] / expenditure_list[item]) > 0.9:
            print("checking in " + item)
            print("\033[33m warning! budget is used more that 90% \033[0m")

    user_list = userinfo_csv['username']

    for item in user_list:
        spending = 0
        for i in range(len(spending_csv)):
            if spending_csv['username'][i] == item:
                spending += spending_csv['amount'][i]
        print("this is " + str(item) + " this month spending: " + str(spending))

    print("here are some details for you, input 1")
    print("or you want 6 month summary, input 2")
    s = input("please input:")
    if s == "1":
        expenditure_list = {'services': 0, 'dining': 0, 'shopping': 0, 'transportation': 0, 'health&fitness': 0,
                            'uncategorized': 0}
        print("this is your spending detail")
        username = input("please input your username:")
        for i in range(len(spending_csv)):
            if spending_csv['username'][i] == username:
                print(str(spending_csv['username'][i]) + " " + str(spending_csv['amount'][i]) + " in " + str(
                    spending_csv['category'][i]) + " on " + str(spending_csv['date'][i]))
                expenditure_list[str(spending_csv['category'][i])] += spending_csv['amount'][i]
        print(expenditure_list)
    if s == "2":
        for i in range(6):
            month_summary((datetime.datetime.now() - datetime.timedelta(days=30 * i)).strftime('%m'))


def month_summary(month):
    print("this month is " + month)
    month_expenditure = 0
    for i in range(len(spending_csv)):
        if re.search(pattern=str(month), string=spending_csv['date'][i]):
            month_expenditure = month_expenditure + int(spending_csv['amount'][i])
    print("month_expenditure is  " + str(month_expenditure))
    total_budget = 0
    for i in range(len(budget_csv)):
        if "0" + str(budget_csv['month'][i]) == month:
            total_budget = budget_csv['total'][i]
    print("this month total budget is " + str(total_budget))

    print("saving money is:" + str(total_budget - month_expenditure))


if __name__ == '__main__':
    overview()
