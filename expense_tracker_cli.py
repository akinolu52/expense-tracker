import sys

from expense_tracker import ExpenseTracker


def main():
    if len(sys.argv) < 2:
        print("Usage: expense-tracker <command> [options]")
        return

    command = sys.argv[1]
    expense_tracker = ExpenseTracker()

    if command == 'add':
        if 6 < len(sys.argv) < 8:
            print("Usage: expense-tracker add --description <description> --amount <amount> --category <category>")
            return

        if len(sys.argv) < 7:
            print("Usage: expense-tracker add --description <description> --amount <amount>")
            return

        description = sys.argv[3]

        if len(description) < 1:
            print("Usage: expense-tracker add --description <description> --amount <amount>")
            return

        amount = int(sys.argv[5])
        category = None

        if len(sys.argv) == 8:
            category = sys.argv[7]

        expense_tracker.add_expense(description, amount, category)

    elif command == 'update':
        if len(sys.argv) != 7:
            print("Usage: expense-tracker update --id <id> --description <description> --amount <amount>")
            return

        id = int(sys.argv[3])
        description = sys.argv[5]
        amount = int(sys.argv[7])

        expense_tracker.update_expense(id, description, amount)

    elif command == 'delete':
        if len(sys.argv) != 4:
            print("Usage: expense-tracker delete --id <id>")
            return

        id = int(sys.argv[3])
        expense_tracker.delete_expense(id)

    elif command == 'list':
        if 2 < len(sys.argv) != 4:
            print("Usage: expense-tracker list --filter <filter>")
            return

        category = None
        if len(sys.argv) == 4:
            category = sys.argv[3]

        expense_tracker.list_expenses(category)

    elif command == 'summary':
        if len(sys.argv) > 4:
            print("Usage: expense-tracker summary --month <month>")
            return

        month = None
        if len(sys.argv) == 4:
            month = int(sys.argv[3])

        expense_tracker.total_expense(month)

    else:
        print("Unknown command")


if __name__ == '__main__':
    main()
