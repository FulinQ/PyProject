import os
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

# def total_stock():
#   if len(pr_database) == 0:
#     return 0
#   elif len(pr_database) < 0:
#     return 'Error: Negative amount in stock'
#   elif len(pr_database) > 0:
#     for 

pr_database = pr_Database()
os.chdir('/Users/fulinq/Documents/KMITL/Y1/T1/IntroToProgramming/PyProject')
fi = open('product.txt', 'r')
pr_count = 1
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
        pr_count += 1

print(pr_database)

while True:
    command = input()
    #Quit command
    if command == 'q':
        break
    #Find the available stocks with product's id
    elif command == 'sid':
        product = pr_database.findid_pr(int(input()))
        if product is not None:
            print(product.get_available(), 'in stock')
        else:
            print('Invalid product ID')
    #Find the available stocks with product's id
    elif command == 'sna':
        product = pr_database.findna_pr(input())
        if product is not None:
            print(product.get_available(), 'in stock')
        else:
            print('Invalid product ID')
