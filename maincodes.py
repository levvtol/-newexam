## packages
## pip(3) install tkinter


import tkinter as tk                
from tkinter import font as tkfont  
from tkinter import *
from tkinter import messagebox
from smtplib import SMTP
import os,time
import tkinter.font as tkFont

mycolor = "#c9effe"

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

       
       
       
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (menu, login, signup, exams,examrules,exam_physics, options,changepass):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

           
           
           
            frame.grid(row=0, column=0, sticky="nsew")
        with open("iki" + '.txt', 'r') as file_object2:
            iki = file_object2.read() 
        
        if iki == "0":
            self.show_frame("menu")
        else:
            with open("savelogin" + '.txt', 'r') as file_object2:
                savelogin = file_object2.read() 
                
                if savelogin == "1":
                    self.show_frame("exams")
                elif savelogin == "0":
                    self.show_frame("menu")
            
            
                
       
       
       
       
       
            
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
            
            
class menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg = mycolor)
        

        button1 = tk.Button(self, text="Login",
                            command=lambda: controller.show_frame("login"))
        button2 = tk.Button(self, text="Signup",
                            command=lambda: controller.show_frame("signup"))
        button1.pack()
        button2.pack()


class login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg = mycolor)
        def saveloginxyz():
            def xyz():
                
                    with open("iki" + '.txt', 'r') as file_object2:
                        iki = file_object2.read() 
                        iki = int(iki)
                        with open('iki' + '.txt', 'w') as file_object2: 
                            iki = 1
                            iki = str(iki) 
                            file_object2.write(iki)  
                            
            xyz()
            
            
        def savelogin():

            email = eemail1.get()
            def y():
                
                if(chkValue.get()):
                    with open("savelogin" + '.txt', 'r') as file_object2:
                        savelogin = file_object2.read() 
                        savelogin = int(savelogin)
                        with open('savelogin' + '.txt', 'w') as file_object2: 
                            savelogin = 1
                            savelogin = str(savelogin) 
                            file_object2.write(savelogin)
                                
                else:
                    with open("savelogin" + '.txt', 'r') as file_object2:
                        savelogin = file_object2.read() 
                        savelogin = int(savelogin)
                        with open('savelogin' + '.txt', 'w') as file_object2: 
                            savelogin = 0
                            savelogin = str(savelogin) 
                            file_object2.write(savelogin)  
                            
            y()
            with open('last_save_user' + '.txt', 'w') as file_object24: 
                file_object24.write(email)   
                                                
                    
        
        def save():
            global iki
            email = eemail1.get()
            password = esifre1.get()
            file = f"./users/{email}"                    
        
            
            if email != "":
                f = 0
                entries = os.listdir('./users/')
                for entryx in entries:
                    if entryx == f"{email}.txt":
                        with open(file + '.txt', 'r') as f:
                            pas = f.read() 
                            if password == pas:
                                messagebox.showinfo("login", f"hello dear {email}")
                                f = 1
                                controller.show_frame("exams")
                                iki = 1
                                saveloginxyz()
                                eemail1.delete(0, END)
                                esifre1.delete(0, END)
                                

                if f != 1:
                    messagebox.showinfo("error", "email adress or password are't correct")
            
            
            
            with open('last_save_user' + '.txt', 'w') as file_object24: 
                file_object24.write(email)  
            
            
            
        
                
        def showpassaword():
            if(CheckVar12.get()):
                
                esifre1.config(show="")
            else:
                
                esifre1.config(show="*")
        
        
        def forgetpassword():
            ws = Tk()
            
            def x():
                email = eemail1.get()
                file = f"./users/{email}"
                
                entries = os.listdir('./users/')
                global g
                g = 0
                
    
                for entryx in entries:
                    if entryx == f"{email}.txt":
                        with open(file + '.txt', 'r') as f:
                            password = f.read() 
                        messagebox.showinfo("password", f"your password :{password}")
                        ws.destroy()
                        g = 1
                        
                if g != 1:
                    messagebox.showinfo("password", "email can't find")
                        
                        
                                

            
            ws.geometry("500x300")


            label  = Label(ws, text = "Enter your email:").place(x = 10, y = 10)
            eemail1 = Entry(ws, font = mycolor, fg = "blue", relief = FLAT, selectbackground = "yellow")
            
            eemail1.place(x=130, y=8)
            button = Button(ws, text = "find password" ,command=x).place(x = 360, y = 260 )
            ws.mainloop()
        
        entry_field_variable = tk.StringVar()
        lemail1 = Label(self, text="email:", bg = mycolor)
        lemail1.place(x=0, y=150)
        lsifre1 = Label(self, text="şifrə:", bg = mycolor)
        lsifre1.place(x=0, y=180)
        
        eemail1 = Entry(self, font = mycolor, fg = "blue", relief = FLAT, selectbackground = "yellow")
        esifre1 = Entry(self,font = mycolor , relief = FLAT, show = "*", selectbackground = "yellow")
        eemail1.place(x=80, y=150)
        esifre1.place(x=80, y=180)
        eemail1.insert(0, "email daxil edin")
        eemail1.configure(state=DISABLED)
        esifre1.insert(0, "sifre daxil edin")
        esifre1.configure(state=DISABLED, show = "")
        
        
        
        def on_click(event):
            eemail1.configure(state=NORMAL)
            eemail1.delete(0, END)
            eemail1.unbind('<Button-1>', on_click_id)
        def on_click2(event):
            esifre1.configure(state=NORMAL, show = "")
            esifre1.delete(0, END)
            esifre1.unbind('<Button-1>', on_click_id2)
            esifre1.config(show = "*")
        
        
        
        on_click_id = eemail1.bind('<Button-1>', on_click)
        on_click_id2 = esifre1.bind('<Button-1>', on_click2)
        
        button = tk.Button(self, text="Signup",
                           command=lambda: controller.show_frame("signup"))
        button.place(x = 0, y = 0)
        button2 = tk.Button(self, text="Menu",
                   command=lambda: controller.show_frame("menu"))
        button2.place(x = 80 , y = 0)
        CheckVar12 = IntVar()
        
        C12 = Checkbutton(self, text = "Şifrəni gör", variable = CheckVar12,background = mycolor,
                         onvalue = 1, offvalue = 0, height=2,
                         width = 14, command= showpassaword)

        C12.place(x = 300 , y = 185 )
        chkValue = IntVar()
        if savelogin == 1:
            chkValue.set(False)
        C123 = Checkbutton(self, text = "save login", variable = chkValue,background = mycolor,
                 onvalue = 1, offvalue = 0, height=2, 
                 width = 14, command= savelogin)
        C123.place(x = 300 , y = 5 )
        with open("savelogin" + '.txt', 'r') as file_object2:
            x = file_object2.read() 
        if x == "0":
            chkValue = tk.BooleanVar() 
            chkValue.set(False)
            C123.config(var = chkValue)
        else:
            chkValue = tk.BooleanVar() 
            chkValue.set(True)
            C123.config(var = chkValue) 
                       
        bqeydiyyat = Button(self, text="Login",command=save)
        bqeydiyyat.place(x=400, y=260)
        bqeydiyyat2 = Button(self, text="Forget password?" ,command= forgetpassword)
        bqeydiyyat2.place(x=250, y=260)
        
        
        



