import os

FILE_PATH = "expenses.txt"

def save_line(text):
    with open(FILE_PATH, "a") as f:
        f.write(text + "\n")


def load_expenses():
    if not os.path.exists(FILE_PATH):
        return ["No expenses found."]

    with open(FILE_PATH, "r") as f:
        return f.readlines()
