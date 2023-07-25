from tkinter import *
import math
def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBox.get())/100,2))
    result = (float(textBoxWeight.get()) / math.pow(float(textBox.get()) / 100, 2))
    labelResult.configure(text= result)

    if result >= 30:
        labelResult.configure(text = "อ้วนมาก")
    elif result < 29.99 and result >= 25.00:
        labelResult.configure(text = "อ้วน")
    elif result < 24.99 and result >= 23.00:
        labelResult.configure(text = "น้ำหนักเกิน")
    elif result < 22.99 and result >= 18.6:
        labelResult.configure(text = "น้ำหนักปกติ เหมาะสม")
    elif result < 18.5:
        labelResult.configure(text = "ผอมเกินไป")
    else:
        labelResult.configure(text = "F")

mainWindow = Tk()
#ปุ่ม = ตัวแปร,ข้อความในปุ่ม,ย้อนกลับไปตัวแปรฟังชั่น
labelHight = Label(mainWindow,text = "ส่วนสูง (cm.)")
labelHight.grid(row=0,column=0)
textBox = Entry(mainWindow)
textBox.grid(row=0,column=1)
labelWeight = Label(mainWindow,text = "น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)
button = Button(mainWindow,text = "คำนวณ")
button.bind('<Button-1>',leftClickButton)
button.grid(row=2,column=0)
labelResult = Label(mainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2,column=1)



mainWindow.mainloop()