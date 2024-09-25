# -*- coding: cp1251 -*-
import math 
from tkinter import * 

def add():  
    res = "{}".format(txt.get())
    res2="{}".format(txt2.get())

    hait_stoika=float(res)
    diametr_trubi=float(res2)
   
    
    arcTG=float(math.atan(100/(60.1-hait_stoika))) * (180/math.pi)
    print (arcTG)
    a=float (180 - 2 * arcTG)
    sin_ugla_a=float( math.sin((a * math.pi/180)))
    print ( sin_ugla_a)
    Radius_giba=float (100 / (sin_ugla_a))
    Radius_giba=Radius_giba-diametr_trubi/2
    Radius_giba=round(Radius_giba,2)
    
    print ("radius",Radius_giba)
    print ("diametr",Radius_giba*2)

    lbl1.configure(text=f"Radius_giba={Radius_giba}")
    lbl2.configure(text=f"Diametr_giba={Radius_giba*2}")

    




window = Tk()  
window.title("Калькулятор Радиусов")  
lbl1 = Label(window, text="Radius_giba")  
lbl1.grid(column=10, row=200)  

lbl2 = Label(window, text="Diametr_giba")  #
lbl2.grid(column=10, row=250)  

Titl_r=Label(window, text="H")
Titl_r.grid(column=0, row=0)  
Titl_D=Label(window, text="D")  
Titl_D.grid(column=0, row=10) 

txt = Entry(window, width=10)
txt.grid(column=10, row=0)

txt2 = Entry(window, width=10)
txt2.grid(column=10, row=10)

window.geometry('250x250')


btn = Button(window, text="Произвести расчет!",command=add)  
btn.grid(column=10, row=20)  

window.mainloop()
