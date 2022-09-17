#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from auxilio_funcs import Tables

df_DeMoivre = pd.read_excel('Garcia e Simoes.xlsx', sheet_name=1)
df_DeMoivre


# In[2]:


df_Garcia_Simoes = pd.read_excel('Garcia e Simoes.xlsx', sheet_name=0)
df_Garcia_Simoes


# In[3]:


df_Gompertz = pd.read_excel('Garcia e Simoes.xlsx', sheet_name=2)
df_Gompertz


# In[4]:


df_Makeham = pd.read_excel('Garcia e Simoes.xlsx', sheet_name=3)
df_Makeham


# In[5]:


# idade = int(input("Escolha uma idade: "))


# In[6]:


import matplotlib.pyplot as plt
# plt.xlabel("Idade")
# plt.ylabel("s(x)")
# plt.title("Garcia s(x) vs Gompertz s(x)")
# plt.plot(df_Garcia_Simoes['x'], df_Garcia_Simoes['s(x)'], 'g-', label = 'Garcia e Simoes')
# plt.plot(idade, df_Garcia_Simoes.loc[idade,'s(x)'], 'go',label=f"s({idade}) = {df_Garcia_Simoes.loc[idade,'s(x)']:.3f}")
# plt.plot(df_Gompertz['x'], df_Gompertz['s(x)'], 'b-', label = 'Gompertz')
# plt.plot(idade, df_Gompertz.loc[idade,'s(x)'], 'bo',label=f"s({idade}) = {df_Gompertz.loc[idade,'s(x)']:.3f}")
# plt.legend()
# plt.grid()
# plt.show()


# In[7]:


# plt.xlabel("Idade")
# plt.ylabel("s(x)")
# plt.title("Moivre u(x) vs Gompertz u(x) vs Makeham u(x)")
# plt.plot(df_DeMoivre['x'], df_DeMoivre['u_x'], 'g-', label = 'De Moivre')
# plt.plot(idade, df_DeMoivre.loc[idade,'u_x'], 'go',label=f"u({idade}) = {df_DeMoivre.loc[idade,'u_x']:.3f}")
# plt.plot(df_Gompertz['x'], df_Gompertz['u_x'], 'b-', label = 'Gompertz')
# plt.plot(idade, df_Gompertz.loc[idade,'u_x'], 'bo',label=f"u({idade}) = {df_Gompertz.loc[idade,'u_x']:.3f}")
# plt.plot(df_Makeham['x'], df_Makeham['u_x'], 'r-', label = 'Makeham')
# plt.plot(idade, df_Makeham.loc[idade,'u_x'], 'ro',label=f"u({idade}) = {df_Makeham.loc[idade,'u_x']:.3f}")
# plt.legend()
# plt.grid()
# plt.show()


# In[8]:


# Testando função de criar tabela
# w = int(input("Digite a ultima idade da tábua: "))

# tabela_teste = Tables(w, ["x", "l_x", "d_x", "q_x"]).create()
# tabela_teste

df_gui = pd.read_excel("Planilha31.08.xlsx")
w_df_gui = len(df_gui.index)-1
# %%
