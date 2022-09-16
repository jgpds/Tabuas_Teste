from tkinter import * 

  
root = Tk()   
root.geometry("600x600")  
  
v1 = 0
idade_min = DoubleVar()
idade_max = DoubleVar() 


def show1():
    l1.pack_forget()
    l2.pack_forget()
    l5.place_forget()
    if idade_max.get() < idade_min.get():
        l5.config(text="**A idade máxima deve ser maior que a idade mínima**", font=("Courier", 10), fg = "red")
        l5.place(x=90 , y=30)
    else:
        sel = "Idade minima = " + str(idade_min.get())
        sel2 = "Idade máxima = " + str(idade_max.get()) 
        l1.config(text = sel, font =("Courier", 10))
        l2.config(text = sel2, font =("Courier", 10))
        l1.pack() 
        l2.pack()
        
  
s1 = Scale( root, variable = idade_min,  
           from_ = 0, to = 100,  
           orient = VERTICAL) 

s2 = Scale( root, variable = idade_max,  
           from_ = 0, to = 100,  
           orient = VERTICAL)
              
  
  
b1 = Button(root, text ="CALCULAR",  
            command = show1,  
            bg = "yellow")   
  
l1 = Label(root) 
l2 = Label(root)
l3 = Label(root)
l4 = Label(root)
l5 = Label(root)
l3.config(text = "Idade mínima", font=("Courier", 10))
l4.config(text = "Idade máxima", font=("Courier", 10))

  
s1.place(x=10, y=200) 
s2.place(x=10, y=320) 
l3.place(x=60, y=250)
l4.place(x=60, y=370)  
b1.pack(anchor = CENTER)
  
root.mainloop() 