
import tkinter as tk

root= tk.Tk()

# global variables
math=""
fnum= 0.0

# Functions
def button_click(num):
    current_num= entry.get()
    entry.delete(0, "end")
    entry.insert(0, str(current_num) + str(num))
    return

def button_AC():
    entry.delete(0, "end")
    return

def button_clr():
    num= entry.get()
    fnum= int(num)
    entry.delete(0, "end")
    entry.insert(0, str(fnum)[: -1])
    return


def button_add():
    global fnum
    global math
    num1= entry.get()
    fnum= float(num1)
    entry.delete(0, "end")
    math= "addition"
    return

def button_sub():
    global fnum
    global math
    num1= entry.get()
    fnum= float(num1)
    entry.delete(0, "end")
    math= "subtraction"
    return

def button_mul():
    global fnum
    global math
    num1= entry.get()
    fnum= float(num1)
    entry.delete(0, "end")
    math= "multiplication"
    return

def button_div():
    global fnum
    global math
    num1= entry.get()
    fnum= float(num1)
    entry.delete(0, "end")
    math= "division"
    return

def button_rem():
    global fnum
    global math
    num1= entry.get()
    fnum= float(num1)
    entry.delete(0, "end")
    math= "reminder"
    return

def button_equal():
    global fnum
    num2= entry.get()
    num= float(num2)
    entry.delete(0, "end")

    if math == "addition":
        entry.insert(0, fnum + num)
        return

    elif math == "subtraction":
        entry.insert(0, fnum - num)
        return

    elif math == "multiplication":
        entry.insert(0, fnum * num)
        return

    elif math == "division":
        entry.insert(0, fnum / num)
        return

    elif math == "reminder":
        entry.insert(0, fnum % num)
        return

    return


root.title("Calculator App")

# Entry Widget
entry= tk.Entry( root, width= 25, borderwidth= 5, bg= 'grey')
entry.grid(row=0, column=0, columnspan= 3)

# Creating Buttons
button_1= tk.Button(root, text= '1', padx=20, pady= 5, command= lambda: button_click(1))
button_2= tk.Button(root, text= '2', padx=20, pady= 5, command= lambda: button_click(2))
button_3= tk.Button(root, text= '3', padx=20, pady= 5, command= lambda: button_click(3))
button_4= tk.Button(root, text= '4', padx=20, pady= 5, command= lambda: button_click(4))
button_5= tk.Button(root, text= '5', padx=20, pady= 5, command= lambda: button_click(5))
button_6= tk.Button(root, text= '6', padx=20, pady= 5, command= lambda: button_click(6))
button_7= tk.Button(root, text= '7', padx=20, pady= 5, command= lambda: button_click(7))
button_8= tk.Button(root, text= '8', padx=20, pady= 5, command= lambda: button_click(8))
button_9= tk.Button(root, text= '9', padx=20, pady= 5, command= lambda: button_click(9))
button_0= tk.Button(root, text= '0', padx=20, pady= 5, command= lambda: button_click(0))

button_plus= tk.Button(root, text= '+', padx=20, pady= 5, command= button_add)
button_sub= tk.Button(root, text= '-', padx=20.5, pady= 5, command= button_sub)
button_mul= tk.Button(root, text= '*', padx=25, pady= 5, command= button_mul)
button_div= tk.Button(root, text= '/', padx=25, pady= 5, command= button_div)
button_clr= tk.Button(root, text= 'Clr', padx=20, pady= 5, command= button_clr)
button_AC= tk.Button(root, text= 'AC', padx=20, pady= 5, command= button_AC)
button_rem= tk.Button(root, text= '%', padx=47, pady= 5, command= button_rem)
button_equal= tk.Button(root, text= '=', padx=50, pady= 5, command= button_equal)



# Placing the buttons on the GUI
button_1.grid(row=1, column= 0)
button_2.grid(row=1, column= 1)
button_3.grid(row=1, column= 2)
button_4.grid(row=2, column= 0)
button_5.grid(row=2, column= 1)
button_6.grid(row=2, column= 2)
button_7.grid(row=3, column= 0)
button_8.grid(row=3, column= 1)
button_9.grid(row=3, column= 2)
button_0.grid(row=4, column= 1)

button_plus.grid(row=4, column= 0)
button_sub.grid(row=4, column= 2)
button_clr.grid(row=1, column= 3)
button_AC.grid(row=2, column= 3)
button_rem.grid(row=5, column= 0, columnspan= 2)
button_equal.grid(row=5, column= 2, columnspan= 2)
button_mul.grid(row=4, column= 3)
button_div.grid(row=3, column= 3)




# Start the program
root.mainloop()