# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:37:48 2017

@author: stpl
"""

from tkinter import Tk, Label, Button, Entry, Canvas, Frame, Scrollbar, messagebox
#from functools import partial

#def slpash():

d = {};
l = [];
l_net = [];

def pr(lth, lj, ld, llr, lc, n):
    for i in range(int(n)):
        print("Lth: ",lth[i].get());
        print("Lj: ",lj[i].get());
        print("Ld: ",ld[i].get());
        print("Llr: ",llr[i].get());
        print("Lc: ",lc[i].get());
        print("________________________________________");
        for i in range(len(l_net)):
            d[l_net[i]] = [float(lth[i].get()), float(lj[i].get()), float(ld[i].get()), float(llr[i].get()), float(lc[i].get())];
        
     #summation of all columns(parameters) w.r.t networks and their square_root
    uroot = 0;
    u_root_l = [];
    for i in range(5):
        for k in range(len(l_net) -1):
            uroot += d[l_net[k]][i];
        u_root_l.append(uroot);
        uroot = 0;


    for i in range(len(u_root_l)):
        u_root_l[i] = u_root_l[i]**0.5;
    
    print("u_root_l: ",u_root_l);
    
    #step 1(b):Dividing each element of columns with the corresponding value in l[]:
    for i in range(5):
        for k in range(len(l_net) -1):
            d[l_net[k]][i] /=u_root_l[i];
            #print("________",d[k][i]);
     
    #Step 2: Multiplying weights with columns in d:
    for i in range(5):
        for k in range(len(l_net) -1):
            d[l_net[k]][i] *= d['Weight'][i];
    print("\nDictionary after multiplying with weights : ", d);
    
    ideal = [];
    non_ideal = [];
    u_root_l = []; #reusing u_root_l for computing ideal and then non-ideal solution...
    
    #computing ideal solution:
    for i in range(len(l_net) - 1):
        u_root_l.append(d[l_net[i]][0]); #reusing u_root_l for computing ideal and then non-ideal solution...
     
    ideal.append(max(u_root_l));
    u_root_l = [];
    
    for i in range(1,5):
        for k in range(len(l_net) - 1):
            u_root_l.append(d[l_net[k]][i]);
        ideal.append(min(u_root_l));
    u_root_l = [];
    
    #computing non_ideal solution:
    for i in range(len(l_net) - 1):
        u_root_l.append(d[l_net[i]][0]); #reusing u_root_l for computing ideal and then non-ideal solution...
     
    non_ideal.append(min(u_root_l));
    u_root_l = [];
    
    for i in range(1,5):
        for k in range(len(l_net) -1):
            u_root_l.append(d[l_net[k]][i]);
        non_ideal.append(max(u_root_l));
    
    print("Ideal sol. : ", ideal, "non_ideal : ", non_ideal);
    
    s_ideal = {};
    s_non_ideal = {};
    #Computing Si* and Si':
    s = 0;
    for k in range(len(l_net) - 1):
        for i in range(5):
            s += (d[l_net[k]][i] - ideal[i])**2;
        s_ideal[l_net[k]] = (s**0.5);
        s = 0;

    for k in range(len(l_net) - 1):
        for i in range(5):
            s += (d[l_net[k]][i] - non_ideal[i])**2;
        s_non_ideal[l_net[k]] = (s**0.5);
        s = 0;
    
    print("\nS_ideal: ", s_ideal, "s_non_ideal: ", s_non_ideal);
    
    #Computing Ci* using list l:
    u_root_l = {} #using u_root_l as dictionary..
    for k in range(len(l_net) - 1):
        s = (s_non_ideal[l_net[k]]/(s_ideal[l_net[k]]+s_non_ideal[l_net[k]]));
        u_root_l[l_net[k]] = s;

    print('Final Result :', u_root_l,'\n'); #for debugging purpose...
    i = max(u_root_l,key = u_root_l.get);
    print('Best: ', max(u_root_l, key = u_root_l.get),'--------->', u_root_l[i]);
    
def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"));
    
    
def multiple_entry(l, old_root, n):
    
    #l_net = [];
    for i in l:
        print("Entry : ",i.get());
        l_net.append(i.get());
    l_net.append("Weight");
    #appending weight parameter to the network list....for assigning weights to the parameters....
    #Thus last parameter in l_net is weight....
    
    #Data Structures.....
    lth =[];
    lj = [];
    ld = [];
    llr = [];
    lc = [];
    y_inc = 0;
   
    old_root.destroy();
    r = Tk();
    #r.config(background = "red")
    if int(n) <=35 :
        
#        canvas = Canvas(r, background=None);
#        frame = Frame(canvas, background= None);
#        scroll = Scrollbar(r, orient='vertical', command=canvas.yview);
        
        label = Label(r, text = "Throughput").place(x = 100, y = 10);
        label = Label(r, text = "Jitter").place(x = 240, y = 10);
        label = Label(r, text = "Delay").place(x = 380, y = 10);
        label = Label(r, text = "Loss Rate").place(x = 520, y = 10);
        label = Label(r, text = "Cost").place(x = 660, y = 10);
        
        for i in range(int(n) + 1):
             label = Label(r, text = (l_net[i]));
             label.place(x = 10, y = 50 + y_inc);
             #l.config(x = 10, y = 10 + y_inc);
             
             
             eth = Entry(r);
             lth.append(eth);
             eth.place(x = 100, y = 50 + y_inc);
             
             eth = Entry(r);
             lj.append(eth);
             eth.place(x = 240, y = 50 + y_inc);
             
             eth = Entry(r);
             ld.append(eth);
             eth.place(x = 380, y = 50 + y_inc);
             
             eth = Entry(r);
             llr.append(eth);
             eth.place(x = 520, y = 50 + y_inc);
             
             eth = Entry(r);
             lc.append(eth);
             eth.place(x = 660, y = 50 + y_inc);
             
             y_inc += 20;
        
        
        Button(r, text = "0 Kelvin", command = lambda : pr(lth, lj, ld, llr, lc, n)).place(x = 400, y = 50 + y_inc);
        
        
        
#        canvas.configure(yscrollcommand=scroll.set);
#        scroll.pack(side="right", fill="y");
#        canvas.pack(fill="both", expand=True)
#        canvas.create_window((4, 4), window=frame, anchor="nw");
#        frame.bind('<Configure>', lambda event, canvas = canvas: onFrameConfigure(canvas));
        
        #Canvas and frame are not affecting the root for scrolling the region....
        
        r.geometry('800x{}'.format(y_inc + 90));
        
        
        print(y_inc);
    
    else:
        r.iconify();
        messagebox.showinfo("Info", "Limit is 35 networks");
        r.destroy();
    
    r.mainloop();
    
    
    
def n(n, old_root):
    try:
        print("n = ",n);
        
        old_root.destroy();
        r = Tk();
        r.geometry('320x200');
        canvas = Canvas(r);
        frame = Frame(canvas);
        scroll = Scrollbar(r, orient='vertical', command=canvas.yview);
        
        for i in range(int(n)):
            labl = Label(frame, text = "Network Name: {}".format(i+1), width = 45)
            labl.pack();
            e = Entry(frame);
            l.append(e);
            e.pack();
            #y_inc += 50;
            #print(y_inc);
        b = Button(frame, text = "0 Kelvin", command = lambda : multiple_entry(l, r, n))
        b.pack();
    
    
        #scroll.pack();
        #canvas.pack();
        canvas.configure(yscrollcommand=scroll.set);
        scroll.pack(side="right", fill="y");
        canvas.pack(fill="both", expand=True)
        canvas.create_window((4, 4), window=frame, anchor="nw");
        frame.bind('<Configure>', lambda event, canvas = canvas: onFrameConfigure(canvas));
        r.mainloop();
    except:
        r.destroy();
        nwork_no();

def nwork_no():
    r = Tk();
    r.title('MCDM_Program');
    r.geometry('300x80');
    l = Label(r, text = 'Enter the no. of nwork');
    l.pack();
    e = Entry(r);
    e.pack();
    b = Button(r, text = 'OK', command = lambda:n(e.get(), r));
    b.pack();
    r.mainloop();


if __name__ == '__main__':
    nwork_no();
