# with open("/Users/akshayks/Desktop/VS code/Practice Lab/WS.txt",'w') as ws:
#     ws.write('''William Shakespeare was an English playwright, poet, and actor who is widely
# regarded as one of the greatest writers in the English language and the world’s pre-
# eminent dramatist. He was born in Stratford-upon-Avon in 1564 and married Anne
# Hathaway in 1582. They had three children. Shakespeare's plays include Macbeth,
# Romeo and Juliet, and The Tempest.''')


'''with open("/Users/akshayks/Desktop/VS code/Practice Lab/WS.txt",'r') as data:
    item=data.read()
    l=[]
    item=item.split()
    for i in item:
        l.append(i)

    l=list(set(l))
    
    with open("/Users/akshayks/Desktop/VS code/Practice Lab/Words.txt",'w') as word:
        for i in l:
            t=str((i,item.count(i)))
            word.writelines(t)'''


with open("/Users/akshayks/Desktop/VS code/Practice Lab/WS.txt",'r') as con:
    dat=con.read()
    dat=dat.split()
    l=[]
    for i in dat:
        l.append(i[::-1])

    with open("/Users/akshayks/Desktop/VS code/Practice Lab/Reversed.txt",'w') as rev:
        for i in l:
            rev.write(i+'\t')




    
