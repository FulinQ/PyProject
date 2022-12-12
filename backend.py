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

  def de_stock(self, amount):
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
fi.close()

print(date.today())
# print(customer)
# """ Check that dictionary is working """

# for i in range(1, pr_count):
#   print(pr_dict[i])

# pr_dict[1]['stock'] = 4

# for i in range(1, pr_count):
#   print(pr_dict[i])

while True:
  print()
  command = input('Enter command : \nsid : check product\'s stock by id \nsna : check product\'s stock by name : \nsale : create order \n')
#Quit command
  if command == 'q':
    fi = open('product.txt', 'w')
    for i in range(1, pr_count):
      fi.write(str(pr_dict[i]['id'])+' ')
      fi.write(str(pr_dict[i]['name'])+' ')
      fi.write(str(pr_dict[i]['cost'])+' ')
      fi.write(str(pr_dict[i]['price'])+' ')
      fi.write(str(pr_dict[i]['stock'])+'\n')
    fi.close()

    fi = open('customer.txt', 'w')
    customer = sorted(customer.items())
    for i in customer:
      data = str(i[0]) + ' '
      fi.write(data)
      data = str(i[1]) + '\n'
      fi.write(data)
    fi.close()

    # fi.open('customer.txt', 'w')
    # for i in customer:
    #   i....
    print('Data saved')
    break
#Find the available stocks with product's id
  elif command == 'sid':
    product = pr_database.findid_pr(int(input()))
    if product is not None:
      print(product.pr_name, product.get_available(), 'in stock')
    else:
      print('Invalid product ID')
#Find the available stocks with product's id
  elif command == 'sna':
    product = pr_database.findna_pr(input())
    if product is not None:
      print(product.pr_name, product.get_available(), 'in stock')
    else:
      print('Invalid product ID')
#Sale function
  elif command == 'sale':
    order = []
    cus = str(input('Customer name : '))
    cus = cus.upper()
    while True:
      sum = 0
      if len(order) == 0:
        print('No product in your basket')
      else:
        print('Your order : ', len(order))
        for i in order:
          product_o = pr_database.findna_pr(i[0])
          print(product_o.pr_name, end = ' ')
          print(i[1], end = ' ')
          print(product_o.pr_price*i[1], 'Baht')
          sum += product_o.pr_price*i[1]
          print('Total :', sum)
        print()
      o_pr = input('Enter product id : ')

      if o_pr == 'finish':
        while True:
          print()
          print('Final Bill :', cus)
          for i in order:
            product_o = pr_database.findna_pr(i[0])
            print(product_o.pr_name, end = ' ')
            print(i[1], end = ' ')
            print(product_o.pr_price*i[1], 'Baht')
          revenue = sum
          print('Total :', sum)
          cash = int(input('Enter cash : '))
          if cash < revenue:
            print('Must pay more than the total price.')
            continue
          else:
            print('Customer pays :', cash, 'Baht')
            change = cash - sum
            print('Change :', change)
            profit = 0
            cost = 0
            x = date.today()
            fi = open('sold.txt', 'a')
            for i in order:
              # print(i)
              product = pr_database.findna_pr(i[0])
              if product is not None:
                product.de_stock(int(i[1]))
                pi = product.pr_price - product.pr_cost
                pi *= int(i[1])
                cost = product.pr_cost*int(i[1])
                profit += pi
                data = str(x.year)+' '+str(x.month)+' '+str(x.day)+' '+str(cus)+' '+str(product.pr_name)+' '+str(i[1])+' '+str(cost)+' '+str(pi)+' '+'\n'
                fi.write(data)
            fi.close()
            print('Profit :', profit)
            order = []
            name = cus
            customer[name] = customer.get(name,0) + 1
            break

      elif o_pr == 'clear':
        order = []
        break
      else:
        try: 
          product = pr_database.findid_pr(int(o_pr))
          if product is not None:
            s = None
            id_o = None
            for i in range(1,pr_count):
              if pr_dict[i]['id'] == product.pr_id:
                a = pr_dict[i]['stock']
                s = a
                id_o = i
                break
              else:
                continue
            print(product.pr_name, s, 'in stock')
            try:
              o_qu = int(input('Enter quantity : '))
            except:
              print('Quantity must be an integer. Please enter product ID again.')
              continue
            if o_qu < s:
              list_o = [product.pr_name, o_qu]
              # print(pr_dict[id_o]['stock'])
              pr_dict[id_o]['stock'] = s - o_qu
              # print(pr_dict[id_o]['stock'])
              order.append(list_o)
              continue
            elif o_qu <= 0:
              print('Error: quantity cannot be zero or negative number. Enter product ID again')            
              continue
            else:
              print('Error enter product ID again')
              continue
        except:
          print('Error: Enter product ID again.')
          continue
#add stock
  elif command == 'add':
    i_pr = (int(input('Enter product ID : ')))
    product = pr_database.findid_pr(i_pr)
    fi = open('supply_up.txt', 'a')
    x = date.today()
    if product is not None:
      print('Now, there are', product.get_available(),product.pr_name , 'in stock')
      amount = int(input('Adding amount : '))
      product.add_stock(amount)
      for i in range(1, pr_count):
        if pr_dict[i]['id'] == product.pr_id:
          pr_dict[i]['stock'] += amount
          cost = pr_dict[i]['cost']*amount
          data = str(x.year)+' '+str(x.month)+' '+str(x.day)+' '+str(pr_dict[i]['id'])+' '+ str(pr_dict[i]['name'])+' '+str(cost)+'\n'
          fi.write(data)
          fi.close()
          break
        else: 
          continue
    else:
      print('Product not found. New product?(y/n)')
      yn = input()
      if yn == 'n':
        fi.close()
        print('Quit adding stock command')
      elif yn == 'y':
        print()
        print('Please product\'s data')
        id = int(input('Enter Product ID : '))
        name = input('Enter Product Name : ')
        cost = int(input('Enter Product Cost : '))
        price = int(input('Enter Product Price : '))
        stock = int(input('Enter Product Stock : '))
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
        cost = cost*stock
        data = str(x.year)+' '+str(x.month)+' '+str(x.day)+' '+str(id)+' '+ str(name)+' '+str(cost)+'\n'
        fi.write(data)
        fi.close()
      else:
        fi.close()
        print('Input is not match, return to Home.')
    