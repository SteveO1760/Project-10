class Budget:
    def __init__(self, expense_type):
        self.expense_type = expense_type
        self.expenses_dict = {}

    def add_expenses(self):
        while True:
            try:
                num_expenses = int(input(f"Enter number of {self.expense_type} expenses you want to add (integers only): "))
                break
            except ValueError:
                print("ERROR: Enter integers only.")

        print('Enter expenses in "Name Amount" format (e.g. Milk 10)')

        for i in range(num_expenses):
            while True:
                try:
                    name, cost = input(f"Enter expense #{i+1}: ").split()
                    self.expenses_dict[name] = float(cost)
                    break
                except ValueError:
                    print("Wrong format — try again (Milk 10).")

        self.write_to_file()

    def get_expenses(self):
        return sum(self.expenses_dict.values())

    def get_expenses_list(self):
        print(f"\nList of {self.expense_type} expenses:")
        for name, cost in self.expenses_dict.items():
            print(f"{name}: ${cost}")

    def write_to_file(self):
        with open("expenses.txt", "a") as f:
            f.write(f"[{self.expense_type}]\n")
            for name, cost in self.expenses_dict.items():
                f.write(f"{name}: {cost}\n")
            f.write("\n")
