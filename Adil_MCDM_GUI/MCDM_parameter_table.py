# -*- coding: utf-8 -*-

"""
Seprate file to test the design and organize the "parameter data" of different networks......

"""
print(__doc__);

from tkinter import Tk, Label, Button, Entry, Canvas, Frame, Scrollbar, messagebox

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"));

def pr():
    for i in range(net):
        print("Lth: ",lth[i].get());
        print("Lj: ",lj[i].get());
        print("Ld: ",ld[i].get());
        print("Llr: ",llr[i].get());
        print("Lc: ",lc[i].get());
        print("________________________________________");

#Data Structures.....
lth =[];
lj = [];
ld = [];
llr = [];
lc = [];

x_inc = 125;
y_inc = 0;
temp_char = "This a test for just testing that a test is working....";
le = len(temp_char) * 2;

net = int(input("Enter the no. of networks"));
r = Tk();
if net <=30 :
    
    canvas = Canvas(r);
    frame = Frame(canvas);
    scroll = Scrollbar(r, orient='vertical', command=canvas.yview);
    
    
    for i in range(net):
         l = Label(r);
         l.configure(background = "Blue");
         l.place(x = 10, y = 40 + y_inc);
         #l.config(x = 10, y = 40 + y_inc);
         
         eth = Entry(r);
         lth.append(eth);
         eth.place(x = le + x_inc  , y = 40 + y_inc);
         
         eth = Entry(r);
         lj.append(eth);
         eth.place(x = le + 2 * x_inc  , y = 40 + y_inc);
         
         eth = Entry(r);
         ld.append(eth);
         eth.place(x = le + 3 * x_inc , y = 40 + y_inc);
         
         eth = Entry(r);
         llr.append(eth);
         eth.place(x = le + 4 * x_inc , y = 40 + y_inc);
         
         eth = Entry(r);
         lc.append(eth);
         eth.place(x = le + 5 * x_inc , y = 40 + y_inc);
         
         y_inc += 20;
    
         
    
    Button(r, text = "0 Kelvin", command = pr).place(x = 400, y = 90 + y_inc);
    
    
    
    canvas.configure(yscrollcommand=scroll.set);
    scroll.pack(side="right", fill="y");
    canvas.pack(fill="both", expand=True)
    canvas.create_window((4, 4), window=frame, anchor="nw");
    frame.bind('<Configure>', lambda event, canvas = canvas: onFrameConfigure(canvas));
    
    #Canvas and frame are not affecting the root for scrollthe region....
    
    r.geometry('{}x{}'.format(le + 7 * x_inc, y_inc + 130));
    
    
    print(y_inc);

else:
    r.iconify();
    messagebox.showinfo("Info", "Limit is 35 networks");
    r.destroy();

#print("WInfo : ", r.winfo_x(), r.winfo_y());
r.bind('<Motion>', motion)
print(r.winfo_pointerxy());
r.mainloop();

