''' If the strings are of same format,return true,else return false,
eg: 'aba' and 'xyx' results in true and 'abc' and 'xyx' results in false'''


def func(a,b):
    if len(a)!= len(b):
        return False
    
    char_map={}
    
    for c1,c2 in zip(a,b):
        if c1 in char_map:
            if char_map[c1] == c2:
                return True
            else:
                return False
        
        else:
            if c2 in char_map.values():
                return False
            else:
                char_map[c1]=c2

a=input("Enter a string:")
b=input("Enter another string:")

print(func(a,b))
