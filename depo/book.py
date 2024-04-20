import tkinter as tk
import tester

root = tk.Tk()
root.title('Programme')
root.geometry('800x500')


choice = 2


def Euro():
    global choice
    choice = 2
    euro.configure(state='active')
    dollar.configure(state='normal')


def Dollar():
    global choice
    choice = 3
    dollar.configure(state='active')
    euro.configure(state='normal')


def Temperature():
    l1.configure(text="Температура сьогодні:")
    input.configure(state='disabled')
    l2.configure(text=tester.tempparser6.Result[2])
    input.grid_forget()
    euro.grid_forget()
    dollar.grid_forget()


def Money():
    l1.configure(text="Введіть число (гривні):")
    l2.configure(text='')
    input.grid(columnspan=16, column=3)
    euro.grid(column=4, row=7)
    dollar.grid(column=7, row=7)
    if input.cget("state") == 'disabled':
        input.configure(state='normal')
    else:
        value = float(input.get())
        if choice == 2:
            l2.configure(text=f"{value / tester.nbuparser.Result[choice]} євро")
        if choice == 3:
            l2.configure(text=f"{value / tester.nbuparser.Result[choice]} доллари")


c = tk.Label(width=20, height=2)
c.grid(row=1, column=1)
b1 = tk.Button(height=2, width=10, bg='light gray', text='Курс Валют', command=Money)
b1.grid(row=2, column=4)
c1 = tk.Label(width=50, height=2)
c1.grid(row=1, column=5)
b2 = tk.Button(height=2, width=10, bg='light gray', text='Температура', command=Temperature)
b2.grid(row=2, column=7)
c2 = tk.Label(width=10, height=4)
c2.grid(row=3, column=1)

l1 = tk.Label(text='Температура сьогодні:', font=140)
l1.grid(columnspan=16, column=3)
l2 = tk.Label(text=tester.tempparser6.Result[2], font=140)
l2.grid(columnspan=16, column=3)
input = tk.Entry(state='disabled')

euro = tk.Button(width=6, height=2, text='Євро', command=Euro, state='active', activeforeground='gray')
dollar = tk.Button(width=6, height=2, text='Доллар', command=Dollar, state='normal', activeforeground='gray')


root.mainloop()
