from tkinter import Tk, Label, Button, Entry, Canvas, Frame, Scrollbar, messagebox
#from functools import partial

#def slpash():

d = {};
l = [];

def pr(lth, lj, ld, llr, lc, n):
    for i in range(int(n)):
        print("Lth: ",lth[i].get());
        print("Lj: ",lj[i].get());
        print("Ld: ",ld[i].get());
        print("Llr: ",llr[i].get());
        print("Lc: ",lc[i].get());
        print("________________________________________");
        
def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"));
    
    
def multiple_entry(l, old_root, n):
    
    l_net = [];
    for i in l:
        print("Entry : ",i.get());
        l_net.append(i.get());
    
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
        
        for i in range(int(n)):
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
        
        #Canvas and frame are not affecting the root for scrollthe region....
        
        r.geometry('800x{}'.format(y_inc + 90));
        
        
        print(y_inc);
    
    else:
        r.iconify();
        messagebox.showinfo("Info", "Limit is 35 nworks");
        r.destroy();
    
    r.mainloop();
    
    
    
def n(n, old_root):
    try:
        print("n = ",n);
        
        old_root.destroy();
        r = Tk();
        r.geometry('320x500');
        canvas = Canvas(r);
        frame = Frame(canvas);
        scroll = Scrollbar(r, orient='vertical', command=canvas.yview);
        
        for i in range(int(n)):
            labl = Label(frame, text = "network name: {}".format(i+1), width = 45)
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