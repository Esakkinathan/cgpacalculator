from tkinter import *
from tkinter import ttk  
from tkinter import messagebox  

gradeval= ('O','A+','A','B+','B','C','U')
grade={"O":10,"A+":9,"A":8,"B+":7,"B":6,"C":5,"U":0}


def gpachecksem1(a1,b1,c1,d1,e1,f1,g1):
  if(a1=="" or b1=="" or c1=="" or d1=="" or e1=="" or f1=="" or g1==""):
    messagebox.showerror("Error","Select All the grades")
  else:
    sumval=((grade[a1]*2)+(grade[b1]*3)+(grade[c1]*3)+(grade[d1]*2)+(grade[e1]*4)+(grade[f1]*4)+(grade[g1]*3))
    print(sumval)
    gpa=sumval/21
    Label(sem1win,text="Your SEMESTER-1 GPA is:",bg="#121212",fg="#fff",font = ("Courier",15)).place(x=50,y=500) 
    print(gpa)
    ans=round(gpa,2)
    Label(sem1win, text=str(ans),bg="red",fg="black",font = ("MV Boli", 15)).place(x=330,y=500)


def gpachecksem2(a2,b2,c2,d2,e2,f2,g2,h2):
  if(a2=="" or b2=="" or c2=="" or d2=="" or e2=="" or f2=="" or g2=="" or h2==""):
    messagebox.showerror("Error","Select All the grades")
  else:
    sumval2=((grade[a2]*3)+(grade[b2]*3)+(grade[c2]*2)+(grade[d2]*4)+(grade[e2]*2)+(grade[f2]*4)+(grade[g2]*4)+(grade[h2]*3))
    print(sumval2)
    gpa2=sumval2/25
    Label(sem2win, text = "Your SEMESTER-2 GPA is:",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=70,y=540)
    print(gpa2)
    ans=round(gpa2,2)
    Label(sem2win, text =str(ans),bg="red",fg="black",font = ("MV Boli", 15)).place(x=330,y=540)


def gpachecksem3(a3,b3,c3,d3,e3,f3,g3,h3,i3):
  if(a3=="" or b3=="" or c3=="" or d3=="" or e3=="" or f3=="" or g3=="" or h3=="" or i3==""):
    messagebox.showerror("Error","Select All the grades")
  else:
    grade={"O":10,"A+":9,"A":8,"B+":7,"B":6,"C":5,"U":0}
    sumval3=((grade[a3]*3)+(grade[b3]*1.5)+(grade[c3]*4)+(grade[d3]*3)+(grade[e3]*2)+
      (grade[f3]*1.5)+(grade[g3]*3)+(grade[h3]*1)+(grade[i3]*4))
    print(sumval3)
    gpa3=sumval3/23
    print(gpa3)
    Label(sem3win, text = "Your SEMESTER-3 GPA is:",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=70,y=550)
    ans=round(gpa3,2)
    Label(sem3win, text =str(ans),bg="red",fg="black",font = ("MV Boli", 15)).place(x=340,y=550)


def gpachecksem4(a3,b3,c3,d3,e3,f3,g3,h3):
  if(a3=="" or b3=="" or c3=="" or d3=="" or e3=="" or f3=="" or g3=="" or h3==""):
    messagebox.showerror("Error","Select All the grades")
  else:
    grade={"O":10,"A+":9,"A":8,"B+":7,"B":6,"C":5,"U":0}
    sumval4=((grade[a3]*4)+(grade[b3]*3)+(grade[c3]*3)+(grade[d3]*1.5)+(grade[e3]*1.5)+
      (grade[f3]*4)+(grade[g3]*3)+(grade[h3]*2))
    print(sumval4)
    gpa4=sumval4/22
    print(gpa4)
    Label(sem4win, text = "Your SEMESTER-3 GPA is:",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=70,y=550)
    ans=round(gpa4,2)
    Label(sem4win, text =str(ans),bg="red",fg="black",font = ("MV Boli", 15)).place(x=340,y=550)
    
