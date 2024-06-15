H=100
R=200
M=50
D=150
L=300
d={'Hibiscus':['Red', 'White', 'Pink', 'Violet', 'Orange', 'Yellow'],
   'Rose':['Red', 'White', 'Maroon', 'Yellow'],
   'Marigold':['Orange', 'Yellow'],
   'Dahlia':['Red', 'White', 'Pink'],
   'Lotus':['Blue', 'Pink', 'Yellow']}

n=input()
if '1' in n[0]:
    di={}
    for i in d:
        di[i]=len(d[i])
    m=max(di.values())
    for i in di:
        if di[i]==m:
            print(i)

elif '2' in n[0]:
    n=n.split(',')
    for i in d:
        if n[-1] in d[i]:
            print(i,end=" ")
        

elif '3' in n[0]:
    n=n.split(',')
    d_total={'Hibuscus':600,'Rose':800,'Marigold':100,'Dahlia':450,'Lotus':300}
    for i in d_total:
        if int(n[-1])>=d_total[i]:
            print(i,end=' ')
        
    
elif '4' in n:
    n=n.split(',')
    unique_colors=[]
    unique_colors_dict={}
    for i in d.values():
        for j in i:
            unique_colors.append(j)
    
    for i in unique_colors:
        unique_colors_dict[i]=unique_colors.count(i)

    #print(unique_colors_dict)
    for i in unique_colors_dict:
        if unique_colors_dict[i]==1:
            print(i)

else:
    print('Error')

#OR


'''F1 = {"Name":"Hibiscus", "Price":100,"Colours":["Red","White","Pink","Violet","Orange","Yellow"]}
F2 = {"Name":"Rose", "Price":200,"Colours":["Red","White","Maroon","Yellow"]}
F3={"Name":"Marigold", "Price":50,"Colours":["Orange","Yellow"]}
F4={"Name":"Dahlia", "Price":150,"Colours":["Red","White","Pink"]}
F5={"Name":"Lotus", "Price":300,"Colours":["Blue","Pink","Yellow"]}
Nursery=[F1,F2,F3,F4,F5]
str1 = input()
choice = str1.split(',')
if len(choice)==1:
    menu = int(choice[0])
else:
    menu = int(choice[0])
    if menu ==2:
        select = choice[1]
    else:
        select = int(choice[1])
if menu==1:
    max=0
    maxL = ""
    for x in Nursery:
        n = len(x["Colours"])
        if n > max:
            max = n
            maxL = x["Name"]
    print(maxL)
elif menu==2:
    flag=0
    for x in Nursery:
        if select in x["Colours"]:
            flag=1
            print(x["Name"],end=' ')
    if flag==0:
        print("None")
elif menu==3:
    flag=0
    for x in Nursery:
        if select >= x["Price"]*len(x["Colours"]):
            flag=1
            print(x["Name"], end=' ')
    if flag==0:
        print("None")
elif menu==4:
    colours=[]
    for x in Nursery:
        for y in x["Colours"]:
            colours.append(y)
    for c in colours:
        if colours.count(c)==1:
            print(c)
else:
    print("Error")'''

        
        
        
        