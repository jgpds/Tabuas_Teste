from sysconfig import is_python_build
from textwrap import fill
from tkinter import *
from tkinter.font import BOLD
from turtle import bgcolor, title 
from TabuasDemoivreEtc import w_df_gui, df_gui
from auxilio_funcs import standard
import matplotlib.pyplot as plt


root = Tk()   
root.title("TEORIA ATUARIAL 1: Calculadora de funções biométricas")
root.geometry("900x600")  
root.config(bg='#3c403d')
# settando o grid
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=2)
root.rowconfigure(2, weight=2)

v1 = 0
idade_min = DoubleVar()
idade_max = DoubleVar() 

# Botão de opções
standard.pop(0) #removendo 'x' da lista
my_list = standard
options = StringVar(root)
options.set(my_list[0]) # default value

om1 = OptionMenu(root, options, *my_list) # my_list = ['x', 'q_x', ...] #*my_list = 'x', 'q_x', ...
om1.configure(bg='#303330', height= 1, width=2, fg = '#e0dcd1', activebackground='#6a017a')
om1["highlightthickness"] = 0 # deixa sem borda branca
om1["menu"].config(bg="#303330", fg="#e0dcd1") # muda a cor quando clica no optionmenu
om1.place(x = 20, y = 10)

def imprimirOpcao(df_aux, idade_min, idade_max):
    plt.clf()
    opcao = options.get()
    l7 = Label(root, text=f'Opção selecionada:   {opcao}', bg='#3c403d', font=("Ubuntu", 10), fg = '#e0dcd1')
    l7.place(x=80, y=10)
    if opcao == 'l_x' and len(df_aux) == 1:
        print(df_aux)
        label_interpretacao.config(text=f"Interpretação {opcao}:\nNúmero de vivos a idade exata {idade_min} = {df_aux.loc[idade_min, 'l_x']:.2f}", font=("Ubuntu", 12), bg='black', fg = '#e0dcd1', bd=9, relief='raised')
        label_interpretacao.place(x=260, y=150, height=400, width=600)
    elif opcao == 'l_x' and len(df_aux) != 1:
        label_interpretacao.config(text=f"Não há interpretação de {opcao} nesse caso =(\nPorém é possível ver seu comportamento no gráfico!", font=("Ubuntu", 12), bg='black', fg = '#e0dcd1', relief='raised', bd=9)
        label_interpretacao.place(x=260, y=150, height=400, width=600)
    elif opcao == 'd_x':
        label_interpretacao.config(text=f"Interpretação {idade_min}_d_{idade_max}:\nnumero de mortos entre as idades {idade_min} e {idade_max} = {df_aux.loc[idade_min,'l_x']-df_aux.loc[idade_max,'l_x']:.2f}\n\n\nATENÇÃO! O gráfico corresponde ao comportamento de x+1_d_x sendo x a idade mínima\nindependente do intervalo inserido.", font=("Ubuntu", 12), bg='black', fg = '#e0dcd1', bd=9, relief='raised')
        label_interpretacao.place(x=260, y=150, height=400, width=600)
    elif opcao == 'q_x':
        label_interpretacao.config(text=f"Interpretação {idade_min}_q_{idade_max}:\nprobabilidade de morrer entre as idades {idade_min} e {idade_max} = {((df_aux.loc[idade_min,'l_x']-df_aux.loc[idade_max,'l_x'])/df_aux.loc[idade_min, 'l_x']):.8f}", font=("Ubuntu", 12), bg='black', fg = '#e0dcd1', relief='raised', bd=9)
        label_interpretacao.place(x=260, y=150, height=400, width=600)
    elif opcao == 'p_x':
        label_interpretacao.config(text=f"Interpretação {opcao}:\nprobabilidade de sobreviver entre as idades {idade_min} e {idade_max} = {(1-((df_aux.loc[idade_min,'l_x']-df_aux.loc[idade_max,'l_x'])/df_aux.loc[idade_min, 'l_x'])):.8f}", font=("Ubuntu", 12), bg='black', fg = '#e0dcd1', relief='raised', bd=9)
        label_interpretacao.place(x=260, y=150, height=400, width=600)
    elif opcao == 'L_x':
        label_interpretacao.config(text=f"Interpretação {opcao}:\nNúmero de anos vividos pelo grupo entre as idades {idade_min} e {idade_max} = {(df_aux.loc[idade_min, 'l_x']+df_aux.loc[idade_max, 'l_x'])/2:.8f}", font=("Ubuntu", 12), bg='black', fg = '#e0dcd1', relief='raised', bd=9)
        label_interpretacao.place(x=260, y=150, height=400, width=600)
    elif opcao == 'T_x':
        label_interpretacao.config(text=f"Interpretação {opcao}:\nnumero total de anos vividos pelo grupo entre as idades {idade_min} e w({idade_max} = {(df_aux.loc[idade_min, 'l_x']+df_aux.loc[idade_max, 'l_x'])/2:.8f}\n\n**Idade máxima deve ser a última idade da tábua) = ", font=("Ubuntu", 12), bg='black', fg = '#e0dcd1', relief='raised', bd=9)
        label_interpretacao.place(x=260, y=150, height=400, width=600)
    elif opcao == 'e_x':
        label_interpretacao.config(text=f"Interpretação {opcao}:\nExpectativa de vida a idade {idade_min} =", font=("Ubuntu", 12), bg='black', fg = '#e0dcd1', relief='raised', bd=9)
        label_interpretacao.place(x=260, y=150, height=400, width=600)
    elif opcao == 'u_x':
        label_interpretacao.config(text=f"Interpretação {opcao}:\nTaxa instantanea de mortalidade na idade x = ", font=("Ubuntu", 12), bg='black', fg = '#e0dcd1', relief='raised', bd=9)
        label_interpretacao.place(x=260, y=150, height=400, width=600)
    elif opcao == 'm_x':
        label_interpretacao.config(text=f"Interpretação {opcao}:\nTaxa central de mortalidade = ", font=("Ubuntu", 12), bg='black', fg = '#e0dcd1', relief='raised', bd=9)
        label_interpretacao.place(x=260, y=150, height=400, width=600)
    print(df_aux[opcao])
    plt.xlabel("Idade")
    plt.ylabel(f"{opcao}")
    plt.title(f"Idade vs {opcao}")
    plt.plot(df_aux['x'], df_aux[opcao], '-ok')
    plt.grid()
    plt.show()


