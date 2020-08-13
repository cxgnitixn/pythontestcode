from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Calculator')
content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=1, relief='sunken',width=250, height=250)
    
def inpadd(adsign):
    name.insert(10,adsign)
    return

def insubt(subsign):
    name.insert(10,subsign)
    return

def mult(mulsign):
    name.insert(10,mulsign)
    return

def divs(divsign):
    name.insert(10,divsign)
    return

def inpshow():
    inp = name.get()
    se = eval(str(inp))
    print(se)

        
usr = int
name = ttk.Entry(textvariable=usr)
equ = ttk.Button(text='=', command=inpshow)
ads = ttk.Button(text='+', command=lambda:inpadd('+'))
subt = ttk.Button(text='-', command=lambda:insubt('-'))
mul = ttk.Button(text='*', command=lambda:mult('*'))
div = ttk.Button(text='/', command=lambda:divs('/'))

content.grid(column=0, row=0)
name.grid(column=4, row=2)
equ.grid(column=4, row=3)
ads.grid(column=4, row=4)
subt.grid(column=4, row=5)
mul.grid(column=4, row=6)
div.grid(column=4, row=7)
