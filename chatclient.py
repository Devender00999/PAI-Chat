from tkinter import*  
from threading import *
from tkinter import messagebox
b=50

#......................creating class................................................
class client:
    def chattingclient(self):
        if True:
            #.......................................creating socket for different pc...................
             
            import netifaces
            gateways = netifaces.gateways()
            default_gateway = gateways['default'][netifaces.AF_INET][0]
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            
            port=12345
            try:
                #s.connect((default_gateway, port))#uncomment this line if you want to text between Two Computer
                s.connect(("192.168.1.105",port))#use this and change this ip with yours
            except:
                pass
                
            #.............................................same pc...................................
            host=socket.gethostname()    
            
            #....................................function for sending..................................
            def sender(*args):
                global b,ntext,count,pos
                print(b)
                if True:
                    sendata=data.get()
                    #print(val.get())
                    message = Message(canvas,text=sendata,width=350,pady=0,font=("gabriola",15),fg='black',bg="white")
                    canvas.create_window(380,b,window=message,anchor=NE)
                    b = b+message.winfo_reqheight()+10
                    canvas.yview()
                    data.set("")
                    scrollfun(canvas)
                    canvas.yview_moveto(1.0)
                    try:
                        s.send(bytes(sendata,'utf-8'))
                    except:
                        messagebox.showerror("Error","server not ready !")
                        win.destroy()
                else:
                    messagebox.showerror("Error","server not refady\n your message cannot send")
                    win.destroy()
            
            def move(event):
                pass
            #................function for recieving.......................
            def receiver():
                global b
                print("Hi")

                while True:
                    try:
                        data1=str(s.recv(1024)).strip('b').strip('\'')
                        message = Message(canvas,text=data1,width=350,pady=0,font=("gabriola",15),fg='black',bg="white")
                        canvas.create_window(1,b,window=message,anchor=NW)
                        b = b+message.winfo_reqheight()+10
                        scrollfun(canvas)
                        canvas.yview_moveto(1.0)
                        data.set("")
                    except:
                        break
            #.............................GUI...................................
            win = Tk()
            win.iconbitmap("icons/chat.ico")
            win.title("PAI Chat")
            win.geometry("400x600")
            frame=Frame(win,width=400,height=600)
            frame.place(x=0,y=0)
            canvas=Canvas(frame,bg='#FFFFFF',width=380,height=555)
            canvas.bind_all("<MouseWheel>",move)
            vbar=Scrollbar(frame,orient=VERTICAL,elementborderwidth=-3)
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
            btn2=Button(win,command=sender,relief = FLAT,text="send",image=sendphoto)
            btn2.image=sendphoto
            btn2.place(x=355,y=560)

            rec_thread=Thread(target=receiver)
        
            rec_thread.start()
            win.mainloop()
        else:
            pass
ob=client()
ob.chattingclient()
        

