import csv

def knn1(x1,x2,x3,x4,x5,x11,x12,x13,x14,x15):
    dc=(x1-x11)**2+(x2-x12)**2+(x3-x13)**2+(x4-x14)**2+(x5-x15)**2
    return (dc)

def sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
    
# Compare the current element with next one
		
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element
    return (InputList)

def vote(nol,satu,dua,tiga): 
    listcat=[]
    listcat.insert(0,nol)
    listcat.insert(1,satu)
    listcat.insert(2,dua)
    listcat.insert(3,tiga)
    return (listcat)

x1 = [];
x2 = [];
x3 = [];
x4 = [];
x5 = [];
y = [];
x11 = [];
x12 = [];
x13 = [];
x14 = [];
x15 = [];
no=[];

train = csv.reader(open("DATA Tugas 3 AI/DataTrain_Tugas3_AI.csv"))
for row in train:
        no.append(row[0]);
        x1.append(row[1]);
        x2.append(row[2]);
        x3.append(row[3]);
        x4.append(row[4]);
        x5.append(row[5]);
        y.append(row[6]);

test = csv.reader(open("DATA Tugas 3 AI/DataTest_Tugas3_AI.csv"))
for row in test:
        x11.append(row[1]);
        x12.append(row[2]);
        x13.append(row[3]);
        x14.append(row[4]);
        x15.append(row[5]);

#main
k=5


i=1
h=1
u=2

fixcat=[]
dist=[]
dist1=[]
temp=[]
near=[]
cat=[]
print("loading...")
while i <= 200:
    n=1
    while n <= 800:
        d=knn1(float(x1[n]),float(x2[n]),float(x3[n]),float(x4[n]),float(x5[n]),float(x11[i]),float(x12[i]),float(x13[i]),float(x14[i]),float(x15[i]))
        temp.insert(n,d)
        dist1.insert(n,d)
        temp.extend(y[n])
        dist.extend(temp)
        u=u+1
        temp.clear()
        n=n+1
    o=1
    while o<=7:
        nol=0
        satu=0
        dua=0
        tiga=0
        near=sort(dist1)
        m=1
        while m <= 1599 :
            if near[o] == dist[m] :
                m=m+1  
                if (dist[m] == '1'):
                    satu=satu+1
                elif (dist[m] == '2'):
                    dua=dua+1
                elif (dist[m] == '3'):
                    tiga=tiga+1
                else :
                    nol=nol+1 
            else :
                m=m+1
        cat=vote(nol,satu,dua,tiga)
        o=o+1
    if (cat[1]==1):
        fixcat.insert(i,1)
    elif (cat[2]==1):
        fixcat.insert(i,2)
    elif (cat[3]==1):
        fixcat.insert(i,3)
    else :
        fixcat.insert(i,0)
    dist.clear()
    dist1.clear()
    near.clear()
    cat.clear()
    i=i+1
    #sortedcat=sort(cat)
v=1
for v in range(0, len(fixcat)):
    print ("baris ke-",v+1,", dengan Y = ",fixcat[v])

print("menyimpan pada file TebakanTugas3.csv")

f = open('DATA Tugas 3 AI/TebakanTugas3.csv', 'w')
with f:
    writer = csv.writer(f,lineterminator='\n')
    for val in fixcat:
        writer.writerow([val])
print("menyimpan selesai")


                
            
            
                
        
        

        
    





    
