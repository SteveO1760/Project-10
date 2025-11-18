import tkinter as tk, src.file_manager as fm
from tkinter import messagebox
from classes.classes_10 import Budget

app = tk.Tk(); app.title("BudgetBuddy"); app.geometry("280x250")
entries = {}

for t in ["Category","Name","Amount"]:
    tk.Label(app, text=t).pack()
    entries[t] = tk.Entry(app); entries[t].pack()

def save():
    c,n,a = entries["Category"].get(), entries["Name"].get(), entries["Amount"].get()
    if not (c and n and a): return messagebox.showerror("Error","All fields required")
    try: a=float(a)
    except: return messagebox.showerror("Error","Amount must be numeric")
    b=Budget(c); b.expenses_dict[n]=a; b.write_to_file()
    messagebox.showinfo("Saved","Expense added!")

tk.Button(app,text="Save Expense",bg="lightgreen",command=save).pack(pady=5)
tk.Button(app,text="View Expenses",bg="lightblue",command=lambda: messagebox.showinfo("All Expenses","".join(fm.load_expenses()))).pack()

app.mainloop()
