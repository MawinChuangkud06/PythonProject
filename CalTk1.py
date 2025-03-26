import tkinter

def calculate(event):
    try:
        result = eval(entry.get())
        entry.delete(0, tkinter.END)
        entry.insert(tkinter.END, str(result))
    except Exception:
        entry.delete(0, tkinter.END)
        entry.insert(tkinter.END, "Error")

def clear():
    entry.delete(0, tkinter.END)

tk = tkinter.Tk()
tk.title("Calculator")

entry = tkinter.Entry(tk, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tkinter.Button(tk, text=button, width=5, height=2, command=lambda: calculate(None)).grid(row=row_val, column=col_val, padx=0, pady=0)
    elif button == 'C':
        tkinter.Button(tk, text=button, width=5, height=2, command=clear).grid(row=row_val, column=col_val, padx=0, pady=0)
    else:
        tkinter.Button(tk, text=button, width=5, height=2, command=lambda b=button: entry.insert(tkinter.END, b)).grid(row=row_val, column=col_val, padx=0, pady=0)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.mainloop()
