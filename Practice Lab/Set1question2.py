# with open("MLK.txt",'w') as mlk:
#     mlk.write('''Martin Luther King Jr. aka MLK was born in 1929. MLK was one of the most
# prominent leaders in the civil rights movement from 1955. King advanced civil rights
# for people of color in the United States through nonviolence and civil disobedience.
# MLK was assassinated in 1968.''')

with open("/Users/akshayks/Desktop/VS code/Practice Lab/MLK.txt",'r') as data:
    item=data.read()
    l=[]
    item=item.split()
    for i in item:
        l.append(i)

    l=list(set(l))
    
    with open("/Users/akshayks/Desktop/VS code/Practice Lab/Words.txt",'w') as word:
        for i in l:
            t=str((i,item.count(i)))
            word.writelines(t)
            # print(t)


with open("/Users/akshayks/Desktop/VS code/Practice Lab/MLK.txt",'r') as swap:
    dat=swap.read()
    dat=dat.split()
    for i in dat:
        for i in range(0,len(dat)-1,2):
            dat[i],dat[i+1]=dat[i+1],dat[i]
    
    with open("/Users/akshayks/Desktop/VS code/Practice Lab/WordSwap.txt",'w') as new:
        for i in dat:
            new.write(i+"\t")





