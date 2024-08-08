from currency_converter import CurrencyConverter
import tkinter as tk

c = CurrencyConverter()

#print(c.convert(200, "INR", "USD"))

common_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CAD', 'AUD', 'NZD', 'CNY', 
'SEK', 'NOK', 'DKK', 'SGD', 'HKD', 'KRW', 'INR', 'BRL', 'RUB', 
'ZAR', 'TRY', 'MXN', 'PLN', 'THB', 'IDR', 'MYR', 'PHP', 'TWD', 
'HUF', 'CZK', 'ILS', 'CLP', 'PKR', 'AED', 'SAR']

def convert_money():
    amount = int(entry.get())
    c1 = from_var.get()
    c2 = to_var.get()
    result = c.convert(amount, c1, c2)
    result_label = tk.Label(box, text=result, font="Arial 10 bold").place(x=250, y=225)
    


box = tk.Tk()
box.geometry('500x300')
box.title("Currency Converter")

label_main = tk.Label(box, text="Currency Converter", font="Arial 25 bold").place(x=100, y=20)
label1 = tk.Label(box, text="Choose currency to convert from:", font="Arial 10 bold").place(x=50, y=75)
label2 = tk.Label(box, text="Choose currency to convert to:", font="Arial 10 bold").place(x=50, y=125)

from_var = tk.StringVar(box)
from_var.set("INR")
from_menu = tk.OptionMenu(box, from_var, *common_currencies)

to_var = tk.StringVar(box)
to_var.set("USD")
to_menu = tk.OptionMenu(box, to_var, *common_currencies)

label3 = tk.Label(box, text="Enter your amount here:", font="Arial 10 bold").place(x=50, y=175)
entry = tk.Entry(box)

button = tk.Button(box, text="Convert", command=convert_money).place(x=200, y=250)

label4 = tk.Label(box, text="The converted amount:", font="Arial 10 bold").place(x=50, y=225)

from_menu.place(x=275, y=70)
to_menu.place(x=275, y=120)
entry.place(x=250, y=177)
box.mainloop()