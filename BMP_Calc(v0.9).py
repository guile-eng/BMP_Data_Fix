from tkinter import *
import pandas as pd
import numpy as np
from pandas import DataFrame as df
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter import messagebox

root= Tk()
root.title(" BMP Datafix by Ms.Gee (Version: 0.9) ")

frame=LabelFrame(root,text="Eventlog inputs",padx=80, pady=10)
frame.grid(row=0, column=0)

frame2=LabelFrame(root,text="Calculations",padx=10, pady=10)
frame2.grid(row=1, column=1)

frame3=LabelFrame(root,text="Log",padx=10, pady=10)
frame3.grid(row=1, column=0)

frame4=LabelFrame(root,text="Replicates",padx=10, pady=10)
frame4.grid(row=0, column=1)

t_vessels=Entry(frame,width=10)
t_vessels.grid(row=0, column=1)
t_vessels.insert(0,"14")


t_days=Entry(frame,width=10)
t_days.grid(row=1, column=1)
# t_days.insert(0,"14")
days= t_days.get()

lvessels = Label(frame, text='Number of sample vessels: ', height=1).grid(row=0, column=0)
ldays = Label(frame, text='Number of days: ', height=1).grid(row=1, column=0)
ldays = Label(frame, text='CSV path: ', height=1, width=40).grid(row=2, column=0)
##################
eventlog=[]
def openFile ():
	global pathname
	global eventlog
	pathname = filedialog.askopenfilename(initialdir="/user/desktop", title="Select file ...", filetypes= ( ("CSV file", ".csv"),("All files", "*.*") )  )
	file_label=Label(frame,text=pathname, height=1, width=50 ).grid(row=2, column=1)
	eventlog=pd.read_csv(pathname,header=1)

def vname (v_number):
  #Criando a lista de nomes com base no numero de vessel
  a= eventlog.iloc[eventlog.index[eventlog["Channel number"]== str(v_number)].tolist()]  #Criando novo indice
  a= pd.DataFrame(a).reset_index(drop=1)
  #Pegando o primeiro nome do indice (se nao tiver nenhum, mensagem avisando)
  if (len(a)==0):
    b=["No name available"]
  else:
    b=a.loc[0,'Name']

  return b


def graph():
  messagebox.showinfo("Function not ready","I'm still working in this function. Thanks")
  a=plt.plot(eventlog[eventlog["Channel number"]=="1"], eventlog["Days"])
  plt.show(a)





def filter_0 ():
  if len(eventlog) == 0:
    messagebox.showinfo("Select eventlog","Select the proper csv eventlog")
  if t_days.get() == "":
    messagebox.showinfo("Error","Select the total amount of days running")
  a=int(t_days.get())
  b=int(t_vessels.get())
  l0=[]
  s="d"
  if s == 'd':
    for y in range (0,a,1):
      for x in range (1,b+1,1):
        q = eventlog[eventlog["Channel number"] == str(x)]
        v1d1 = q[q["Days"] == y]
            
        if len(v1d1)== 0:
          
          if len(v1d1.columns) == 16:
            l0.extend([[str(x),vname(x),0,y,5,0,0,0,0,0,0,0,0,0,0,0]])
          
          elif len(v1d1.columns) == 17:
            l0.extend([[str(x),vname(x),0,y,5,0,0,0,0,0,0,0,0,0,0,0,0]])
            
          else:
            l0=print("Numero de colunas nao compativel")
   
  elif s == 'n':
    for x in range (1,b+1,1):
      for y in range (0,a+1,1):
        q = eventlog[eventlog["Channel number"] == str(x)]
        v1d1 = q[q["Days"] == y]
            
        if len(v1d1)== 0:
          
          if len(v1d1.columns) == 16:
            l0.extend([[str(x),vname(x),0,y,5,0,0,0,0,0,0,0,0,0,0,0]])
          
          elif len(v1d1.columns) == 17:
            l0.extend([[str(x),vname(x),0,y,5,0,0,0,0,0,0,0,0,0,0,0,0]])
            
            
          else:
            l0=print("Numero de colunas nao compativel")
  else:
   l0=print("Invalid order")
  print("Eventlog_0 has been created!")
  T.insert(END,"Eventlog_0 has been created!\n")
  f=pd.DataFrame(l0)
  f.columns= eventlog.columns
  f.to_csv('./0_eventlog.csv', index = False)



def media_c():
  if len(eventlog) == 0:
    messagebox.showinfo("Select eventlog","Select the proper csv eventlog")
  vessels=int(t_vessels.get())
  days=int(t_days.get())
  dic={
      '1':16,
      '3':17,
      '5':18,
      '7':19,
      '9':20,
      '11':21,
      '13':22,
  }
  lc=[]
  for y1 in range (0,int(days),1):
    for x1 in range (1,int(vessels)+1,2):
      q1 = eventlog[eventlog["Channel number"] == str(x1)]
      v1d1 = q1[q1["Days"] == y1]
      a= v1d1['Vol this tip (STP)'].sum()
      q2 = eventlog[eventlog["Channel number"] == str(x1+1)]
      v2d2 = q2[q2["Days"] == y1]
      b= v2d2['Vol this tip (STP)'].sum()
      
      c= (a+b)/2

    
      if len(v2d2.columns) == 16:
        lc.extend([[str(dic[str(x1)]),vname(x1).replace('-A','-C').replace(f'-{x1}-',"-"+str(dic[str(x1)])+"-"),0,y1,5,0,0,0,0,c,0,0,0,0,0,0]])
        
          
      elif len(v2d2.columns) == 17:
        lc.extend([[str(dic[str(x1)]),vname(x1).replace('-A','-C').replace(f'-{x1}-',"-"+str(dic[str(x1)])+"-"),0,y1,5,0,0,0,0,0,c,0,0,0,0,0,0]])
        
      else:
        lc=print("Numero de colunas nao compativel")
  print("Eventlog_C has been created!")
  T.insert(END,"Eventlog_C has been created!\n")
  f=pd.DataFrame(lc)
  f.columns= eventlog.columns
  f.to_csv('./C_eventlog.csv', index = False)





T =Text(frame3, height=10, width=100)
T.grid(row=0)
b_open= Button(frame2, text="Open eventlog",command= openFile, height=1, width=15).grid(row=0,column=0)
b_plot= Button(frame2, text="Plot graph",command= graph, height=1, width=15).grid(row=0,column=1)
button0=Button(frame2,text="Calculate 0", command=filter_0, height=1, width=15).grid(row=1, column=0)
buttonc=Button(frame2,text="Calculate C", command=media_c, height=1, width=15 ).grid(row=1, column=1)
button_quit=Button(frame2,text="Exit", command=root.quit, height=1, width=15).grid(row=2, column=0)

root.mainloop()
