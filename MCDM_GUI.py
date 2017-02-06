from tkinter import Tk, Label, Button, Entry, Canvas, Frame, Scrollbar, messagebox

import time

start = time.time();
d = {};
l = [];
l_net = [];

def mcdm(lth, lj, ld, llr, lc, n):
    try:
        for i in range(int(n)):
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
        
        
        #step 1(b):Dividing each element of columns with the corresponding value in l[]:
        for i in range(5):
            for k in range(len(l_net) -1):
                d[l_net[k]][i] /=u_root_l[i];
         
        #Step 2: Multiplying weights with columns in d:
        for i in range(5):
            for k in range(len(l_net) -1):
                d[l_net[k]][i] *= d['Weight'][i];
        
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
            
        #Computing Ci* using list l:
            
        u_root_l = {} #using u_root_l as dictionary..
        
        for k in range(len(l_net) - 1):
            s = (s_non_ideal[l_net[k]]/(s_ideal[l_net[k]]+s_non_ideal[l_net[k]]));
            u_root_l[l_net[k]] = s;
    
        print('Final Result :', u_root_l,'\n'); #for debugging purpose...
        i = max(u_root_l,key = u_root_l.get);
        print('Best: ', max(u_root_l, key = u_root_l.get),'--------->', u_root_l[i]);
        print("Time taken (second): ", time.time() - start, "milliSeconds");
        messagebox.showinfo("Result", "Best Solution:\n {} ---> {}".format(max(u_root_l, key = u_root_l.get), u_root_l[i]));
        
            
    except Exception as e:
        messagebox.showerror("Opps!", str(e));
    
def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"));
       
def multiple_entry(l, old_root, n):
    for i in l:
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
    print("Time taken (first) : ", time.time() - start, "milliSeconds");
    r = Tk();
    r.iconbitmap(r"D:\Graphicloads-Medical-Health-Dna.ico");
    if int(n) <=35 :
        label = Label(r, text = "Throughput").place(x = 100, y = 10);
        label = Label(r, text = "Jitter").place(x = 240, y = 10);
        label = Label(r, text = "Delay").place(x = 380, y = 10);
        label = Label(r, text = "Loss Rate").place(x = 520, y = 10);
        label = Label(r, text = "Cost").place(x = 660, y = 10);
        
        for i in range(int(n) + 1):
             label = Label(r, text = (l_net[i]));
             label.place(x = 10, y = 50 + y_inc);
             
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
        
        Button(r, text = "0 Kelvin", command = lambda : mcdm(lth, lj, ld, llr, lc, n)).place(x = 400, y = 50 + y_inc);
        
        r.geometry('800x{}'.format(y_inc + 90));
    
    else:
        r.iconify();
        messagebox.showinfo("Info", "Limit is 35 networks");
        r.destroy();
    r.resizable(0,1);
    r.mainloop();   
    
def network_name(n, old_root):
    try:
        old_root.destroy();
        r = Tk();
        r.iconbitmap(r"D:\Graphicloads-Medical-Health-Dna.ico");
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

        b = Button(frame, text = "0 Kelvin", command = lambda : multiple_entry(l, r, n))
        b.pack();
        
        canvas.configure(yscrollcommand=scroll.set);
        scroll.pack(side="right", fill="y");
        canvas.pack(fill="both", expand=True)
        canvas.create_window((4, 4), window=frame, anchor="nw");
        frame.bind('<Configure>', lambda event, canvas = canvas: onFrameConfigure(canvas));
        r.resizable(0,0);
        r.mainloop();
    except:
        r.destroy();
        network_no();

def network_no():
    r = Tk();
    r.iconbitmap(r"D:\Graphicloads-Medical-Health-Dna.ico");
    r.title('MCDM_Program');
    r.geometry('300x80');
    r.resizable(0,0);
    l = Label(r, text = 'Enter the no. of network');
    l.pack();
    e = Entry(r);
    e.pack();
    b = Button(r, text = 'OK', command = lambda:network_name(e.get(), r));
    #e.bind('<Return>', network_name(e.get(), r));
    b.pack();
    r.mainloop();


if __name__ == '__main__':
    network_no();