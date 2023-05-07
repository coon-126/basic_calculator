import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title('Calculator')

        # Create display widget
        self.display = tk.Entry(master, width=30, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)

        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)

        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)

        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('=', 4, 2)
        self.create_button('+', 4, 3)

        self.create_button('C', 5, 0)
        self.create_button('(', 5, 1)
        self.create_button(')', 5, 2)
        self.create_button('^', 5, 3)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=7, height=2, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Error')
        elif text == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, text)


root = tk.Tk()
calc = Calculator(root)
root.mainloop()