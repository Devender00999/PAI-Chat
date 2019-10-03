
#..............................importing module............................
import socket                   
import os
from tkinter import *
from tkinter import messagebox
class client:
    def fileclientfun(self):
    
        s = socket.socket()             
        host = socket.gethostname()

        port = 60000                    
        import netifaces
        gateways = netifaces.gateways()
        default_gateway = gateways['default'][netifaces.AF_INET][0]
        try:
            #s.connect((default_gateway, port))
            s.connect(("192.168.1.105", port))
        except:
            Tk().withdraw()
            messagebox.showerror("Error","server not ready !")
            
            

        filename=str(s.recv(1024)).strip('b').strip('\'')#..................receiving filepath...........
        print(filename)


        with open(filename, 'wb') as f:
            print ('file opened')
            while True:
                print('receiving data...')
                data = s.recv(1024)
                f.write(data)
        
                if not data:
                    break
       
        

        f.close()
        print('Successfully get the file')
        data=s.recv(1024)
        print(data)
        s.close()
        size=os.path.getsize(filename)
        size_bytes=str(size)+" Bytes"
        #..............................popupGui........................................................
        def ok():
            win1.destroy()
        win1=Tk()
        win1.geometry("350x450")
        win1.config(bg="skyblue")
        win1.title("PAI Chat")
        win1.iconbitmap("icons/chat.ico")
        label = Message(win1, text="filename", bg='skyblue', width=350, font="times 12")
        label.place(x=0, y=50)
        label = Message(win1, text=filename, bg='skyblue', width=350, font="times 12")
        label.place(x=150, y=50)
        labe2 = Message(win1, text="Size of the file", bg='skyblue', width=350, font="times 12")
        labe2.place(x=0, y=90)
        labe2 = Message(win1, text=size_bytes, bg='skyblue', width=350, font="times 12")
        labe2.place(x=150, y=90)
        
        label4 = Message(win1, text="connected to ", bg='skyblue', width=350, font="times 12")
        label4.place(x=0, y=110)
        label5 = Message(win1, text=host, bg='skyblue', width=350, font="times 12")
        label5.place(x=150, y=110)
        label10 = Message(win1, text="recieving", bg="skyblue", font="times 12", width=100)
        label10.place(x=0, y=140)
        label10 = Message(win1, text="100", bg="skyblue", font="times 12", width=100)
        label10.place(x=180, y=140)
        label11 = Message(win1, text="%", bg="skyblue", font="times 12", width=350)
        label11.place(x=230, y=140)
        btn=Button(win1,text="ok",font=" times 15",command=ok,bg="tomato")
        btn.place(x=170,y=200)
        print('connection closed')

obj=client()
obj.fileclientfun()
