
d={'Andhra Pradesh':{'Official Language':['Telugu','English'],'Other spoken languages':['Urdu','Hindi','Banjara','Tamil','Kannada','Marathi','Oriya']},
   'Karnataka':{'Official Language':['Kannada','English'],'Other spoken languages':['Urdu','Telugu','Tamil','Marathi']},
   'Kerela':{'Official language':['Malayalam','English'],'Other spoken languages':['Hindi','Kannada','Tamil','Tulu']},
   'Tamilnadu':{'Official language':['Tamil','English'],'Other spoken languages':['Telegu','Kannada','Urdu','Malayalam','Hindi']},
   'Telengana':{'Official language':['Telegu','Urdu'],'Other spoken languages':['Hindi','Tamil','Kannada','Marathi','Oriya']}}

option=input()

if option=='1':
    maxdict={}
    count=0
    for i in d:
        for j in d[i]:
            for k in d[i][j]:
                count+=1
        
        maxdict[i]=count
        count=0
    
    m=max(maxdict.values())
    for i in maxdict:
        if maxdict[i]==m:
            print(i)
                
elif '2' in option:
    option=option.split(',')
    st=option[-1]
    count=0
    if option[-1] in d:
        for i in d:
            if i==st:
                for j in d[i]['Other spoken languages']:
                    count+=1
    print(count)

elif '3' in option:
    option=option.split(',')
    lan=option[-1]
    for i in d:
        if lan in d[i]['Other spoken languages']:
            print(i,end=' ')
               
elif option == '4':
    languages=[]
    dic_unique_lan={}
    for i in d:
        for j in d[i]:
            for k in d[i][j]:
                languages.append(k)
               
    for i in languages:
        dic_unique_lan[i]=languages.count(i)
    
    for i in dic_unique_lan:
        if dic_unique_lan[i]==1:
            print(i)

else:
    print('Error')
            
#OR


'''S1 = {"Name":"Andhra Pradesh", "Official":["Telugu","English"],"Spoken":["Urdu","Hindi","Banjara","Tamil","Kannada","Marathi","Oriya"]}
S2 = {"Name":"Karnataka", "Official":["Kannada","English"],"Spoken":["Urdu","Telugu","Tamil","Marathi"]}
S3={"Name":"Kerala", "Official":["Malayalam","English"],"Spoken":["Hindi","Kannada","Tamil","Tulu"]}
S4={"Name":"Tamilnadu", "Official":["Tamil","English"],"Spoken":["Telugu","Urdu","Kannada","Malayalam","Hindi"]}
S5={"Name":"Telangana", "Official":["Telugu","Urdu"],"Spoken":["Hindi","Tamil","Kannada","Marathi","Oriya"]}
States=[S1,S2,S3,S4,S5]
str1 = input()
choice = str1.split(',')
if len(choice)==1:
    menu = int(choice[0])
else:
    menu = int(choice[0])
    select = choice[1]
if menu==1:
    max=0
    maxL = ""
    for x in States:
        n = len(x["Official"])+len(x["Spoken"])
        if n > max:
            max = n
            maxL = x["Name"]
    print(maxL)
elif menu==2:
    for x in States:
        if x["Name"]==select:
            print(len(x["Spoken"]))
elif menu==3:
    for x in States:
        if select in x["Spoken"]:
            print(x["Name"], end=' ')
elif menu==4:
    langs=[]
    for x in States:
        for y in x["Official"]:
            langs.append(y)
        for y in x["Spoken"]:
            langs.append(y)
    for l in langs:
        if langs.count(l)==1:
            print(l)
else:
    print("Error")'''