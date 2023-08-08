import re
def filter_lambda(L):
    lista=[]
    for c in L:
        if c == 'cat':
            lista.append(c)
    return lista


a = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]
aa=filter_lambda(a)
print("list is : ",a)
print ("list cat: " ,aa)
print("=====================================")
print("=====================================")
print("=====================================")
#a = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]
re =re.compile(r'cat')
#using filter
s = list(filter(lambda n : re.search(n) , a))
print("Filtered : " ,s)
            