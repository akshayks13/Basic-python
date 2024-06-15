'''def func(arg):
    print("My name is",arg['name'])
    # print("My age is",arg(age))
    # print("My dept is",arg(dept))




d={'name':"akshay",'age':18,'dept':'CSE'}
func(d)'''


def add(a,*num,**details):
    for i,j in details.items():
        print(i,j)
    print(num)


add(1,2,3,name='akshay')
add(87,32,636,28,abc='kabksb',name='akshay')
add(5,9,86,72,98,65,34,age='18',dept='cse',name='ak')