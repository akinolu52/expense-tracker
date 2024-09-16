# expense-tracker

expenses: https://roadmap.sh/projects/expense-tracker

to use run the command:
`sudo pip install -e .`


```bash
$ expense-tracker add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ expense-tracker add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ expense-tracker add --description "Dinner" --amount 10 --category "Food"
# Expense added successfully (ID: 3)

$ expense-tracker list
# ID  Date       Description  Category  Amount 
# 1   2024-08-06  Lunch       Food      $20
# 2   2024-08-06  Dinner      None      $10

$ expense-tracker list --category
# ID  Date       Description  Category  Amount
# 1   2024-08-06  Lunch       Food     $20

$ expense-tracker summary
# Total expenses: $30

$ expense-tracker delete --id 1
# Expense deleted successfully

$ expense-tracker summary
# Total expenses: $20

$ expense-tracker summary --month 9
# Total expenses for September: $80

$ expense-tracker export --month 9
# September Expenses exported successfully.
```