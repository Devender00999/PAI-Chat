#.............................importing module......................................
from tkinter import filedialog
from tkinter import messagebox
import socket
import os
from tkinter import ttk
from tkinter import*
from tkinter import messagebox
from threading import*
import time
global filename,size_bytes
global addr
#..............filedialog.................................................................................
class fileserver:
    def fileserverfun(self):
        Tk().withdraw()
        filename=filedialog.askopenfilename(initialdir="/",title="select file",filetypes=(("Text files","*.txt"),("jpeg files","*.jpg"),("all files","*.*")))
        print(filename)
        f1=os.path.basename(filename)
        print(f1)
        size=os.path.getsize(filename)
        size_bytes=str(size)+" Bytes"
        print(size)

        #...............................progress_bar.....................
        def pro_bar_fun():
            for i in range(1,100):
                time.sleep(0.01)
                pro["value"]=i
                pro.update()
            pro_bar_fun()
        def sharing():
            pass
        # Establish connection with client. and sharing file   
        def connection():
           while True:
                conn, addr = s.accept()     
                print ('Got connection from', addr)
                conn.send(bytes(f1,encoding='utf-8'))
                label7 = Message(win, text="connected to          ", bg="skyblue", width=350, font="times 12")
                label7.place(x=0, y=165)
                label6 = Message(win, text=str(addr), bg="skyblue", width=350, font="times 12")

                label6.place(x=130, y=165)
    
                f = open(filename,'rb')
                l = f.read(1024)
                #for i in f:

                while (l):
                      conn.send(l)

      
                      l = f.read(1024)
                f.close()
 
                print('Done sending')
                conn.send(bytes('Thank you for connecting',encoding='utf-8'))
        
                conn.close()

        #........................................................starting socket or comminucatin establising.........................		
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        host="192.168.1.105"
        port =60000
        s.bind((host,port))
        s.listen(5)
        host=socket.gethostname()
        hostname=socket.gethostbyname(host)
        print("server working...")
        win=Tk()
        win.title("PAI Chat")

        win.iconbitmap("icons\chat.ico")
        win.config(bg="skyblue")
        win.geometry("350x450")

        label=Message(win,text=filename,bg='skyblue',width=350,font="times 12")
        label.place(x=0,y=50)
        labe2=Message(win,text=f1,bg='skyblue',width=350,font="times 12")
        labe2.place(x=0,y=70)
        label3=Message(win,text=size_bytes,bg='skyblue',width=350,font="times 12")
        label3.place(x=0,y=110)
        label4=Message(win,text="server started....",bg='skyblue',width=350,font="times 12")
        label4.place(x=0,y=140)
        label5=Message(win,text="waiting for reciver.....",bg='skyblue',width=350,font="times 12")
        label5.place(x=0,y=170)
        pro=ttk.Progressbar(win,orient='horizontal',length=100,mode='det')
        pro.place(x=200,y=170)
        
        thread_pro=Thread(target=pro_bar_fun)
        thread_pro.start()
        thread_con=Thread(target=connection)
        thread_con.start()

        win.mainloop()
obj=fileserver()
obj.fileserverfun()


    
    
