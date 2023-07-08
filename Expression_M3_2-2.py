import tkinter as tk
from tkinter import*

#กำหนดให้ m เป็นตัวแทนการใช้ lib tkinter
m = tk.Tk()

#กำหนด function clear เพื่อลบข้อมูลเมื่อทำการกด btn clear แล้วเปลี่ยนค่ากลับเป็น 0
def clear():
    global expression
    global lable_show_cal
    result="0"
    expression =""
    lable_show_cal.set(result)

#กำหนด function เมื่อทำการกดปุ่ม แล้วจะนำค่าจาก btn ที่เราได้กดไป มาเก็บไว้ใน expression 
#ปล้วเมื่อกด btn เพิ่มขึ้น จะนำค่าของ btn มาต่อกันใน expression เพื่อเพิ่มจำนวน
def press(number):
    global expression
    global lable_show_cal
    expression=expression+number
    lable_show_cal.set(expression)

#กำหนด font ที่ใช้งาน
m.option_add("font","consolas 30")
lable_show_cal= StringVar()
#กำหนดให้ lable_show_cal เป็น 0 เสมอเมื่อเปิด Program
lable_show_cal.set(0)
#กำหนดให้ตัวแปร expression ไม่มีค่าเมื่อเปิด Program เสมอ
expression=""

#กำหนดชื่อโปรแกรม
m.title('Main Win')

#กำหนด la คือ label เพื่อใช้ในการแสดงตัวเลข
la = Label(m,textvariable=lable_show_cal)

#กำหนดให้ la มา pack เก็บไว้เพื่อต่อไปหากมีคำสั่ง pack แล้ว la ที่ถูก pack ตัวแรก
#จะเป็น parent ในการเรียง ui ของ object อื่นๆ ต่อไปเรื่อยๆได้
la.pack()
btn0 = tk.Button(m,text='0',width=25,command=lambda:press("0"))
btn0.pack()
btn1 = tk.Button(m,text='1',width=25,command=lambda:press("1"))
btn1.pack()
btn2 = tk.Button(m,text='2',width=25,command=lambda:press("2"))
btn2.pack()
btn3 = tk.Button(m,text='3',width=25,command=lambda:press("3"))
btn3.pack()
btn4 = tk.Button(m,text='4',width=25,command=lambda:press("4"))
btn4.pack()
btn5 = tk.Button(m,text='5',width=25,command=lambda:press("5"))
btn5.pack()
btn6 = tk.Button(m,text='6',width=25,command=lambda:press("6"))
btn6.pack()
btn7 = tk.Button(m,text='7',width=25,command=lambda:press("7"))
btn7.pack()
btn8 = tk.Button(m,text='8',width=25,command=lambda:press("8"))
btn8.pack()
btn9 = tk.Button(m,text='9',width=25,command=lambda:press("9"))
btn9.pack()
btnp = tk.Button(m,text='+',width=25,command=lambda:press("+"))
btnp.pack()
btnx = tk.Button(m,text='-',width=25,command=lambda:press("-"))
btnx.pack()
btnxx = tk.Button(m,text='x',width=25,command=lambda:press("x"))
btnxx.pack()
btnharn = tk.Button(m,text='÷',width=25,command=lambda:press("÷"))
btnharn.pack()
btntaokub = tk.Button(m,text='=',width=25,command=lambda:press("="))
btntaokub.pack()
btncl = tk.Button(m,text='clear',width=25,command=clear)
btncl.pack()

#กำหนดให้ btn นี้เป็น stop เพื่อทำการหยุดโปรแกรม
btn = tk.Button(m,text='Stop',width=25,command=lambda:m.destroy())
btn.pack()

#กำหนดให้ loop โปรแกรมเรื่อยๆ ไม่มีที่สิ้นสุด
m.mainloop()