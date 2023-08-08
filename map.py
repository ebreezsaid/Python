emplo=['ail','mohammed','hmed','hamed']
hwork=[1,2,3,4]
pperh=[5,6,7,8]


doubePay=list(map(lambda p :p*2 , pperh))

result=list(map(lambda h,p : h*p , hwork,doubePay))
              
print("after doubel",result)