def cgpacheck(sem1,sem2,sem3,sem4):
  if(sem1=="" or sem2=="" or sem3=="" or sem4==""):
    messagebox.showerror("Error","Enter values in all the field")
  else:
    try:
      if(float(sem1)>10 or float(sem2)>10 or float(sem3)>10 or float(sem4)>10):
        messagebox.showerror("Error", "values should be less than 10")   
      else:
        csumval=float(sem1)+float(sem2)+float(sem3)+float(sem4)
        cgpa=csumval/4
        Label(cgpawin, text = "Your Current CGPA is:",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=340)
        ans=round(cgpa,2)
        Label(cgpawin, text = str(ans),bg="red",fg="black",font = ("Courier", 15)).place(x=350,y=340)
    except ValueError:
      messagebox.showerror("Error", "values are not a number")



def opensem1():
  global sem1win
  sem1win = Toplevel() 
  def on_cls():
    if(messagebox.askokcancel("Quit","Do you want to close?")):
      sem1win.destroy()
      mainwin.deiconify()
  sem1win.title('CPGA CALCULATOR') 
  sem1win.geometry('550x550')
  sem1win.configure(bg="#121212")

   
  Label(sem1win,text="Select the grade:",bg='red',fg="#fff",font=("Courier", 20,"bold","underline")).pack(padx=5,pady=10) 
  Label(sem1win, text = "Select your BS3171 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=70)  
  Label(sem1win, text = "Select your CY3151 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=120) 
  Label(sem1win,text="Select your GE3151 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=170)
  Label(sem1win,text="Select your GE3171 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=220)
  Label(sem1win,text="Select your HS3151 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=270)
  Label(sem1win,text="Select your MA3151 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=320)
  Label(sem1win,text = "Select your PH3151 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=370) 

  a1 = StringVar()
  b1 = StringVar()
  c1 = StringVar()
  d1 = StringVar()
  e1 = StringVar()
  f1 = StringVar()
  g1 = StringVar()   


  bs3171= ttk.Combobox(sem1win,width=7,textvariable=a1,values=gradeval)      
  bs3171.place(x=400,y=75)
  bs3171.current()

  cy3151= ttk.Combobox(sem1win,width=7,textvariable=b1,values=gradeval)  
  cy3151.place(x=400,y=125)
  cy3151.current()

  ge3151 = ttk.Combobox(sem1win,width=7,textvariable=c1,values=gradeval)   
  ge3151.place(x=400,y=175)
  ge3151.current()
                  
  ge3171 = ttk.Combobox(sem1win,width=7,textvariable=d1,values=gradeval) 
  ge3171.place(x=400,y=225)
  ge3171.current()
           
  hs3151 = ttk.Combobox(sem1win,width=7,textvariable=e1,values=gradeval) 
  hs3151.place(x=400,y=275) 
  hs3151.current()

  ma3151 = ttk.Combobox(sem1win,width=7,textvariable=f1,values=gradeval)     
  ma3151.place(x=400,y=325) 
  ma3151.current()

  ph3151 = ttk.Combobox(sem1win,width=7,textvariable=g1,values=gradeval)     
  ph3151.place(x=400,y=370) 
  ph3151.current()

          #checkbutton
  checkbtn1=Button(sem1win,text="Check",bg="#2c3e50",fg="#fff",relief=FLAT,activebackground="#121212",activeforeground="#fff",font=("Courier",10),command=lambda : gpachecksem1(a1.get(),b1.get(),c1.get(),d1.get(),e1.get(),f1.get(),g1.get()))
  backbtn1=Button(sem1win,text="<back",bg="#2c3e50",fg="#fff",relief=FLAT,activebackground="#121212",activeforeground="#fff",font = ("Courier", 10),command=lambda :goback1())
  checkbtn1.place(x=400,y=430)
  backbtn1.place(x=150,y=430)
  sem1win.protocol("WM_DELETE_WINDOW",on_cls)
  def goback1():
    mainwin.deiconify()
    sem1win.destroy()


def opensem2():
  global sem2win
  sem2win = Toplevel() 
  sem2win.title('CPGA CALCULATOR') 
  sem2win.geometry('550x590')
  sem2win.configure(bg="#121212")

  Label(sem2win,text="Select the grade:",bg='red',fg="#fff",font=("Courier", 20,"bold","underline")).pack(padx=5,pady=10) 
  Label(sem2win,text="Select your BE3251 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=70) 
  Label(sem2win,text="Select your CS3251 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=120) 
  Label(sem2win,text="Select your CS3271 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=170)
  Label(sem2win,text="Select your GE3251 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=220)
  Label(sem2win,text="Select your GE3271 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=270)
  Label(sem2win,text="Select your HS3251 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=320)
  Label(sem2win,text="Select your MA3251 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=370) 
  Label(sem2win,text="Select your PH3256 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=420)  


  a2 = StringVar()
  b2 = StringVar() 
  c2 = StringVar()  
  d2 = StringVar() 
  e2 = StringVar()
  f2 = StringVar() 
  g2 = StringVar()
  h2 = StringVar()   
         

  be3251= ttk.Combobox(sem2win,width=7,textvariable=a2,values=gradeval)   
  be3251.place(x=400,y=75)
  be3251.current()

  cs3251= ttk.Combobox(sem2win,width=7,textvariable=b2,values=gradeval)
  cs3251.place(x=400,y=125)
  cs3251.current()         
           
  cs3271 = ttk.Combobox(sem2win,width=7,textvariable=c2,values=gradeval)   
  cs3271.place(x=400,y=175) 
  cs3271.current()
          
  ge3251 = ttk.Combobox(sem2win,width=7,textvariable=d2,values=gradeval) 
  ge3251.place(x=400,y=225) 
  ge3251.current()

  ge3271 =ttk.Combobox(sem2win,width=7,textvariable=e2,values=gradeval) 
  ge3271.place(x=400,y=275) 
  ge3271.current()
           
  hs3251 = ttk.Combobox(sem2win,width=7,textvariable=f2,values=gradeval)   
  hs3251.place(x=400,y=325)
  hs3251.current()
        
  ma3251 = ttk.Combobox(sem2win,width=7,textvariable=g2,values=gradeval)    
  ma3251.place(x=400,y=375)
  ma3251.current()
       
  ph3256 = ttk.Combobox(sem2win,width=7,textvariable=h2,values=gradeval)
  ph3256.place(x=400,y=420) 
  ph3256.current()


  checkbtn2=Button(sem2win,text="Check",bg="#2c3e50",fg="#fff",relief=FLAT,activebackground="#121212",activeforeground="#fff",font = ("Courier", 15),command=lambda : gpachecksem2(a2.get(),b2.get(),c2.get(),d2.get(),e2.get(),f2.get(),g2.get(),h2.get()))
  checkbtn2.place(x=330,y=470)
  backbtn2=Button(sem2win,text="back",bg="#2c3e50",fg="#fff",relief=FLAT,activebackground="#121212",activeforeground="#fff",font = ("Courier", 15),command=lambda : goback2())
  backbtn2.place(x=150,y=470)
  def goback2():
    mainwin.deiconify()
    sem2win.destroy()


def opensem3():
  global sem3win
  sem3win=Toplevel() 
  sem3win.title('CPGA CALCULATOR') 
  sem3win.geometry('600x630')
  sem3win.configure(bg="#121212")


  Label(sem3win,text="Select the grade:",bg='red',fg="#fff",font=("Courier", 20,"bold","underline")).place(x=100,y=20)
  Label(sem3win,text="Select your CS3301 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=70)
  Label(sem3win,text="Select your CS3311 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=120)
  Label(sem3win,text="Select your CS3351 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=170)
  Label(sem3win,text="Select your CS3352 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=220)
  Label(sem3win,text="Select your CS3361 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=270)
  Label(sem3win,text="Select your CS3381 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=320) 
  Label(sem3win,text="Select your CS3391 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=370)  
  Label(sem3win,text="Select your GE3361 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=420) 
  Label(sem3win,text="Select your MA3354 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=470)  


  a3 = StringVar()
  b3 = StringVar()
  c3 = StringVar()         
  d3 = StringVar()        
  e3 = StringVar()
  f3 = StringVar()
  g3 = StringVar()         
  h3 = StringVar()         
  i3 = StringVar()


  



  cs3301 = ttk.Combobox(sem3win,width=7,textvariable=a3,values=gradeval) 
  cs3301.place(x=400,y=75) 
  cs3301.current()


  cs3311 = ttk.Combobox(sem3win,width=7,textvariable=b3,values=gradeval)   
  cs3311.place(x=400,y=125)
  cs3311.current()

  cs3351= ttk.Combobox(sem3win,width=7,textvariable=c3,values=gradeval) 
  cs3351.place(x=400,y=175) 
  cs3351.current()


  cs3352 = ttk.Combobox(sem3win,width=7,textvariable=d3,values=gradeval)   
  cs3352.place(x=400,y=225) 
  cs3352.current()
   

  cs3361 = ttk.Combobox(sem3win,width=7,textvariable=e3,values=gradeval)   
  cs3361.place(x=400,y=275) 
  cs3361.current()
  
  cs3381 = ttk.Combobox(sem3win,width=7,textvariable=f3,values=gradeval)   
  cs3381.place(x=400,y=325)
  cs3381.current()

  cs3391 = ttk.Combobox(sem3win,width=7,textvariable=g3,values=gradeval) 
  cs3391.place(x=400,y=375) 
  cs3391.current()


  ge3361 = ttk.Combobox(sem3win,width=7,textvariable=h3,values=gradeval)   
  ge3361.place(x=400,y=420) 
  ge3361.current()

  ma3354= ttk.Combobox(sem3win,width=7,textvariable=i3,values=gradeval) 
  ma3354.place(x=400,y=470)
  ma3354.current()

          #checkbutton
  checkbtn3=Button(sem3win,text="Check",bg="#2c3e50",fg="#fff",relief=FLAT,activebackground="#121212",activeforeground="#fff",font = ("Courier", 13),command=lambda : gpachecksem3(a3.get(),b3.get(),c3.get(),d3.get(),e3.get(),f3.get(),g3.get(),h3.get(),i3.get()))
  checkbtn3.place(x=330,y=510)
  backbtn3=Button(sem3win,text="<back",bg="#2c3e50",fg="#fff",relief=FLAT,activebackground="#121212",activeforeground="#fff",font = ("Courier", 13),command=lambda : goback3())
  backbtn3.place(x=150,y=510)
  def goback3():
    mainwin.deiconify()
    sem3win.destroy()


def opensem4():
  global sem4win
  sem4win=Toplevel() 
  sem4win.title('CPGA CALCULATOR') 
  sem4win.geometry('600x630')
  sem4win.configure(bg="#121212")


  Label(sem4win,text="Select the grade:",bg='red',fg="#fff",font=("Courier", 20,"bold","underline")).place(x=100,y=20)
  Label(sem4win,text="Select your CS3401 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=70)
  Label(sem4win,text="Select your CS3451 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=120)
  Label(sem4win,text="Select your CS3452 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=170)
  Label(sem4win,text="Select your CS3462 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=220)
  Label(sem4win,text="Select your CS3481 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=270)
  Label(sem4win,text="Select your CS3491 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=320) 
  Label(sem4win,text="Select your CS3492 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=370)  
  Label(sem4win,text="Select your GE3451 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=420) 
  #Label(sem4win,text="Select your MA3354 grade :",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=470)  


  a4 = StringVar()
  b4 = StringVar()
  c4 = StringVar()         
  d4 = StringVar()        
  e4 = StringVar()
  f4 = StringVar()
  g4 = StringVar()         
  h4 = StringVar()         
  #i4 = StringVar()


  



  cs3401 = ttk.Combobox(sem4win,width=7,textvariable=a4,values=gradeval) 
  cs3401.place(x=400,y=75) 
  cs3401.current()


  cs3451 = ttk.Combobox(sem4win,width=7,textvariable=b4,values=gradeval)   
  cs3451.place(x=400,y=125)
  cs3451.current()

  cs3452= ttk.Combobox(sem4win,width=7,textvariable=c4,values=gradeval) 
  cs3452.place(x=400,y=175) 
  cs3452.current()


  cs3461 = ttk.Combobox(sem4win,width=7,textvariable=d4,values=gradeval)   
  cs3461.place(x=400,y=225) 
  cs3461.current()
   

  cs3481 = ttk.Combobox(sem4win,width=7,textvariable=e4,values=gradeval)   
  cs3481.place(x=400,y=275) 
  cs3481.current()
  
  cs3491 = ttk.Combobox(sem4win,width=7,textvariable=f4,values=gradeval)   
  cs3491.place(x=400,y=325)
  cs3491.current()

  cs3492 = ttk.Combobox(sem4win,width=7,textvariable=g4,values=gradeval) 
  cs3492.place(x=400,y=375) 
  cs3492.current()


  ge3451 = ttk.Combobox(sem4win,width=7,textvariable=h4,values=gradeval)   
  ge3451.place(x=400,y=420) 
  ge3451.current()

  
          #checkbutton
  checkbtn4=Button(sem4win,text="Check",bg="#2c3e50",fg="#fff",relief=FLAT,activebackground="#121212",activeforeground="#fff",font = ("Courier", 13),command=lambda : gpachecksem4(a4.get(),b4.get(),c4.get(),d4.get(),e4.get(),f4.get(),g4.get(),h4.get()))
  checkbtn4.place(x=330,y=510)
  backbtn4=Button(sem4win,text="<back",bg="#2c3e50",fg="#fff",relief=FLAT,activebackground="#121212",activeforeground="#fff",font = ("Courier", 13),command=lambda : goback4())
  backbtn4.place(x=150,y=510)
  def goback4():
    mainwin.deiconify()
    sem4win.destroy()


def opencgpa():
  global cgpawin
  cgpawin = Toplevel() 
  cgpawin.title('CPGA CALCULATOR') 
  cgpawin.geometry('500x400')
  cgpawin.configure(bg="#121212")
  sem1Label =Label(cgpawin, text="Enter SEMESTER-1 GPA:",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=70)
  sem2Label =Label(cgpawin, text="Enter SEMESTER-2 GPA:",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=120)
  sem3Label =Label(cgpawin, text="Enter SEMESTER-3 GPA:",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=170)
  sem3Label =Label(cgpawin, text="Enter SEMESTER-4 GPA:",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=50,y=220)
  sem1 = StringVar()
  sem2 = StringVar()
  sem3 = StringVar()
  sem4 = StringVar()

  sem1Entry = Entry(cgpawin,bg="#121212",fg="#fff",width=15,bd=3,textvariable=sem1,insertbackground="white").place(x=330,y=70)
  sem2Entry = Entry(cgpawin,bg="#121212",fg="#fff",width=15,bd=3,textvariable=sem2,insertbackground="white").place(x=330,y=120)
  sem3Entry = Entry(cgpawin,bg="#121212",fg="#fff",width=15,bd=3,textvariable=sem3,insertbackground="white").place(x=330,y=170)
  sem4Entry = Entry(cgpawin,bg="#121212",fg="#fff",width=15,bd=3,textvariable=sem4,insertbackground="white").place(x=330,y=220)
          

  checkbtn5=Button(cgpawin,text="Check",bg="#2c3e50",relief=FLAT,activebackground="#121212",activeforeground="#fff",fg="#fff",font = ("Courier", 13),command=lambda : cgpacheck(sem1.get(),sem2.get(),sem3.get(),sem4.get()))
  checkbtn5.place(x=350,y=270)
  backbtn5=Button(cgpawin,text="<back",bg="#2c3e50",relief=FLAT,activebackground="#121212",activeforeground="#fff",fg="#fff",font = ("Courier", 13),command=lambda : goback3())
  backbtn5.place(x=150,y=270)
  def goback3():
    mainwin.deiconify()
    cgpawin.destroy()



mainwin  = Tk() 
mainwin.title('CGPACALCULATOR') 
mainwin.geometry('400x300')
mainwin.configure(bg="#121212")
Label(mainwin,text="CGPA CALCULATOR:",bg='red',fg="black",font = ("MV Boli",20,"bold","underline")).pack(padx=5,pady=10)
Label(mainwin, text = "Select one option",bg="#121212",fg="#fff",font = ("Courier", 15)).place(x=30,y=100)  
opt = StringVar() 
option= ttk.Combobox(mainwin, width = 10, textvariable = opt )   
option['values'] = ('SEMESTER-1','SEMESTER-2','SEMESTER-3','SEMESTER-4','checkCGPA')   
option.place(x=250,y=100)
option.current()
Button(mainwin,text="Click",bg="#2c3e50",relief=FLAT,fg="#fff",activebackground="#121212",activeforeground="#fff",font=("Courier",10),command=lambda : optioncheck(opt.get())).place(x=180,y=200)


def optioncheck(opt):
  mainwin.state('iconic')
  if(opt=='SEMESTER-1'):
    opensem1()
  elif(opt==""):
    mainwin.deiconify()
    messagebox.showerror("error","Select any one option")
  elif(opt=='SEMESTER-2'):
    opensem2()
  elif(opt=='SEMESTER-3'):
    opensem3()
  elif(opt=='SEMESTER-4'):
    opensem4()
  elif(opt=='checkCGPA'):
    opencgpa()
        
mainwin.mainloop() 


