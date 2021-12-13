# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 19:01:37 2021

@author: sivaparvathi671
"""
from tkinter import *
import pandas as pd
f=pd.read_excel('QUIZ-I CS.xlsx',index_col=False)
questions=f['Question'].tolist()
options_A=f['A'].tolist()
options_B=f['B'].tolist()
options_C=f['C'].tolist()
options_D=f['D'].tolist()
ans=f['Answer'].tolist()
index=1
formet=list(zip(questions,options_A,options_B,options_C,options_D,ans))
#print(formet[:3])
def next_q():
    global index,l1,formet,rb_li,v
    index+=1
    l1['text']=formet[index][0]
    print(v.get())
    
    #l1['text']=formet[index][0]
    i=1
    for rb in rb_li:
        rb['text']=formet[index][i]
        #rb.select()
        i+=1

def prev_q():
    global index,l1,formet,rb_li,v
    index-=1
    l1['text']=formet[index][0]
    i=1
    print(v.get())
    for rb in rb_li:
        rb['text']=formet[index][i]
        #rb.select()
        i+=1
    
win=Tk()
win.geometry("900x900")
win.title("QUIZ")
win.config(background="#ffffff")
l=Label(win,text="Welcome to Quiz",bg="#ffffff",fg="red",font=('Arial',20))
l1=Label(win, text=formet[index][0],font=('Arial',25),bg="#ffffff")
l2=Label(win, text="CHOOSE ONE OPTION ",font=10,bg="#ffffff")
v = StringVar(win, '1')
print(formet[index][4])
b1=Button(win, text="PREV",font=25,command=prev_q)
b2=Button(win, text="SUBMIT",font=25)
b3=Button(win, text="NEXT",font=25,command=next_q)
rb_li=[]
value=['A','B','C','D']
for i in range(1,5):
    r1=Radiobutton(win, text = formet[index][i], variable = v,value = value[i-1],bg="#ffffff",font=('Arial',15))
    rb_li.append(r1)

l.pack(pady=(5,3))
l1.pack(pady=(3,5))
l2.pack(pady=(2,6))
for rb in rb_li:
    rb.pack(pady=(10,0))
b1.place(x=100,y=500)
b2.place(x=400,y=500)
b3.place(x=800,y=500)
print(index)

    
    
    
    
win.mainloop()

    


