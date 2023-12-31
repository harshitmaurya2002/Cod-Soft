from tkinter import *
root=Tk()
root.geometry("570x600+200+200")
root.title("The Calculator")
root.resizable(False,False)
root.configure(bg="black")

equa=""

def show(value):
    global equa
    equa+=value
    
    lab_result.config(text=equa)

def clear():
    global equa
    equa=""
    lab_result.config(text=equa)
def calculate():
    global equa
    result=""
    if equa!="":
        try:
            result=eval(equa)
        except:
            result="error"
            equa=""
    lab_result.config(text=result)


lab_result=Label(root,width=25,height=2,text="",font=("arial",30))
lab_result.pack()


Button(root,text="C",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="red",command=lambda: clear()).place(x=10,y=100)
Button(root,text="/",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("/")).place(x=150,y=100)
Button(root,text="%",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("%")).place(x=290,y=100)
Button(root,text="*",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("*")).place(x=430,y=100)
Button(root,text="7",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("7")).place(x=10,y=200)
Button(root,text="8",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("8")).place(x=150,y=200)
Button(root,text="9",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("9")).place(x=290,y=200)                                                                                                                          
Button(root,text="-",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("-")).place(x=430,y=200)
Button(root,text="6",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("6")).place(x=10,y=300)
Button(root,text="5",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("5")).place(x=150,y=300)
Button(root,text="4",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("4")).place(x=290,y=300)
Button(root,text="+",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("+")).place(x=430,y=300)
Button(root,text="1",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("1")).place(x=10,y=400)
Button(root,text="2",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("2")).place(x=150,y=400)
Button(root,text="3",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("3")).place(x=290,y=400)
Button(root,text="=",width=5,height=3,font=("arial",30,"bold"),bd=5,fg="black",bg="orange",command=lambda: calculate()).place(x=430,y=400)
Button(root,text=".",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show(".")).place(x=290,y=500)
Button(root,text="0",width=11,height=1,font=("arial",30,"bold"),bd=5,fg="white",bg="grey",command=lambda: show("0")).place(x=10,y=500)

root.mainloop()
