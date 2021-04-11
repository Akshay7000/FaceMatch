import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = ""
bg="#ffffff"
white="true"
def mode():
	global white,bg
	if (white == "true"):
		mode_btn.configure(text="Dark")
		btn1.configure(background='white',fg='black')
		btn2.configure(background='white',fg='black')
		btn3.configure(background='white',fg='black')
		btn4.configure(background='white',fg='black')
		
		btn5.configure(background='white',fg='black')
		btn6.configure(background='white',fg='black')
		btn7.configure(background='white',fg='black')
		btn8.configure(background='white',fg='black')
		
		btn9.configure(background='white',fg='black')
		btn10.configure(background='white',fg='black')
		btn11.configure(background='white',fg='black')
		btn12.configure(background='white',fg='black')
		
		btn13.configure(background='white',fg='black')
		btn14.configure(background='white',fg='black')
		btn15.configure(background='white',fg='black')
		btn16.configure(background='white',fg='black')
		white="false"
	else:
		mode_btn.configure(text="Light")
		btn1.configure(background='black',fg='white')
		btn2.configure(background='black',fg='white')
		btn3.configure(background='black',fg='white')
		btn4.configure(background='black',fg='white')
		
		btn5.configure(background='black',fg='White')
		btn6.configure(background='black',fg='White')
		btn7.configure(background='black',fg='White')
		btn8.configure(background='black',fg='White')
		
		btn9.configure(background='black',fg='White')
		btn10.configure(background='black',fg='White')
		btn11.configure(background='black',fg='White')
		btn12.configure(background='black',fg='White')
		
		btn13.configure(background='black',fg='White')
		btn14.configure(background='black',fg='White')
		btn15.configure(background='black',fg='White')
		btn16.configure(background='black',fg='White')
		
		
		white="true"
		
def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)

def btn_plus_clicked():
    global A
    global operator
    global val
    A =int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minus_clicked():
    global A
    global operator
    global val
    A =int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mul_clicked():
    global A
    global operator
    global val
    A =int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_clicked():
    global A
    global operator
    global val
    A =int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def c_clicked():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)

def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x= int((val2.split("+")[1]))
        C = A+x
        data.set(C)
        val= str(C)
    elif operator =="-":
        x= int((val2.split("-")[1]))
        C = A-x
        data.set(C)
        val= str(C)
    elif operator =="*":
        x= int((val2.split("*")[1]))
        C = A*x
        data.set(C)
        val= str(C)
    elif operator =="/":
        x= int((val2.split("/")[1]))
        if x==0:
            messagebox.showerror("Error","Division by 0 Not Supported")
            A= ""
            val= ""
            data.set(val)
        else:
            C = int(A/x)
            data.set(C)
            val = str(C)


###########################################################################

root = tkinter.Tk()
root.geometry("250x400+300+300")
#root.resizable(0,0)
root.title("Calculater")
root.bind("<Escape>", exit)
#root.overrideredirect(True) 
data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 22),
    textvariable = data,
    background = "#000000",
    fg = bg,
	)
lbl.pack(expand = True, fill = "both",)
mode_btn = Button(
    text = "Light",
    font = ("Veranda", 10),
    relief = GROOVE,
    border = 0,
    command = mode,
	bg="#000000",
	fg=bg
	)
mode_btn.place(x = 0, y = 0)

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand = True, fill = "both",)

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both",)

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both",)

btnrow4 = Frame(root, bg=bg)
btnrow4.pack(expand = True, fill = "both",)


btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = btn_1_isclicked,
	bg="#000000",
	fg=bg
	)
btn1.pack(side= LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = btn_2_isclicked,
	bg="#000000",
	fg=bg
)
btn2.pack(side= LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = btn_3_isclicked,
	bg="#000000",
	fg=bg
)
btn3.pack(side= LEFT, expand = True, fill = "both",)

btn4 = Button(
    btnrow1,
    text = "+",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = btn_plus_clicked,
	bg="#000000",
	fg=bg
)
btn4.pack(side= LEFT, expand = True, fill = "both",)



btn5 = Button(
    btnrow2,
    text = "4",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = btn_4_isclicked,
	bg="#000000",
	fg=bg
)
btn5.pack(side= LEFT, expand = True, fill = "both",)

btn6 = Button(
    btnrow2,
    text = "5",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = btn_5_isclicked,
	bg="#000000",
	fg=bg
)
btn6.pack(side= LEFT, expand = True, fill = "both",)

btn7 = Button(
    btnrow2,
    text = "6",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = btn_6_isclicked,
	bg="#000000",
	fg=bg
)
btn7.pack(side= LEFT, expand = True, fill = "both",)

btn8 = Button(
    btnrow2,
    text = "-",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = btn_minus_clicked,
	bg="#000000",
	fg=bg
)
btn8.pack(side= LEFT, expand = True, fill = "both",)



btn9 = Button(
    btnrow3,
    text = "7",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = btn_7_isclicked,
	bg="#000000",
	fg=bg
)
btn9.pack(side= LEFT, expand = True, fill = "both",)

btn10 = Button(
    btnrow3,
    text = "8",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = btn_8_isclicked,
	bg="#000000",
	fg=bg
)
btn10.pack(side= LEFT, expand = True, fill = "both",)

btn11 = Button(
    btnrow3,
    text = "9",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = btn_9_isclicked,
	bg="#000000",
	fg=bg
)
btn11.pack(side= LEFT, expand = True, fill = "both",)

btn12 = Button(
    btnrow3,
    text = "*",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = btn_mul_clicked,
	bg="#000000",
	fg=bg
)
btn12.pack(side= LEFT, expand = True, fill = "both",)




btn13 = Button(
    btnrow4,
    text = "C",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = c_clicked,
	bg="#000000",
	fg=bg
)
btn13.pack(side= LEFT, expand = True, fill = "both",)

btn14 = Button(
    btnrow4,
    text = "0",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = btn_0_isclicked,
	bg="#000000",
	fg=bg
)
btn14.pack(side= LEFT, expand = True, fill = "both",)

btn15 = Button(
    btnrow4,
    text = "=",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command= result,
	bg="#000000",
	fg=bg
)
btn15.pack(side= LEFT, expand = True, fill = "both",)

btn16 = Button(
    btnrow4,
    text = "/",
    font = ("Veranda", 22),
    relief = GROOVE,
    border = 0,
    command = btn_div_clicked,
	bg="#000000",
	fg=bg
)
btn16.pack(side= LEFT, expand = True, fill = "both",)

root.mainloop()