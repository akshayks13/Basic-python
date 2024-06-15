N=int(input("Enter the number os customers:"))
l=[]
d_totalpurchase={}
d_purchasetype={}
for i in range(N):
    customer_id,kind_of_purchase,purchase_amount=map(str,input().split(','))
    t=[int(customer_id),kind_of_purchase,int(purchase_amount)]
    l.append(t)

print(l)
for i in range(len(l)):
    if l[i][0] in d_totalpurchase:
        d_totalpurchase[l[i][0]] += l[i][2]
    else:
        d_totalpurchase[l[i][0]]=l[i][2]
  
print('Total purchase per customer:',d_totalpurchase)


l_store=[]
l_online=[]
l_unknown=[]
for i in l:
    if i[1]== 'store':
        if i[0] in l_store:
            pass
        else:
            l_store.append(i[0])
    elif i[1]== 'online':
        if i[0] in l_online:
            pass
        else:
            l_online.append(i[0])
    else:
        if i[0] in l_unknown:
            pass
        else:
            l_unknown.append(i[0])

d_purchasetype['store']=l_store
d_purchasetype['online']=l_online
d_purchasetype['unkown_mode']=l_unknown

print('Customers per purchase type:',d_purchasetype)
    
 
for i in d_totalpurchase:
    m=max(d_totalpurchase.values())
    if d_totalpurchase[i] == m:
        print('Top spenders id is:',i)