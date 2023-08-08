import pandas as pd
from proudect import Prouduct
from stack import Stack
#assuming already have data into excel file into a datafram df
df = pd.read_excel('Reading.xlsx', sheet_name='products')
print("%-20s%-20s%-10s" %("Product Name", "Category", "Price"))
print("-"*50)
pList = []
productStack = Stack()
for index, row in df.iterrows():
    productName = row['pName']
    category = row['Category']
    price = row['Price']
    
    currentProduct = Prouduct(productName,category, price)
    pList.append(currentProduct)
    productStack.push(currentProduct)
    #print(currentProduct.descrip())
    currentProduct.discont(5)
    #print("after: ", currentProduct.descrip())
    
#outside loop'
print("size of stack", productStack.size())
for product in pList:
  #print( product.descrip())
  print("%-20s%-20s%-10.2f" %(product.get_name(),product.get_category(),product.get_price()))
print("=======================")

while not productStack.is_empty():
    product = productStack.pop()
    print("%-20s%-20s%-10.2f" %(product.get_name(),product.get_category(),product.get_price()))
    

    