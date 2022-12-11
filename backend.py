import os
from datetime import date

class Product:
  def __init__(self, pr_id, pr_name, pr_cost, pr_price, pr_stock):
    self.pr_id = pr_id
    self.pr_name = pr_name
    self.pr_cost = pr_cost
    self.pr_price = pr_price
    self.pr_stock = pr_stock

  def get_available(self):
    return int(self.pr_stock)

  def add_stock(self, amount):
    self.pr_stock += amount
    # save the adding history

  def min_stock(self, amount):
    if self.pr_stock > amount:
      self.pr_stock -= amount
    else:
      return 'the given amount is higher than the available stock'

class pr_Database:
  def __init__(self):
    self.db = []

  def add(self,product):
    self.db.append(product)

  def findna_pr(self, pr_name):
    for pr in self.db:
      if pr.pr_name==pr_name:
        return pr
    print("Product not found")
    return None

  def findid_pr(self, pr_id):
    for pr in self.db:
      if pr.pr_id==pr_id:
        return pr
    print("Product not found")
    return None

class Sale(Product):
  def __init__(self, pr_id, pr_name, pr_cost, pr_price, pr_stock, customer):
     super().__init__(pr_id, pr_name, pr_cost, pr_price, pr_stock)


pr_dict = {}
pr_database = pr_Database()


os.chdir('/Users/fulinq/Documents/KMITL/Y1/T1/IntroToProgramming/PyProject')
try:
  fi = open('product.txt', 'r')
except:
  print('Find not found')
pr_count = 1
try:
  while True:
      lines = fi.readline()
      if lines == '':
          break
      else:
          pr_data = lines.split()
          id = int(pr_data[0])
          name = pr_data[1]
          cost = int(pr_data[2])
          price = int(pr_data[3])
          stock = int(pr_data[4])
          product = Product(id, name, cost, price, stock)
          pr_database.add(product)
          pr_item = {}
          pr_item['id'] = id
          pr_item['name'] = name
          pr_item['cost'] = cost
          pr_item['price'] = price
          pr_item['stock'] = stock
          pr_dict[pr_count] = pr_item
          pr_count += 1
except:
  print('Product\'s Data Error')
fi.close()


os.chdir('/Users/fulinq/Documents/KMITL/Y1/T1/IntroToProgramming/PyProject/')
customer = {}
try:
  fi = open('customer.txt', 'r')
except:
  print('File not found')
cus_count = 0
try:
  while True:
      lines = fi.readline()
      if lines == '':
          break
      else:
        lines = lines.split()
        customer[lines[0]] = int(lines[1])
        cus_count += 1
except:
  print('Customer\'s Data Error')

print(date.today())
print(customer)
# """ Check that dictionary is working """

# for i in range(1, pr_count):
#   print(pr_dict[i])

# pr_dict[1]['stock'] = 4

# for i in range(1, pr_count):
#   print(pr_dict[i])

# while True:
#   command = input()
#   #Quit command
#   if command == 'q':
#     break
#   #Find the available stocks with product's id
#   elif command == 'sid':
#     product = pr_database.findid_pr(int(input()))
#     if product is not None:
#       print(product.get_available(), 'in stock')
#     else:
#       print('Invalid product ID')
#   #Find the available stocks with product's id
#   elif command == 'sna':
#     product = pr_database.findna_pr(input())
#     if product is not None:
#       print(product.get_available(), 'in stock')
#     else:
#       print('Invalid product ID')
#   #Sale function
#   elif command == 'sale':
#     cus = input('Customer name :')
#     cus = cus.upper()
      
