from tkinter import*
from PIL import ImageTk,Image

window=Tk()
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
window.state("zoomed")
window.title("Login and Registration Page")

LoginPage=Frame(window)
RegistrationPage=Frame(window)

for frame in (LoginPage,RegistrationPage):
    frame.grid(row=0,column=0,sticky="nsew")

def show_frame(frame):
    frame.tkraise()

show_frame(LoginPage)

#.....................................#
design_frame1=Listbox(LoginPage,bg="#0c71b9",width=115,height=50,highlightthickness=0,borderwidth=0)
design_frame1.place(x=0,y=0)

design_frame2=Listbox(LoginPage,bg="#0096FF",width=115,height=50,highlightthickness=0,borderwidth=0)
design_frame2.place(x=676,y=0)

design_frame3=Listbox(LoginPage,bg="black",width=100,height=33,highlightthickness=0,borderwidth=0)
design_frame3.place(x=75,y=106)

design_frame4=Listbox(LoginPage,bg="#f8f8f8",width=100,height=33,highlightthickness=0,borderwidth=0)
design_frame4.place(x=676,y=106)

#........................................#
email_entry=Entry(design_frame4,fg="black",font=("yu gothic ui semibold",12),highlightthickness=2)
email_entry.place(x=134,y=170,width=256,height=34)
email_entry.config(highlightbackground="black",highlightcolor="black")
email_label=Label(design_frame4,text="Email Account",fg="black",bg="#f8f8f8",font=("yu gothic ui semibold",12,"bold"))
email_label.place(x=130,y=140)

#........................................#
password_entry1=Entry(design_frame4,fg="black",font=("yu gothic ui semibold",12),highlightthickness=2)
password_entry1.place(x=134,y=250,width=256,height=34)
password_entry1.config(highlightbackground="black",highlightcolor="black")
password_label=Label(design_frame4,text="Password",fg="black",bg="#f8f8f8",font=("yu gothic ui semibold",12,"bold"))
password_label.place(x=130,y=220)

#.........................................#
def password_command():
    if password_entry1.cget("show")==".":
        password_entry1.config(show="")
    else:
        password_entry1.config(show=".")

CheckButton=Checkbutton(design_frame4,bg="#f8f8f8",command=password_command,text="Show Password")
CheckButton.place(x=140,y=288)

#....................#

SignUp_button=Button(LoginPage,text="Sign Up",font=("yu gothic ui semibold",12),bg="#f8f8f8",fg="black",
                     command=lambda:show_frame(RegistrationPage),borderwidth=0,activebackground="#1b87d2",cursor="hand2")
SignUp_button.place(x=1100,y=175)

#.........................#

welcome_label=Label(design_frame4,text="Welcome",font=("arial",25,"bold"),bg="#f8f8f8")
welcome_label.place(x=230,y=15)

#.................................#

login_button=Button(LoginPage,text="Login",font=("yu gothic ui semibold",12),bg="#f8f8f8",fg="black",
                     borderwidth=0,activebackground="#1b87d2",cursor="hand2")
login_button.place(x=845,y=175)
login_line=Canvas(LoginPage,width=60,height=5,bg="#1b87d2")
login_line.place(x=840,y=203)

#.....................................#

loginBtn1=Button(design_frame4,fg="#f8f8f8",text="Login",bg="#1b87d2",font=("yu gothic ui semibold",15),
                 cursor="hand2",activebackground="#1b87d2")
loginBtn1.place(x=133,y=340,width=256,height=50)



#........................................................#

side_image=Image.open("system.jpg")
photo=ImageTk.PhotoImage(side_image)
side_image_label=Label(design_frame3,image=photo,bg="#1e85d0")
side_image_label.image=photo
side_image_label.place(x=15,y=50)

