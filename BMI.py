from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk()
GUI.geometry('1000x500')
GUI.title('โปรแกรมคำนวน BMI')


F1 = Frame(GUI)
F1.place(x=550, y=50)

F2 = Frame(GUI)
F2.place(x=185,y=350)

F3 = Frame(GUI)
F3.place(x=580, y=80)

F4 = Frame(GUI)
F4.place(x=580, y=80)


#Tab = ttk.Notebook(GUI)
#Tab.pack()

#F10=Frame(Tab)
#F11=Frame(Tab)

#Tab.add(F10,text='พื้นฐานการคำนวณ')
#Tab.add(F11,text='วงกลม')

ans = 0

def BMI():
    W = float(v_weight.get())
    H = float(v_height.get())
    ans = W/(H**2)
    if 0 < ans < 18.5:
        v_result.set('ค่า BMI = %.1f'%ans)
        v_result1.set('น้ำหนักต่ำกว่าเกณฑ์')


    elif 18.5 <= ans <= 22.9:
        v_result.set('ค่า BMI = %.1f'%ans)
        v_result1.set('น้ำหนักปกติ')



    elif 23 <= ans <= 24.9:
        v_result.set('ค่า BMI = %.1f'%ans)
        v_result1.set('น้ำหนักเกินกว่าปกติ')



    elif 25 <= ans <= 29.9:
        v_result.set('ค่า BMI = %.1f'%ans)
        v_result1.set('ภาวะอ้วนระดับที่ 1')



    elif ans >= 30:
        v_result.set('ค่า BMI = %.1f'%ans)
        v_result1.set('ภาวะอ้วนระดับที่ 2')

img1 = PhotoImage(file='Untitled design-2.png')
IM11 = Label(F4, image=img1)

if 0 < ans < 18.5:
    IM11.pack()

img2 = PhotoImage(file='Untitled design-4.png')
IM12 = Label(F4, image=img2)

if 18.5 <= ans <= 22.9:
    IM12.pack()

img3 = PhotoImage(file='Untitled design.png')
IM13 = Label(F4, image=img3)

if 23 <= ans <= 24.9:
    IM13.pack()

img4 = PhotoImage(file='Untitled design-3.png')
IM14 = Label(F4, image=img4)

if 25 <= ans <= 29.9:
    IM14.pack()

img5 = PhotoImage(file='Untitled design-5.png')
IM15 = Label(F4, image=img5)

if ans >= 30:
    IM15.pack()

img = PhotoImage(file='pokemon.png')
IM = Label(F3, image=img)
IM.pack()

#def add():
#    messagebox.showerror(title='การบวก',message='นี่การคือการบวก a + b = result')

menubar = Menu(GUI)
GUI.config(menu=menubar)

file = Menu(menubar,tearoff=0)
file.add_command(label='Exit', command=GUI.quit())
menubar.add_cascade(label='File',menu=file)

#calc = Menu(menubar,tearoff=0)
#calc.add_command(label='การบวก',command=add)
#calc.add_command(label='การลบ')
#calc.add_command(label='การคูณ')
#calc.add_command(label='การหาร')
#menubar.add_cascade(label='การคำนวณ',menu=calc)

img1 = PhotoImage(file='framee.png')
IM1 = Label(F1,image=img1)
IM1.grid(row=0,column=0)





FONT = ('Angsana New',20)
FONTi = ('Angsana New',30)

v_height = StringVar()
v_weight = StringVar()

L1 = Label(GUI,text='กรอกข้อมูล',font=FONT,bg='yellow')
L1.place(x=260,y=40)

LE1 = Label(GUI,text='ความสูง :',font=FONT)
LE1.place(x=95,y=120)

E1 = ttk.Entry(GUI,textvariable=v_height,font=FONT)
E1.place(x=190,y=120)

LE2 = Label(GUI,text='น้ำหนัก  :',font=FONT)
LE2.place(x=95,y=200)

E2 = ttk.Entry(GUI,textvariable=v_weight,font=FONT)
E2.place(x=190,y=200)

B1 = ttk.Button(GUI,text='ยืนยัน',command=BMI)
B1.place(x=265,y=280)

v_result = StringVar()
v_result.set('-----ผลลัพธ์-----')
Result = Label(F2,textvariable=v_result,font=FONTi,fg='red')
Result.pack()

v_result1 = StringVar()
Result1 = Label(F2,textvariable=v_result1,font=FONTi,fg='red')
Result1.pack()



GUI.mainloop()