class signup(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        img4 = PhotoImage(file='xxx3.png')
        Label(self, image=img4, bg = mycolor).place(x=40, y=-30)
        self.configure(bg = mycolor)
       
        
        
        
       
        def save():
            k = 0
            email = eemail1.get()
            password = esifre1.get()
            global i

            file = f"./users/{email}"

            global id
            file_name2 = 'id'

            if email != "":
                for i in email:
                    if i == "@":
                        k = 1
                        i = 0
                        entries = os.listdir('./users/')
                        if len(password) >= 6:
                            for entryx in entries:
                                if entryx == f"{email}.txt":
                                    messagebox.showinfo("info","this email is used")
                                    i = 1
                                else:
                                    i = 0
                                    if i != 1:
                                        with open(file + '.txt', 'w') as file_object:
                                            file_object.write(password)  
                                            with open(file_name2 + '.txt', 'r') as file_object2:
                                                id = file_object2.read() 
                                                id = int(id)  
                                                with open(file_name2 + '.txt', 'w') as file_object2: 
                                                    id = id + 1
                                                    id = str(id)
                                                    file_object2.write(id)

                        else:
                            messagebox.showinfo("error", "your long of password  is small than 6") 
                            i = 1   
                if k != 1:
                    messagebox.showinfo("error", "your email haven't @ ")
                        
        
           
       
        def qeydiyyat():
            list = []
            global eemail
            global esifre
            global eyensifre
            eemail = eemail1.get()
            esifre = esifre1.get()
            eyensifre = eyensifre1.get()
            if eemail != "" and esifre != "" and esifre == eyensifre:
                    list.append(eemail)
                    list.append(esifre)
                    
                    def passoword():
                        save()
                        if i == 0:
                            messagebox.showinfo("Qeydiyyat", "Qeydiyyati ugurla tamanladiniz!")
                            controller.show_frame("login")
        
                            
                        
                    passoword()
            elif  eemail == "" and esifre != "":
                messagebox.showerror("xeta",
                                    "email daxil edin")
            elif eemail != "" and esifre == "":
                messagebox.showerror("xeta",
                                    " sifreni daxil edin")
            elif esifre != eyensifre:
                messagebox.showerror("xeta",
                                    " sifre yeninden sifre ile eyni deyil")
            else:
                messagebox.showerror("xeta",
                                     " sifreni ve email adresini daxil edin!")
         
        def showpassaword():
            if(CheckVar1.get()):
                eyensifre1.config(show="")
                esifre1.config(show="")

            else:
                eyensifre1.config(show="*")
                esifre1.config(show="*")

        lemail1 = Label(self, text="email:", bg = mycolor)
        lemail1.place(x=0, y=150)
        lsifre1 = Label(self, text="şifrə:", bg = mycolor)
        lsifre1.place(x=0, y=180)
        lyensifre1 = Label(self, text="yeniden şifrə:", bg = mycolor)
        lyensifre1.place(x=0, y=210)
        eemail1 = Entry(self, font = mycolor, fg = "blue", relief = FLAT, selectbackground = "yellow")
        esifre1 = Entry(self,font = mycolor , relief = FLAT, show = "*", selectbackground = "yellow")
        eemail1.place(x=80, y=150)
        esifre1.place(x=80, y=180)
        eemail1.insert(0, "email daxil edin")
        eemail1.configure(state=DISABLED)
        esifre1.insert(0, "sifre daxil edin")
        esifre1.configure(state=DISABLED, show = "")

        eyensifre1 = Entry(self,font = mycolor , selectbackground = "yellow", show = "*", relief = FLAT)
        eyensifre1.place(x=80, y=210)
        eyensifre1.insert(0, "yeniden sifre daxil edin")
        eyensifre1.configure(state=DISABLED, show = "")
        def on_click(event):
            eemail1.configure(state=NORMAL)
            eemail1.delete(0, END)
            eemail1.unbind('<Button-1>', on_click_id)
        def on_click2(event):
            esifre1.configure(state=NORMAL, show = "")
            esifre1.delete(0, END)
            esifre1.unbind('<Button-1>', on_click_id2)
            esifre1.config(show = "*")
        def on_click3(event):
            eyensifre1.configure(state=NORMAL, show = "")
            eyensifre1.delete(0, END)
            eyensifre1.unbind('<Button-1>', on_click_id3)
            eyensifre1.config(show = "*") 



        on_click_id = eemail1.bind('<Button-1>', on_click)
        on_click_id2 = esifre1.bind('<Button-1>', on_click2)
        on_click_id3 = eyensifre1.bind('<Button-1>', on_click3)
        bqeydiyyat = Button(self, text="Qeydiyyat", command = qeydiyyat)
        bqeydiyyat.place(x=400, y=260)
        
        
        
        
        
        CheckVar1 = IntVar()
        C1 = Checkbutton(self, text = "Şifrəni gör", variable = CheckVar1,background = mycolor,
                         onvalue = 1, offvalue = 0, height=2,
                         width = 14, command= showpassaword)

        C1.place(x = 300 , y = 185 )
        
        
        
        
        
        
        button = tk.Button(self, text="Login",
                           command=lambda: controller.show_frame("login"))
        button.place(x = 0 , y = 0)
        
        button2 = tk.Button(self, text="Menu",
                   command=lambda: controller.show_frame("menu"))
        button2.place(x = 70 , y = 0)
        
class exams(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        fontstyle = tkFont.Font(family="Arial", size=20)
        global chkValue
        global contra
        def showSelected():
            itm = lb.get(lb.curselection())
            var.set(itm)
        def loginout():
            
                        
            
            def xyz():
                with open("savelogin" + '.txt', 'r') as file_object2:
                    savelogin = file_object2.read() 
                    savelogin = int(savelogin)
                    with open('savelogin' + '.txt', 'w') as file_object2: 
                        savelogin = 0
                        savelogin = str(savelogin) 
                        file_object2.write(savelogin)  
                with open("iki" + '.txt', 'r') as file_object2:
                    iki = file_object2.read() 
                    iki = int(iki)
                    with open('iki' + '.txt', 'w') as file_object2: 
                        iki = 0
                        iki = str(iki) 
                        file_object2.write(iki)  
                        controller.show_frame("menu")
                        
                
            xyz()
           
            
            
            
            

        var =StringVar()
        lb = Listbox(self)
        lb.pack()
        lb.insert(1, "Fizika.Qüvvə")
        lb.insert(2, "Riyazziyat.KSQ")
        lb.insert(3, "Az- dili. Fonetika")
        lb.insert(4, "İnglis dili. BSQ")
        disp = Label(self, textvariable=var)
        disp.pack(pady=20)
        Button(self, text='Show Selected', command=showSelected).pack()
        
        button = tk.Button(self, text="go to exam",
                   command=lambda: controller.show_frame("examrules"))
        button.place(x = 360, y = 260)
        but = Button(self, text = "loginout" , command= loginout).place(x = 400 , y = 30)
        button2 = tk.Button(self, text="options",
                command=lambda: controller.show_frame("options"))
        button2.place(x = 400, y = 65)
        
        
        
        
class examrules(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        t11 = Label(self,
            text=" \n 1. İmtahan mövzusu imtahan suallarının əsas mövzusudur.\n 2. Açar sözlər cavablar əsnasında istifadə edilməlidir.\n 3. Açar sözlər yazıldığı kimi istifadə edilməlidir. ")
        t11.place(x=50, y=50)
        l1 = Label(self, text="Imtahan qaydaları")
        l1.place(x=200, y=20)
        b1 = Button(self, text=" Təsdiq edirəm", command= lambda: controller.show_frame("exam_physics"))
        b1.place(x=190, y=230)
        b2 = Button(self, text="Imtahanlara qayıt", command= lambda: controller.show_frame("exams"))
        b2.place(x=350 , y=260)
        
class exam_physics(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
       
        
        
        fontstyle = tkFont.Font(family="Arial", size=20)
        def increase():
            fontsize = fontstyle['size']
            l22['text'] = fontsize + 2
            if fontsize < 40:
                fontstyle.config(size=fontsize + 2)
        def decrease():
            fontsize = fontstyle['size']
            l22['text'] = fontsize - 2
            if fontsize > 4:
                fontstyle.config(size=fontsize - 2)
        om21 = tk.OptionMenu(self, tk.IntVar(), "Tenzimlemeler")
        om21.place(x=0, y=0)
        l22 = Label(self, text=" 20", font=fontstyle)
        l21 = Label(self, text=" Imtahan", font=fontstyle)
        b21 = Button(self, text=" böyütmə", width=30, command=increase)
        b22 = Button(self, text=" kiçiltmə", width=30, command=decrease)
        b21.place(x=0, y=0, width=100)
        b22.place(x=0, y=30, width=100)
        l22.place(x=100, y=0)
        l21.place(x=350, y=20)
        l23 = Label(self, text="Mövzu : Qüvvə,Nyuton qanunları", font=fontstyle)
        l23.place(x=230, y=80)
        l21 = Label(self, text=" Imtahan", font=fontstyle)
        l24_2 = Label(self, text="1.Açar sözlər", font=fontstyle)
        l24_2.place(x=600, y=150)
        l24 = Label(self, text="Nyutonun 1. qanunu", font=fontstyle)
        l24.place(x=0, y=150)
        e21 = Entry(self, bd=3)
        e21.place(x=0, y=200, width=300, height=70)
        lb21 = Listbox(self, font=fontstyle, height=4)
        lb21.insert(1, "Təcil")
        lb21.insert(2, "Kütlə")
        lb21.insert(3, "Sükunət")
        lb21.insert(4, "Ətalətlilik")
        lb21.place(x=600, y=200, width=150)
        l25 = Label(self, text="Nyutonun 2. qanunu", font=fontstyle)
        l25.place(x=0, y=350)
        l24_3 = Label(self, text="2.Açar sözlər", font=fontstyle)
        l24_3.place(x=600, y=350)
        lb22 = Listbox(self, font=fontstyle, height=4)
        e22 = Entry(self, bd=3)
        e22.place(x=0, y=400, width=300, height=70)
        lb22.insert(1, "Təsir")
        lb22.insert(2, "Çəki")
        lb22.insert(3, "İş")
        lb22.insert(4, "qanun")
        lb22.place(x=600, y=400, width=150)
        l26 = Label(self, text="Nyutonun 3. qanunu", font=fontstyle)
        l26.place(x=0, y=550)
        l24_4 = Label(self, text="3.Açar sözlər", font=fontstyle)
        l24_4.place(x=600, y=550)
        lb23 = Listbox(self, font=fontstyle, height=4)
        e23 = Entry(self, bd=3)
        e23.place(x=0, y=600, width=300, height=70)
        lb23.insert(1, "Əks təsir")
        lb23.insert(2, "Təsir")
        lb23.insert(3, "Güc")
        lb23.insert(4, "Qüvvə")
        lb23.place(x=600, y=600, width=150)
        
              
class options(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        fontstyle = tkFont.Font(family="Arial", size=20)
        
           
        button = tk.Button(self, text="exams",
                           command=lambda: controller.show_frame("exams"))
        button.place(x =400, y =65)
        b1 = Button(self, text="Change password", command= lambda: controller.show_frame("changepass"))

        b1.place(x = 30, y = 30)
              
              
              
class changepass(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        fontstyle = tkFont.Font(family="Arial", size=15)
        
        def duz():
            global e1, e2, e3
            e1 = ee1.get()
            e2 = ee2.get()
            e3 = ee3.get()
            if e1 == "" or e2 == "" or e3 =="":
                messagebox.showinfo("error", "pls enter the passwords")
            else:
                with open('last_save_user' + '.txt', 'r') as hah: 
                    lastemail = hah.read()
                    file = f"./users/{lastemail}"                    
                    
                    with open(file + '.txt', 'r') as hah2: 
                        lastpass = hah2.read()        
                if e1 != lastpass:
                    messagebox.showinfo("error", "your old password is false")
                else:
                    if e2 != e3:
                        messagebox.showinfo("error", "your new password and confirm isn't same")
                        
                    else:
                        if e1 == e2:
                            messagebox.showinfo("error", "your old password is same with new password")
                        else:
                            if len(e2) >= 6:
                                with open(file + '.txt', 'w') as hah3: 
                                    lastpass = hah3.write(e2)
                                    messagebox.showinfo("error", "your password changed")
                                    ee1.delete(0, END)
                                    ee2.delete(0, END)
                                    ee3.delete(0, END)
                                    controller.show_frame("options") 
                            else:
                                messagebox.showinfo("error", "your long of password  is small than 6") 
                                
                        
            
        
        l1 = Label(self, text = "old password:", font = fontstyle)
        l1.place(x = 63, y = 40)
        l2 = Label(self, text = "new password:", font = fontstyle)
        l2.place(x = 54, y = 70)
        l3 = Label(self, text = "again new password:", font = fontstyle)
        l3.place(x = 5, y = 100)
        ee1 = Entry(self)
        ee1.place(x =190, y = 40)
        ee2 = Entry(self)
        ee2.place(x =190, y = 70)
        ee3 = Entry(self)
        ee3.place(x =190, y = 100)

        b1 = Button(self, text = "submit", command= duz)
        b1.place(x = 400,  y = 260)
        def quit():
            self.destroy()
        
        b2 = Button(self, text="Options", command= lambda: controller.show_frame("options"))
        b2.place(x = 320,  y = 260)
                                                                             
if __name__ == "__main__":
    mycolor = "#c9effe"
    
    app = SampleApp()
    app.geometry("500x300")
    app.mainloop()
