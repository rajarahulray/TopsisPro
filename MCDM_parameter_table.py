# -*- coding: utf-8 -*-

"""
Seprate file to test the design and organize the "parameter data" of different networks......

"""
print(__doc__);

from tkinter import Tk, Label, Button, Entry, Canvas, Frame, Scrollbar, messagebox

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

y_inc = 0;

net = int(input("Enter the no. of networks"));
r = Tk();
if net <=35 :
    
    #canvas = Canvas(r, background=None);
    #frame = Frame(canvas, background= None);
    #scroll = Scrollbar(r, orient='vertical', command=canvas.yview);
    
    
    for i in range(net):
         l = Label(r, text = "network = {}".format(i+1)).place(x = 10, y = 10 + y_inc);
         #l.config(x = 10, y = 10 + y_inc);
         
         eth = Entry(r);
         lth.append(eth);
         eth.place(x = 100, y = 10 + y_inc);
         
         eth = Entry(r);
         lj.append(eth);
         eth.place(x = 240, y = 10 + y_inc);
         
         eth = Entry(r);
         ld.append(eth);
         eth.place(x = 380, y = 10 + y_inc);
         
         eth = Entry(r);
         llr.append(eth);
         eth.place(x = 520, y = 10 + y_inc);
         
         eth = Entry(r);
         lc.append(eth);
         eth.place(x = 660, y = 10 + y_inc);
         
         y_inc += 20;
    
         
    
    Button(r, text = "0 Kelvin", command = pr).place(x = 400, y = 50 + y_inc);
    
    
    
    #canvas.configure(yscrollcommand=scroll.set);
    #scroll.pack(side="right", fill="y");
    #canvas.pack(fill="both", expand=True)
    #canvas.create_window((4, 4), window=frame, anchor="nw");
    #frame.bind('<Configure>', lambda event, canvas = canvas: onFrameConfigure(canvas));
    
    #Canvas and frame are not affecting the root for scrollthe region....
    
    r.geometry('800x{}'.format(y_inc + 90));
    
    
    print(y_inc);

else:
    r.iconify();
    messagebox.showinfo("Info", "Limit is 35 networks");
    r.destroy();

r.mainloop();