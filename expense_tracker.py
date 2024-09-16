import json
import os
from datetime import datetime
from typing import List, Dict, Any, Union, Optional

EXPENSE_FILE_PATH = './expenses.json'


class Expense:
    def __init__(self, id: int, description: str, amount: int, created_at: datetime, updated_at: datetime):
        self.id: int = id
        self.description: str = description
        self.amount: int = amount
        self.created_at: str = created_at.isoformat()
        self.updated_at: str = updated_at.isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'description': self.description,
            'amount': self.amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Expense':
        return Expense(
            id=data['id'],
            description=data['description'],
            amount=data['amount'],
            created_at=datetime.fromisoformat(data['created_at']),
            updated_at=datetime.fromisoformat(data['updated_at'])
        )


class ExpenseTracker:
    def __init__(self):
        self.expenses: List[Expense] = self.load_expenses()

    @staticmethod
    def load_expenses() -> List[Expense]:
        """
            check if the expenses JSON file exist and Load expenses from a file
            :return: the content of the expenses JSON file
        """
        try:
            if os.path.isfile(EXPENSE_FILE_PATH) and os.access(EXPENSE_FILE_PATH, os.R_OK):
                with open(EXPENSE_FILE_PATH, 'r') as file:
                    data = json.load(file)
                    return [Expense.from_dict(expense) for expense in data]
            else:
                # if the file is missing, then create an empty file
                with open(EXPENSE_FILE_PATH, 'w') as file:
                    json.dump([], file)
                    return []
        except FileNotFoundError:
            return []

    def save_expenses(self) -> bool:
        """
            Save all expenses into the JSON file
            :return: boolean indicating if the process is successful or not
        """
        try:
            with open(EXPENSE_FILE_PATH, 'w') as file:
                expenses_dict = [expense.to_dict() for expense in self.expenses]
                json.dump(expenses_dict, file, indent=4)
                return True
        except Exception as ex:
            print('Error: ', ex)
            return False

    def get_next_id(self) -> int:
        """
            get the largest ID in the expenses JSON and increment it by 1 or returns 1
            :return: 1 if there are no expenses else return one + the largest ID
        """
        return max(expense.id for expense in self.expenses) + 1 if self.expenses else 1

    def get_expense_index(self, id: int) -> Union[None, int]:
        """
            This function searches through the list of expenses and
            returns the index of the expense that matches the given identifier.
            If no expense is found with the specified ID, it returns None.
            :param id: The identifier of the expense to find.
            :return: Union[None, int]: The index of the expense if found, otherwise None.
        """
        expense_index = None

        # find the expense
        for idx, expense in enumerate(self.expenses):
            if expense.id == id:
                expense_index = idx
                break

        return expense_index

    @staticmethod
    def amount_check(amount: int) -> None:
        if not isinstance(amount, int):
            raise ValueError('Amount must be an integer')
        elif amount < 0:
            raise ValueError('Amount must be a positive integer')

    def add_expense(self, description: str, amount: int) -> None:
        """
            Add a new expense to the list of expenses
            :param description: the description of the expense
            :param amount: the amount of the expense
        """

        try:
            self.amount_check(amount)

            new_expense = Expense(
                id=self.get_next_id(),
                description=description,
                amount=amount,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            self.expenses.append(new_expense)

            if self.save_expenses():
                print(f'Expense added successfully (ID: {new_expense.id})')

            return None

        except Exception as ex:
            print('Error: ', ex)
            return None

    def update_expense(self, id: int, description: Optional[str], amount: Optional[int]) -> None:
        """
            Update the details of an expense
            :param id: the identifier of the expense to update
            :param description: the new description of the expense
            :param amount: the new amount of the expense
        """
        try:
            expense_to_update: Optional[Expense] = None

            expense_index = self.get_expense_index(id)

            if isinstance(expense_index, int):
                expense_to_update = self.expenses[expense_index]

                if description:
                    expense_to_update.description = description

                elif amount:
                    self.amount_check(amount)
                    expense_to_update.amount = amount

                expense_to_update.updated_at = datetime.now().isoformat()

                self.expenses[expense_index] = expense_to_update

                if self.save_expenses():
                    print(f'Expense updated successfully (ID: {id})')
                    return None

        except Exception as ex:
            print('Error: ', ex)
            return None

    def delete_expense(self, id: int) -> None:
        """
            Delete an expense from the list of expenses
            :param id: the identifier of the expense to delete
        """
        try:
            expense_index = self.get_expense_index(id)

            if isinstance(expense_index, int):
                print('ID exist')
                del self.expenses[expense_index]

                if self.save_expenses():
                    print(f'Expense deleted successfully')
                    return None
            else:
                print('ID does not exist')
                return None

        except Exception as ex:
            print('Error: ', ex)
            return None

    def list_expenses(self) -> None:
        """
            List all expenses
        """
        if len(self.expenses) < 1:
            print('No expenses found')
            return

        print('ID\tDate\t\t\t\tDescription  Amount')
        for expense in self.expenses:
            print(f'{expense.id}\t{expense.created_at}\t{expense.description}\t\t${expense.amount}')

        return None

    def total_expense(self, month: Optional[int]) -> int:
        """
            Calculate the total amount of all expenses
            :return: the total amount of all expenses in the system
        """
        total = 0
        if month:
            total = sum(
                expense.amount for expense in self.expenses
                if datetime.fromisoformat(expense.created_at).month == month
            )
        else:
            total = sum(expense.amount for expense in self.expenses)

        print(f'Total expenses: ${total}')