def calculate_results(idade_min, idade_max):
    df_aux = df_gui.loc[idade_min:idade_max]
    print(df_aux)
    return df_aux 


def show1():
    l1.place_forget()
    l2.place_forget()
    l5.place_forget()
    l6.place_forget()
    label_interpretacao.place_forget()
    if idade_max.get() < idade_min.get():
        l5.config(text="**AVISO: A idade máxima deve ser maior ou igual que a idade mínima**".upper(), font=("Ubuntu", 14, 'bold'), fg = "#8f0101", bg='#3c403d', justify=CENTER)
        l5.place(x=100 , y=70)
        
    elif idade_max.get() == idade_min.get():
        df_aux = calculate_results(int(idade_min.get()), int(idade_max.get()))
        l6.config(text=f"Idade = {int(idade_min.get())}", font=("Ubuntu", 10), bg='#3c403d', fg = '#e0dcd1')
        l6.place(x = 400, y = 50)  
        imprimirOpcao(df_aux, int(idade_min.get()), int(idade_max.get()))      
    else:
        df_aux = calculate_results(int(idade_min.get()), int(idade_max.get()))
        sel = "Idade minima = " + str(int(idade_min.get()))
        sel2 = "Idade máxima = " + str(int(idade_max.get())) 
        l1.config(text = sel, font =("Ubuntu", 10), bg='#3c403d', fg = '#e0dcd1')
        l2.config(text = sel2, font =("Ubuntu", 10), bg='#3c403d', fg = '#e0dcd1')
        l1.place(x = 400, y = 50) 
        l2.place(x = 400, y = 70)
        imprimirOpcao(df_aux, int(idade_min.get()), int(idade_max.get()))
 
  
s1 = Scale( root, variable = idade_min,  
           from_ = 0, to = w_df_gui,  
           orient = VERTICAL, bg='#303330', fg = '#e0dcd1', highlightthickness=1, highlightbackground='black', activebackground="#6a017a") 

s2 = Scale( root, variable = idade_max,  
           from_ = 0, to = w_df_gui,  
           orient = VERTICAL, bg='#303330', fg = '#e0dcd1', highlightthickness=1, highlightbackground='black', activebackground="#6a017a")

              
  
  
b1 = Button(root, text ="CALCULAR",  
            command = show1,  
            bg = '#303330', width=20, font=('bold'), fg = '#e0dcd1', borderwidth= 3, activebackground="#6a017a")   
  
l1 = Label(root) 
l2 = Label(root)
l3 = Label(root)
l4 = Label(root)
l5 = Label(root)
l6 = Label(root)
label_interpretacao = Label(root)
l3.config(text = "Idade mínima", font=("Ubuntu", 10), bg='#3c403d', fg = '#e0dcd1')
l4.config(text = "Idade máxima", font=("Ubuntu", 10), bg='#3c403d', fg = '#e0dcd1')

  
s1.place(x=20, y = 200, height= 160) 
s2.place(x=20, y = 400, height= 160) 
l3.place(x=75, y = 250)
l4.place(x=75, y= 450)  
b1.place(x=350, y= 10)
  
root.mainloop() 

# Fazer uma função calculate_results(idade_min, idade_max) que retorna uma lista com as respostas das probabilidades de l_x, q_x etc.... para determinada idades