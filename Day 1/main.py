with open('expense_report.txt', 'r') as f:
    data = f.readlines()
expense_report = []
for item in data:
    expense = item.rstrip()
    expense_report.append(int(expense))

for expense in expense_report:
    for other_expense in expense_report:
        for third_expense in expense_report:
            answer = expense + other_expense + third_expense
            if answer == 2020:
                print('Answer is ' + str(expense) + ' and ' + str(other_expense) + ' and ' + str(third_expense))
                print(expense * other_expense * third_expense)

