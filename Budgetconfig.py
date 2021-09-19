import pandas as pd


def set_budget():
    print("loading...")
    budget_csv = pd.read_csv('Budget.csv', sep=',')
    print("please admin user set this month budget")
    month = input("month:")
    category_list = {'services': 0, 'dining': 0, 'shopping': 0, 'transportation': 0, 'health&fitness': 0,
                     'uncategorized': 0}
    total_budget = 0
    for item in category_list:
        category_list[item] = input("please set " + item + " budget")
        total_budget = total_budget + int(category_list[item])
    income = input("income:")
    while int(income) < int(total_budget):
        print("budget should not more than your income")
        total_budget = 0
        for item in category_list:
            category_list[item] = input("please set " + item + " budget")
            total_budget = total_budget + int(category_list[item])
        income = input("income:")
    print("so total budget = " + str(total_budget))
    print("income = " + str(income))
    budget_csv = budget_csv.append(
        {'month': month, 'services': category_list['services'], 'dining': category_list['dining'],
         'shopping': category_list['shopping'], 'transportation': category_list['transportation'],
         'health&fitness': category_list['health&fitness'],
         'uncategorized': category_list['uncategorized'], 'total': total_budget, 'income': income}, ignore_index=True)
    print(budget_csv.to_string())
    budget_csv.to_csv('Budget.csv', sep=',', na_rep='NULL', columns=['month', 'services', 'dining', 'shopping',
                                                                     'transportation', 'health&fitness',
                                                                     'uncategorized', 'total', 'income'],
                      index=False)


if __name__ == '__main__':
    set_budget()
