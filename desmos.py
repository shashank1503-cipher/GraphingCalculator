import numpy as np
import matplotlib.pyplot as pl
from tkinter import *
import math
def plot():
    def lemm(eqn):
        eqn = eqn.replace("^","**")
        eqn = eqn.replace(".","*")
        y = eqn.split()
        z = ""
        for i in y:
            if i.isalnum() and not i.isdigit():
                for j in i:
                    if j.isdigit():
                        z+= j + "*"
                    else:
                        z+=j
            else:
                z+= i
        return z
    def checkFunction(eqn):
        listoffunction = ["sin","cos","tan","sec","cosec","log","ln","e","floor","ceil","mod"]
        dicoffunction = {"sin" : "np.sin","cos" : "np.cos","tan" : "np.tan","sec":"1/np.cos","cosec" : "1/np.sin","log" : "np.log10","ln" : "np.log","e":"2.7182818284590452353602875","floor": "np.floor","ceil" : "np.ceil","mod" : "np.mod"}
        if "arcsin" in eqn :
            eqn = eqn.replace("arcsin","np.arcsin")
            if "arccos" in eqn:
                eqn = eqn.replace("arccos","np.arccos")
                if "arctan" in eqn:
                    eqn = eqn.replace("arctan","np.arctan")

        else:
            for i in listoffunction:
                if i in eqn:
                    eqn = eqn.replace(i,dicoffunction.get(i))
        return eqn
    def TwoVar(a,b,c,d):
        z = eqn.split("=")
        for i in a:
            for j in b :
                 lhs = z[0]
                 rhs = z[1]
                 lhs = lhs.replace("x","(" + str(i) + ")")
                 lhs = lhs.replace("y","(" + str(j) + ")")
                 
                 rhs = rhs.replace("x","(" + str(i) + ")")
                 rhs = rhs.replace("y","(" + str(j) + ")")
                 if eval(lhs) == eval(rhs) :
                     c = np.append(c,i)
                     d = np.append(d,j)
        pl.plot(c,d)
        pl.grid(True)
        pl.show()
    def OneVar(a,b):
        for i in a:
            y = eqn.replace("x","(" + str(i) + ")" )
            b = np.append(b,eval(y))
        pl.plot(a,b)
        pl.grid(True)
        pl.show()
    
    eqn = eq.get()
    eqn = lemm(eqn)
    eqn = checkFunction(eqn)
    
    Xaxis = np.arange(-10,10,0.1)
    Yaxis = np.arange(-10,10,0.1)
    _x = np.array([])
    _y = np.array([])
    if 'y' in eqn:
        TwoVar(Xaxis,Yaxis,_x,_y)
        
    else:
        OneVar(Xaxis,_x)
    
    

    
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background = "White")
    gui.geometry("1024x768")
    gui.title("Desmos")
    Label(gui,text = "desmos",font = "Consolas 30",fg = "Green",bg = "White").place(x = 50,y = 10)
    Label(gui,text = "f(x) =",font = "Consolas 20",fg = "Green",bg ="White").place(x = 350,y = 150)
    eq = Entry(gui)
    eq.place(x = 450, y = 160)
    button1 =Button(gui,text = "Plot",fg = "white" ,bg = "Light Green",command = plot,highlightbackground ="Black",highlightthickness = 2)
    button1.place(x = 350,y = 250,height = 25,width = 150)
    gui.mainloop()
    
