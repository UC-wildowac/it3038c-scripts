from tkinter import *

expression = ""

def press(num):

	global expression

	expression = expression + str(num)

	equation.set(expression)

def equalpress():

	try:

		global expression

		total = str(eval(expression))

		equation.set(total)

		expression = ""

	except:

		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")

if __name__ == "__main__":

	gui = Tk()

	gui.configure(background="Black")

	gui.title("Simple Calculator")

	gui.geometry("500x500")

	equation = StringVar()

	expression_field = Entry(gui, textvariable=equation)

	expression_field.grid(columnspan=8, ipadx=200)

	button1 = Button(gui, text=' 1 ', fg='black', bg='Blue',
					command=lambda: press(1), height=5, width=16)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='red',
					command=lambda: press(2), height=5, width=16)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='White',
					command=lambda: press(3), height=5, width=16)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='purple',
					command=lambda: press(4), height=5, width=16)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='orange',
					command=lambda: press(5), height=5, width=16)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='pink',
					command=lambda: press(6), height=5, width=16)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='green',
					command=lambda: press(7), height=5, width=16)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='yellow',
					command=lambda: press(8), height=5, width=16)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='blue',
					command=lambda: press(9), height=5, width=16)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='red',
					command=lambda: press(0), height=5, width=16)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='yellow',
				command=lambda: press("+"), height=5, width=16)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='purple',
				command=lambda: press("-"), height=5, width=16)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='orange',
					command=lambda: press("*"), height=5, width=16)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='pink',
					command=lambda: press("/"), height=5, width=16)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='green',
				command=equalpress, height=5, width=16)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='white',
				command=clear, height=5, width=16)
	clear.grid(row=5, column='1')

	Decimal= Button(gui, text='.', fg='black', bg='blue',
					command=lambda: press('.'), height=5, width=16)
	Decimal.grid(row=6, column=0)
	
	gui.mainloop()