#......................................#
def forgot_password():
    win=Toplevel()
    window_width=350
    window_height=350
    screen_width=win.winfo_screenwidth()
    screen_height=win.winfo_screenheight()
    position_top=int(screen_height/4-window_height/4)
    position_right=int(screen_width/2-window_width/2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win.title("Forget Password")
    win.configure(background="#f8f8f8")
    win.resizable(0,0)

    #..........................#

    email_entry2= Entry(win, fg="black", font=("yu gothic ui semibold", 12), highlightthickness=2)
    email_entry2.place(x=40, y=30, width=256, height=34)
    email_entry2.config(highlightbackground="black", highlightcolor="black")
    email_label2= Label(win, text="Email Account", fg="black", bg="#f8f8f8",
                        font=("yu gothic ui semibold", 12, "bold"))
    email_label2.place(x=40, y=0)

    #............................#
    new_password_entry= Entry(win, fg="black", font=("yu gothic ui semibold", 12), highlightthickness=2)
    new_password_entry.place(x=40, y=110, width=256, height=34)
    new_password_entry.config(highlightbackground="black", highlightcolor="black")
    new_password_label = Label(win, text=" New Password", fg="black", bg="#f8f8f8",
                           font=("yu gothic ui semibold", 12, "bold"))
    new_password_label.place(x=40, y=80)

    #...........................#

    confirm_password_entry = Entry(win, fg="black", font=("yu gothic ui semibold", 12), highlightthickness=2)
    confirm_password_entry.place(x=40, y=190, width=256, height=34)
    confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
    confirm_password_label = Label(win, text="Confirm Password", fg="black", bg="#f8f8f8",
                               font=("yu gothic ui semibold", 12, "bold"))
    confirm_password_label.place(x=40, y=160)

    #........................#

    Update_pass= Button(win,fg="#f8f8f8",text="Update Password",bg="#1b87d2", font=("yu gothic ui semibold", 14),
                        cursor="hand2",activebackground="#1b87d2")
    Update_pass.place(x=40, y=240, width=256, height=50)

forgot_password=Button(design_frame4,text="Forget Password",font=("yu gothic ui",8,"bold underline"),
                       bg="#f8f8f8",borderwidth=0,activebackground="#f8f8f8",command=forgot_password,cursor="hand2")
forgot_password.place(x=290,y=290)

#.........................................#

design_frame5=Listbox(RegistrationPage,bg="#0c71b9",width=115,height=50,highlightthickness=0,borderwidth=0)
design_frame5.place(x=0,y=0)

design_frame6=Listbox(RegistrationPage,bg="#0096FF",width=115,height=50,highlightthickness=0,borderwidth=0)
design_frame6.place(x=676,y=0)

design_frame7=Listbox(RegistrationPage,bg="black",width=100,height=33,highlightthickness=0,borderwidth=0)
design_frame7.place(x=75,y=106)

design_frame8=Listbox(RegistrationPage,bg="#f8f8f8",width=100,height=33,highlightthickness=0,borderwidth=0)
design_frame8.place(x=676,y=106)

#...............................#

name_entry= Entry(design_frame8,fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
name_entry.place(x=284, y=150, width=286, height=34)
name_entry.config(highlightbackground="black", highlightcolor="black")
name_label= Label(design_frame8,text="Full Name", fg="black", bg="#f8f8f8",
                        font=("yu gothic ui semibold", 11, "bold"))
name_label.place(x=280, y=120)

#..............................................#

email_entry= Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
email_entry.place(x=284, y=220, width=286, height=34)
email_entry.config(highlightbackground="black", highlightcolor="black")
email_label= Label(design_frame8, text="Email", fg="black", bg="#f8f8f8",
                     font=("yu gothic ui semibold", 11, "bold"))
email_label.place(x=280, y=190)

#.........................................#

password_entry=Entry(design_frame8,fg="#a7a7a7",font=("yu gothic ui semibold",12),highlightthickness=2)
password_entry.place(x=284,y=295,width=286,height=34)
password_entry.config(highlightbackground="black",highlightcolor="black")
password_label=Label(design_frame8,text="Password",fg="black",bg="#f8f8f8",font=("yu gothic ui semibold",12,"bold"))
password_label.place(x=280,y=265)

#..................................#

def password_command2():
    if password_entry.cget("show")==".":
        password_entry.config(show="")
    else:
        password_entry.config(show=".")

checkButton=Checkbutton(design_frame8,fg="black",command=password_command2,text="Show Password")
checkButton.place(x=290,y=330)

#......................................#

confirm_password_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
confirm_password_entry.place(x=284, y=385, width=286, height=34)
confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
confirm_password_label = Label(design_frame8, text="Confirm Password", fg="black", bg="#f8f8f8",
                               font=("yu gothic ui semibold", 12, "bold"))
confirm_password_label.place(x=280, y=355)

#.................................#

SignUp_Button=Button(RegistrationPage,text="Sign Up",font=("yu gothic ui semibold",12),bg="#f8f8f8",fg="black",
                     command=lambda:show_frame(LoginPage),borderwidth=0,activebackground="#1b87d2",cursor="hand2")
SignUp_Button.place(x=1100,y=175)

SignUp_line=Canvas(RegistrationPage,width=60,height=5,bg="#1b87d2")
SignUp_line.place(x=1100,y=203)

#.................................#

welcome_label=Label(design_frame8,text="Welcome",font=("arial",25,"bold"),bg="#f8f8f8")
welcome_label.place(x=230,y=15)

#.......................................#

login_button=Button(RegistrationPage,text="Login",font=("yu gothic ui semibold",12),bg="#f8f8f8",fg="black",
                     borderwidth=0,activebackground="#1b87d2",command=lambda:show_frame(LoginPage),cursor="hand2")
login_button.place(x=845,y=175)

#................................#

SignUp2=Button(design_frame8,fg="#f8f8f8",text="Sign Up",bg="#1b87d2",font=("yu gothic ui bold",15),
                      cursor="hand2",activebackground="#1b87d2")
SignUp2.place(x=285,y=435,width=286,height=50)

#.......................................#

side_image=Image.open("system.jpg")
photo=ImageTk.PhotoImage(side_image)
side_image_label=Label(design_frame7,image=photo,bg="#1e85d0")
side_image_label.image=photo
side_image_label.place(x=15,y=50)

window.mainloop()
