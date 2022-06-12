#Dependencies
from tkinter import *
from tkinter.messagebox import *
from random import randint
#GUI
root=Tk()
root.title('Magic Squares')
root.geometry('300x300')
#Canvas
canvas=Canvas(root , width=300 , height=300)
canvas.pack()
#Number
num=randint(-100 , 100)
#Label
l1=Label(text='Magic Squares' , font=('Fira Sans' , 12))
canvas.create_window(150 , 50, window=l1)
l2=Label(text=num , font=('Fira Sans' , 12))
#Button
b1=Button(root , text='Start' , font=('Fira Sans' , 12) , bg='blue' , fg='white')
canvas.create_window(150 , 100 , window=b1)
b2=Button(root , text='Exit' , font=('Fira Sans' , 12) , bg='red' , fg='white' , width=4)
canvas.create_window(150 , 150, window=b2)
b3=Button(root , text='Verify' , font=('Fira Sans' , 12) , bg='blue' , fg='white') 
#Text
t1=Text(root , width=2 , height=1)
t2=Text(root , width=2 , height=1)
t3=Text(root , width=2 , height=1)
t4=Text(root , width=2 , height=1)
t5=Text(root , width=2 , height=1)
t6=Text(root , width=2 , height=1)
t7=Text(root , width=2 , height=1)
t8=Text(root , width=2 , height=1)
t9=Text(root , width=2 , height=1)
#Functions
def play_f():
    canvas.delete('all')
    canvas.create_window(150 , 40, window=l2)
    canvas.create_window(100 , 80 , window=t1)
    canvas.create_window(150 , 80 , window=t2)
    canvas.create_window(200 , 80, window=t3)
    canvas.create_window(100 , 110, window=t4)
    canvas.create_window(150 , 110, window=t5)
    canvas.create_window(200 , 110 , window=t6)
    canvas.create_window(100 , 140, window=t7)
    canvas.create_window(150 , 140, window=t8)
    canvas.create_window(200 , 140, window=t9)
    canvas.create_window(150 , 200 , window=b3)
#Verify
def verify_f():
    #Getting Input
    n1=t1.get(0.0 , 3.0)
    n2=t2.get(0.0 , 3.0)
    n3=t3.get(0.0 , 3.0)
    n4=t4.get(0.0 , 3.0)
    n5=t5.get(0.0 , 3.0)
    n6=t6.get(0.0 , 3.0)
    n7=t7.get(0.0 , 3.0)
    n8=t8.get(0.0 , 3.0)
    n9=t9.get(0.0 , 3.0)
    if n1=='\n' or n2=='\n' or n3=='\n' or n4=='\n' or n5=='\n' or n6=='\n' or n7=='\n' or n8=='\n' or n9=='\n':
        askretrycancel('Error' , 'Please enter a number on the text boxes')
    else:
        s1=int(n1)+int(n2)+int(n3)
        s2=int(n4)+int(n5)+int(n6)
        s3=int(n7)+int(n8)+int(n9)
        s4=int(n1)+int(n5)+int(n9)
        s5=int(n3)+int(n5)+int(n7)
        if not s1==num or s2==num or s3==num or s4==num or s5==num:
            showinfo('Error' , 'Please ensure that the sum of the row, columns and the diagonals is same as the number above')
        elif s1 and s2 and s3 and s4 and s5 == num:
            showinfo('Sucess' , 'You succesfully solved the magic square')       
#Alocating commands to buttons
b1.configure(command=play_f)
b2.configure(command=root.destroy)
b3.configure(command=verify_f)    
#Exec
root.mainloop()
