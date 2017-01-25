def mcdm():
    try:
        nonw = int(input("Enter the no. of Networks : "));
        
        d = {};
        l = [];
        u_root_l = [];
        ideal= [];
        non_ideal = [];
        s_ideal = {};
        s_non_ideal = {};

        #Entry of networks and its parameters...
        for i in range(nonw):
            n = input('Enter the network name: ')
            ideal.append(n);#ideal used for storing n/w name in lexographical order..
            print("Enter parameter values(Throughput, Delay, Jitter, Loss_Rate, Cost)for --> %s"%n);
            for j in range(5):
                l.append(float(input()));
            d[n] = l;
            l = [];
            
        #input weights...
        print("Enter the weights of all the parameters (in serial order)...");
        
        for i in range(5):
            l.append(float(input()));
        s_ideal['weights'] = l;#s_ideal is used here to store weights with tag 'weights'..
        #Printing Matrix with weights..:
        for i in ideal:
            print('\n',i,' ', d[i]);
        for i in s_ideal:
            print('\n',i,' ', s_ideal[i],'\n');

        #s_ideal and ideal back to same condition as before....(both initialized)
        s_ideal = {};
        ideal = [];
        
        
        #summation of all columns(parameters) w.r.t networks and their square_root
        uroot = 0;
        for i in range(5):
            for k in d:
                uroot += d[k][i];
            u_root_l.append(uroot);
            uroot = 0;


        for i in range(len(u_root_l)):
            u_root_l[i] = u_root_l[i]**0.5;

        #step 1(b):Dividing each element of columns with the corresponding value in l[]:
        for i in range(5):
            for k in d:
                d[k][i] /=u_root_l[i];
                #print(d[k][i]);

        #Step 2: Multiplying weights with columns in d:
        for i in range(5):
            for k in d:
                d[k][i] *= l[i];
                print(d[k][i]);

        l = [];
        #Determining Ideal Solution:

        for k in d:
            l.append(d[k][0]);
           
        ideal.append(max(l));
        l = [];
        for i in range(1, 5):
            for k in d:
                l.append(d[k][i]);
            ideal.append(min(l));

        l = []

        #Computing Non_ideal 
        for k in d:
            l.append(d[k][0]);
           
        non_ideal.append(min(l));
        l = [];
        for i in range(1, 5):
            for k in d:
                l.append(d[k][i]);
            non_ideal.append(max(l));

        #Computing Si* and Si':
        s = 0;
        for k in d:
            for i in range(5):
                s += (d[k][i] - ideal[i])**2;
            s_ideal[k] = (s**0.5);
            s = 0;

        for k in d:
            for i in range(5):
                s += (d[k][i] - non_ideal[i])**2;
            s_non_ideal[k] = (s**0.5);
            s = 0;

        #Computing Ci* using list l:
        l = {}
        for k in d:
            s = (s_non_ideal[k]/(s_ideal[k]+s_non_ideal[k]));
            l[k] = s;

        print('Final Result :', l,'\n'); #for debugging purpose...
        i = max(l,key = l.get);
        print('Best: ', max(l, key = l.get),'-->', l[i]);

        
    except Exception as e:
        print("__________________________");
        print(str(e));
        print();
        print("Restarting Program....");
        print("__________________________\n");
        mcdm();


if __name__ == "__main__":
    mcdm();



