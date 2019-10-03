from tkinter import *
#.................................................method for receiving................................................................#
def receiveclient():
    def chattingreceiver():
        win.destroy()
        import chatclient
    def sharingrecever():
        import fileclient    
    #....................................GUI for receiving message or file....................................................#
    frame1=Frame(frame,width=400,height=600,bg="white")
    frame1.pack()
    
    sphoto = PhotoImage(file="icons/file.png")
    send = Button(frame1,bd=0,relief=FLAT,image=sphoto,bg="white",command=sharingrecever)
    send.place(x=150,y=200)
    label1=Label(frame1,text="File",font="times 20 ",bg="white",fg="black")
    label1.place(x=170,y=310)
    rphoto = PhotoImage(file="icons/chat.png")
    receive = Button(frame1,bd=0,relief=FLAT,image=rphoto,bg="white",command=chattingreceiver)
    receive.place(x=150,y=350)
    label2=Label(frame1,text="Message",font="times 20 ",bg="white",fg="black")
    label2.place(x=165,y=470)
    img1=PhotoImage(file="icons/logo.png")
    label=Label(frame1,image=img1,bg="white")
    label.place(x=25,y=0)
    win.mainloop()
    win.quit()
#........................................................................method for sending...............................................................................#
def sendserver():
    win.quit()
    def chattingsender():
        win.destroy()
        import chatserver
    def sharingsender():
        import fileserver
     #...............................................................GUI  for sending message or file......................................................#   
    frame1=Frame(frame,width=400,height=600,bg="white")
    frame1.pack()
    
    sphoto = PhotoImage(file="icons/file.png")
    send = Button(frame1,image=sphoto,bg="white",command=sharingsender,relief=FLAT,bd=0)
    send.place(x=150,y=200)
    label1=Label(frame1,text="File",font="times 20 ",bg="white",fg="black")
    label1.place(x=170,y=310)
    rphoto = PhotoImage(file="icons/chat.png")
    receive = Button(frame1,image=rphoto,bg="white",command=chattingsender,relief=FLAT,bd=0)
    receive.place(x=150,y=350)
    label2=Label(frame1,text="Message",font="times 20 ",bg="white",fg="black")
    label2.place(x=165,y=470)
    img1=PhotoImage(file="icons/logo.png")
    label=Label(frame1,image=img1,bg="white")
    label.place(x=25,y=0)
    win.mainloop()

    
    

    
    
#............................................................GUI  for send and recevie option..................................................#   
win = Tk()
win.geometry("400x600")
win.title("Pai Chat")
win.iconbitmap("icons/chat.ico")
win.config(bg="white")
frame=Frame(win,width="400",height="600",bg="white")
frame.pack(pady="10")

sphoto = PhotoImage(file="icons/send.png")
send = Button(frame,image=sphoto,bg="white",bd=0,command=sendserver)
send.place(x=150,y=200)
label1=Label(frame,text="Send",font="times 20 ",bg="white",fg="black")
label1.place(x=170,y=310)
rphoto = PhotoImage(file="icons/receive.png")
receive = Button(frame,image=rphoto,bg="white",bd=0,command=receiveclient)
receive.place(x=150,y=350)
label2=Label(frame,text="Recieve",font="times 20 ",bg="white",fg="black")
label2.place(x=165,y=470)
img1=PhotoImage(file="icons/logo.png")
label=Label(frame,image=img1,bg="white")
label.place(x=25,y=0)
win.mainloop()
