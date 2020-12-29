from tkinter import *
import smtplib
def screen2_delete():
    screen2.destroy()



def error():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Error")
    screen2.geometry("720x560")
    Label(screen2, text = "somethings goes wrong , try again....",fg = "red" , width = 300, height = 25).pack()
    Button(screen2, text = "Ok", command = screen2_delete).pack()

def screen3_delete():
    screen3.destroy()

def error_2():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Error")
    screen3.geometry("300x150")
    Label(screen3, text = "all fields should be compited...",fg = "red" , width = 300, height = 25).pack()
    Button(screen3, text ="ok", command = screen3_delete).pack()


def send():
    try:
        username = username_entry.get()
        password = password_entry.get()
        to = receiver_entry.get()
        subject = subject_entry.get()
        body = body_entry.get()
        if username == "" or password == "" or to == "" or subject == "" or body == "":
            error_2()
            return
        else:
            final_message = 'Subject: {}\n\n{}'.format(subject,body )
            server = smtplib.SMTP('smtp@gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(username, to, final_message)
            notif.config(text = "Email Has been send", fg = "green")
    except:
        error()



def reset():
    username_entry.delete(0,'end')
    password_entry.delete(0 , "end")
    receiver_entry.delete(0, "end")
    subject_entry.delete(0,"end")
    body_entry.delete(0,"end")



#main screen
def main_screen():
    global screen
    screen = Tk()
    screen.title("Email Sender ")
    screen.geometry("720x560")
    #graphics
    Label(screen, text = "Django Email Sender", bg = "grey", font=("calibri", 15)).grid(row = 1, sticky= N)
    Label(screen , text = "Welcome to django Email sender").grid(row = 2, sticky = W)
    #email script
    Label(screen , text = "Email", width = 10 , height = 2).grid(row = 4, sticky = W)
    Label(screen , text = "password", width = 10 , height = 2).grid(row = 5, sticky = W)
    Label(screen, text="To", width=10, height=2).grid(row=6, sticky=W)
    Label(screen, text="Subject", width=10, height=2).grid(row=7, sticky=W)
    Label(screen, text="Body", width=10, height=2).grid(row=8, sticky=W)
    global notif
    notif = Label(screen , text = "")
    notif.grid(row = 11 , sticky = W )
    #variables
    username = StringVar()
    password = StringVar()
    receiver = StringVar()
    subject = StringVar()
    body = StringVar()
    #Entries
    global username_entry
    global password_entry
    global receiver_entry
    global subject_entry
    global body_entry
    username_entry = Entry(screen , textvariable = username)
    username_entry.grid(row = 4, column = 5)
    password_entry = Entry(screen,show = "****", textvariable = password)
    password_entry.grid(row = 5 , column = 5)
    receiver_entry = Entry(screen, textvariable = receiver)
    receiver_entry.grid(row = 6, column = 5)
    subject_entry = Entry(screen, textvariable = subject)
    subject_entry.grid(row = 7, column = 5 )
    body_entry = Entry(screen, textvariable = body)
    body_entry.grid(row = 8, column = 5 )
    Button(screen, text = "Send ", command = send).grid(row = 9, sticky = W , pady = 15, padx = 5)
    Button(screen, text="Reset ", command=reset ).grid(row=9,column = 2, sticky=E, pady=15, padx=0)




    screen.mainloop()
main_screen()

