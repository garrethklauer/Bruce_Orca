from tkinter import*
import random 
a=Tk()
a.config(bg="black")
a.geometry("600x400")
m=['a','b','c']
r = ['Red', 'Blue', 'Green', 'Pink', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0 
e=StringVar()
e1=Entry(a, textvariable=e,font="vardana 25", fg='red', bg='black', insertbackground='red')
st=Label(a, text="Lets Start", width=600, height=400,font='vardane 90', fg='green', bg='black')
st.pack()
q=Label(a,font="vardana 50", bg='black')
q.place(x=230,y=50)
uu=Label(a)
sc=Label(a, text='score : 0', font='vardana 30', fg='green', bg='black')
tm=31
t=Label(a)
def re(event):
    score=0
    tm=20
    m.start(event)
def sp(score):
    return score
def results():
    b=Label(a,text='score: '+str(sp(score)), fg='green', font='vardana 50', bg="black")
    b.pack()
    bm=Label(a,text="speed : " + str(round(30/(score)))+ 'sec/word',width=200,height=100,fg='green', font='vardana 40', bg='black')
    bm.pack()
    uu.pack_forget()
    sc.place_forget()

def ti():
    global tm
    if tm>0:
        tm=tm-1
        t.config(text='time left: '+str(tm), font='vardana 30', bg='black', fg='orange')
        t.place(x=2,y=2)
        a.after(1000,ti)
    else:
        e1.place_forget()
        uu.pack()
        sc.place_forget()
        t.place_forget()
        a.after(2000, results)
class m():
    def start(event):
        try:
            st.pack_forget()
            global tm
            if tm==31:
                ti()
            global l1
            i=random.randint(0,9)
            kk=random.randint(0,9)
            q.config(text=str(r[i]), fg=r[kk])
            e1.place(x=120,y=200)
            sc.place(x=400, y=2)
            def n(event):
                global score
                if e.get()==r[i].lower():
                    e1.delete(0,END)
                    score=1+score
                    sc.config(text="score :"+str(score))
                    sp(score)
                    m.start(event)
                else:
                    e1.delete(0,END)
                    m.start(event)
            a.bind("<Return>", n)
        except:
            pass
    a.bind("<Return>", start)

a.mainloop()
