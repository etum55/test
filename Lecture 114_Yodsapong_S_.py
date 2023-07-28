
from currency_converter import CurrencyConverter
from datetime import date # datetime works too
c = CurrencyConverter()
d = date

from tkinter import *

def leftClickButton_1(event):
    conversion_1 = c.convert(textBox_amount.get(),textBox.get(),textBox1.get())
    print(conversion_1)
    labelResult.configure(text = conversion_1)

def leftClickButton_2(event):
    from currency_converter import CurrencyConverter
    from datetime import date
    c = CurrencyConverter()

    conversion_2 = c.convert(textBox_amount.get(),textBox.get(),(textBox1.get()),date=date(int(textBoxDateYear.get()),int(textBoxDateMonth.get()),int(textBoxDateDay.get())))
    print(conversion_2)
    labelResult1.configure(text=conversion_2)


mainWindow = Tk()
#ชื่อ
label = Label(mainWindow,text = "Currency Converter",width=15,fg = "red",bg = "yellow",font=("Helvetica",15),anchor = "n").grid(row=0,column=1)
#หัวข้อและช่องใส่
labelConverter = Label(mainWindow,text = "Currency 1")
labelConverter.grid(row=2,column=0)
textBox = Entry(mainWindow)
textBox.grid(row=2,column=1)
label = Label(mainWindow,text = "to")
label.grid(row=3,column=0)
labelConverter1 = Label(mainWindow,text = "Currency 2")
labelConverter1.grid(row=4,column=0)
textBox1 = Entry(mainWindow)
textBox1.grid(row=4,column=1)
labelamount = Label(mainWindow,text = "Amount")
labelamount.grid(row=5,column=0)
textBox_amount = Entry(mainWindow)
textBox_amount.grid(row=5,column=1)
#ปุ่ม
button = Button(mainWindow,text = "Calculate")
button.bind('<Button-1>',leftClickButton_1)
button.grid(row=6,column=0)
labelResult = Label(mainWindow,text = "Result")
labelResult.grid(row=6,column=1)

#ชื่อ
label = Label(mainWindow,text = "Date").grid(row=7,column=1)

#หัวข้อและช่องใส่
labelDate = Label(mainWindow,text = "Year")
labelDate.grid(row=8,column=0)
textBoxDateYear = Entry(mainWindow)
textBoxDateYear.grid(row=8,column=1)
labelDate = Label(mainWindow,text = "Month")
labelDate.grid(row=9,column=0)
textBoxDateMonth = Entry(mainWindow)
textBoxDateMonth.grid(row=9,column=1)
labelDate = Label(mainWindow,text = "Day")
labelDate.grid(row=10,column=0)
textBoxDateDay = Entry(mainWindow)
textBoxDateDay.grid(row=10,column=1)

#ปุ่ม
button2 = Button(mainWindow,text = "Calculate")
button2.bind('<Button-1>',leftClickButton_2)
button2.grid(row=11,column=0)
labelResult1 = Label(mainWindow,text = "Result")
labelResult1.grid(row=11,column=1)



mainWindow.mainloop()