from tkinter import *
from threading import *
b=50


#...............................creating class......................................................................#
class server:
    def chattingserver(self):
        import socket                                    #..........create socket
        s=socket.socket()
        hostname=socket.gethostname()
        host=""
        host1=socket.gethostbyname(hostname)
        port=12345
        s.bind((host,port))
        s.listen(5)
        
        #............................create popup for host name .......................................
        win=Tk()
        win.geometry("400x350")
        win.iconbitmap("icons/chat.ico")
        win.title("Sender Information")
        win.config(bg="skyblue")
        lb=Message(win,text="host name =",font="times 14",width="100",bg="skyblue")
        lb.place(x=10,y=40)

        lb=Message(win,text=hostname,font="times 14",width="200",bg="skyblue")
        lb.place(x=120,y=40)

        lb=Message(win,text="Ip address =  ",font="times 14",width="100",bg="skyblue")
        lb.place(x=10,y=90)

        lb=Message(win,text=host1,font="times 14",width="200",bg="skyblue")
        lb.place(x=110,y=90)

        lb=Message(win,text="Close window to start server .... ",font="times 14",width="200",bg="white")
        lb.place(x=10,y=150)
        win.mainloop()
        c,addr=s.accept()
        
        print('got connection  from',addr)
        
        #...............................creating function for sending...........................................
        def sender(*args):
            global b,ntext,count,pos
            sendata=data.get()
            message = Message(canvas,text=sendata,width=350,pady=0,font=("gabriola",15),fg="black",bg='white')
            canvas.create_window(380,b,window=message,anchor=E)
            b = b+message.winfo_reqheight()+10
            
            canvas.yview()
            data.set("")
            scrollfun(canvas)
            canvas.yview_moveto(1.0)
            c.send(bytes(sendata,'utf-8'))
            
        
        #..................................................creating function for recieve.........................
        def receiver():
            global b
            val = StringVar()
            b=50
            
            while True:
                try:
                    data1=str(c.recv(1024)).strip('b').strip('\'')
                    
                    message = Message(canvas,text=data1,width=350,pady=0,font=("gabriola",15),fg="black",bg='white')
                    canvas.create_window(0,b,window=message,anchor=W)
                    b = b+message.winfo_reqheight()+10
                    data.set("")
                    scrollfun(canvas)
                    canvas.yview_moveto(1.0)
                    
                except:
                    break
        #.....................................creating GUI........................................................
        win = Tk()
        win.geometry("400x600")
        win.iconbitmap("icons/chat.ico")
        win.title("PAI Chat")
        
       
        global count
        count=1
        frame=Frame(win,width=400,height=600)
        frame.place(x=0,y=0)
        canvas=Canvas(frame,bg='#FFFFFF',width=380,height=555,scrollregion=(0, 0, "2000i", "2000i"))
        vbar=Scrollbar(frame,orient=VERTICAL,elementborderwidth=-3,bg="red")
        vbar.pack(side=RIGHT,fill=Y)
        def scrollfun(canvas):
            canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.bind("<Configure>",lambda event,canvas=canvas:scrollfun(canvas))        
        vbar.config(command=canvas.yview)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(side=TOP,expand=True,fill=BOTH)

        data=StringVar()
        textbox=Entry(win,bg="white",width=35,font="Times 15",textvariable=data)
        textbox.place(x=6,y=565)
        textbox.bind("<Return>",sender)
        sendphoto = PhotoImage(file="icons\sendButton.png")
        btn2=Button(win,command=sender,relief = FLAT,image=sendphoto)
        btn2.place(x=355,y=560)

        rec_thread=Thread(target=receiver)
        
        rec_thread.start()
        win.mainloop()
ob=server()
ob.chattingserver()
        

