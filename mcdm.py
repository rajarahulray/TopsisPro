from tkinter import *
#from tkMessageBox import *

d = {};
l = [];

xc = 100;#x-coordinate varaible if need to change it...
yc = 50;#y-coordinate varaible if need to change it...

r = Tk();
r.geometry('1000x240');
r.title('MCDM');
r.config(background = 'green');

nl = Label(r, text = 'Netrwoks',background = 'green', fg = 'yellow');
nl.place(x = 10, y = yc);

pl = Label(r, text = 'Parameters', background = 'green', fg = 'yellow');
pl.place(x = xc, y = 10);
#First Network with 5 parameters:
n1 = Entry(r);
n1.place(x = xc, y = yc);

n1p1 = Entry(r);
n1p1.place(x = xc+150, y = yc);

n1p2 = Entry(r);
n1p2.place(x = xc+300, y = yc);

n1p3 = Entry(r);
n1p3.place(x = xc+450, y = yc);

n1p4 = Entry(r);
n1p4.place(x = xc+600, y = yc);

n1p5 = Entry(r);
n1p5.place(x = xc+750, y = yc);
 
#Second Network with parameters:

n2 = Entry(r);
n2.place(x = xc, y = yc+30);

n2p1 = Entry(r);
n2p1.place(x = xc+150, y = yc+30);

n2p2 = Entry(r);
n2p2.place(x = xc+300, y = yc+30);

n2p3 = Entry(r);
n2p3.place(x = xc+450, y = yc+30);

n2p4 = Entry(r);
n2p4.place(x = xc+600, y = yc+30);

n2p5 = Entry(r);
n2p5.place(x = xc+750, y = yc+30);

#Third Network with parameters:

n3 = Entry(r);
n3.place(x = xc, y = yc+60);

n3p1 = Entry(r);
n3p1.place(x = xc+150, y = yc+60);

n3p2 = Entry(r);
n3p2.place(x = xc+300, y = yc+60);

n3p3 = Entry(r);
n3p3.place(x = xc+450, y = yc+60);

n3p4 = Entry(r);
n3p4.place(x = xc+600, y = yc+60);

n3p5 = Entry(r);
n3p5.place(x = xc+750, y = yc+60);


#Fourth Network with parameters:

n4 = Entry(r);
n4.place(x = xc, y = yc+90);

n4p1 = Entry(r);
n4p1.place(x = xc+150, y = yc+90);

n4p2 = Entry(r);
n4p2.place(x = xc+300, y = yc+90);

n4p3 = Entry(r);
n4p3.place(x = xc+450, y = yc+90);

n4p4 = Entry(r);
n4p4.place(x = xc+600, y = yc+90);

n4p5 = Entry(r);
n4p5.place(x = xc+750, y = yc+90);

#Fifth Network with parameters:

n5 = Entry(r);
n5.place(x = xc, y = yc+120);

n5p1 = Entry(r);
n5p1.place(x = xc+150, y = yc+120);

n5p2 = Entry(r);
n5p2.place(x = xc+300, y = yc+120);

n5p3 = Entry(r);
n5p3.place(x = xc+450, y = yc+120);

n5p4 = Entry(r);
n5p4.place(x = xc+600, y = yc+120);

n5p5 = Entry(r);
n5p5.place(x = xc+750, y = yc+120);


b = Button(r, text  = 'Add Network');
b.place(x = xc+350, y = yc+150);

r.mainloop();
