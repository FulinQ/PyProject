import os
from datetime import date
import numpy as np
import matplotlib.pyplot as mp

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

def get_year():
  global x, y
  x = date.today()
  print()
  while True:
    y = input('Enter year : ')
    if y == 'q':
      y = None
      return 'q'
    try:
      y = int(y)
    except:
      print('Year must be 4 digit integer')
      continue
    if 2022 <= y <= int(x.year):
      y = str(y)
      return y
    else:
      print('Year must be 4 digit integer')

def get_month():
  global x, m, mon
  x = date.today()
  mon = {'01':32, '02':29, '03':32, '04':31, '05':32, '06':31, '07':32, '08':32, '09':31, '10':32, '11':31, '12':32}
  while True:
      m = input('Enter month(2 digits e.g.01) : ')
      if m == 'q':
        m = None
        return None
      elif m in mon:
        m = str(m)
        return m
      else:
        print('Error : month should be between 01-12')
        continue
      
def consumer_update():
  global customer
  fi = open('customer.txt', 'w')
  cu = sorted(customer.items())
  for i in cu:
    data = str(i[0]) + ' '
    fi.write(data)
    data = str(i[1]) + '\n'
    fi.write(data)
  fi.close()

def product_update():
  global pr_dict
  fi = open('product.txt', 'w')
  for i in range(1, pr_count):
    fi.write(str(pr_dict[i]['id'])+' ')
    fi.write(str(pr_dict[i]['name'])+' ')
    fi.write(str(pr_dict[i]['cost'])+' ')
    fi.write(str(pr_dict[i]['price'])+' ')
    fi.write(str(pr_dict[i]['stock'])+'\n')
  fi.close()


print('\nToday\'s date :', date.today())
# print(customer)
# """ Check that dictionary is working """

# for i in range(1, pr_count):
#   print(pr_dict[i])

# pr_dict[1]['stock'] = 4

# for i in range(1, pr_count):
#   print(pr_dict[i])

while True:
  con = input('Continue? y/n : ')
  if con == 'y':
    print()
    print('Command list')
    print('sid : check product\'s stock by id')
    print('sna : check product\'s stock by name')
    print('rgraph : cost, revenue, profit for sale on each day')
    print('prpie : sold product proportion')
    print('bas : basket size')
    print('topc : top customer of the month')
    print('topp : top product of the month')
    print('add : add product\'s stock')
    print('sale : create order')
  else:
    product_update()
    consumer_update()
    print('Data saved')
    break
  command = input('Enter command : ')
#Quit command
  if command == 'q':
    product_update()
    consumer_update()
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

            fi = open('basket.txt', 'a')
            data = str(x.year)+' '+str(x.month)+' '+str(x.day)+' '+str(cus)+' '+str(len(order))+'\n'
            fi.write(data)
            fi.close()
            product_update()
            order = []
            name = cus
            customer[name] = customer.get(name,0) + 1
            consumer_update()
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
            if o_qu <= s:
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
              print('Error: enter product ID again')
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
      try:
        amount = int(input('Adding amount : '))
      except:
        print('Error: amount should be an integer. Pease try again.')
        continue
      product.add_stock(amount)
      for i in range(1, pr_count):
        if pr_dict[i]['id'] == product.pr_id:
          pr_dict[i]['stock'] += amount
          cost = pr_dict[i]['cost']*amount
          data = str(x.year)+' '+str(x.month)+' '+str(x.day)+' '+str(pr_dict[i]['id'])+' '+ str(pr_dict[i]['name'])+' '+str(cost)+'\n'
          fi.write(data)
          fi.close()
          product_update()
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
        product_update()
        cost = cost*stock
        data = str(x.year)+' '+str(x.month)+' '+str(x.day)+' '+str(id)+' '+ str(name)+' '+str(cost)+'\n'
        fi.write(data)
        fi.close()
      else:
        fi.close()
        print('Input is not match, return to Home.')
#graph
  elif command == 'rgraph':
    rev = {}
    co = {}
    prof = {}
    print()
    y = get_year()
    if y == None:
      continue
    m = get_month()
    if m == None:
      continue
    k = mon[m]
    one = []
    for i in range(1,k):
      j = str(i)
      if len(j) == 1:
        j = str(0)+j
      else:
        j = str(j)
      rev[j] = rev.get(j, 0)
      co[j] = co.get(j, 0)
      prof[j] = prof.get(j, 0)
      d_one = i
      one.append(d_one)
    fi = open('sold.txt', 'r')
    print('Year :',y ,', Month :',m)
    while True:
      line = fi.readline()
      if line == '':
        break
      else:
        line = line.strip()
        line = line.split()
        if line[0] == y and line[1] == m:
          d = line[2]
          # print(d)
          p = int(line[-1])
          c = int(line[-2])
          r = p+c
          rev[d] = rev.get(d, 0) + r
          co[d] = co.get(d, 0) + c
          prof[d] = prof.get(d, 0) + p
        else:
          continue
    fi.close()
    # print(rev)
    # print(co)
    # print(prof)
    rl = list(rev.values())
    cl = list(co.values())
    pl = list(prof.values())
    # print(rl)
    # print(cl)
    # print(pl)
    # print(one)
    mp.figure(figsize = (20,6))
    mp.axes(xticks=one)
    oa = np.array(one)
    ra = np.array(rl)
    ca = np.array(cl)
    pa = np.array(pl)
    mp.bar(oa-0.2,ca,width=0.2,label='cost',align='center')
    mp.bar(oa,ra,width=0.2,label='revenue',align='center')
    mp.bar(oa+0.2,pa,width=0.2,label='profit',align='center')
    mp.title('Cost, Revenue, Profit for sale')
    mp.ylabel('Baht')
    mp.xlabel('Date')
    mp.legend(loc='best')
    mp.show()
    continue
#Sold product pie chart
  elif command == 'prpie':
    print()
    y = get_year()
    if y == None:
      continue
    m = get_month()
    if m == None:
      continue
    fi = open('sold.txt', 'r')
    print('Year :',y ,', Month :',m)
    sold_pr= {}
    while True:
      line = fi.readline()
      if line == '':
        break
      else:
        line = line.strip()
        line = line.split()
        if line[0] == y and line[1] == m:
          sold_na = line[-4]
          sold_nu = int(line[-3])
          sold_pr[sold_na] = sold_pr.get(sold_na, 0) + sold_nu
        else:
          continue
    fi.close()
    # print(sold_pr)
    sold_pr = sorted(sold_pr.items(), key = lambda x: x[1], reverse = True)
    sold_k = []
    for i in sold_pr:
      data = i[0]+' : '+str(i[1])
      sold_k.append(data)
    sold_pr = dict(sold_pr)
    sold_v = list(sold_pr.values())

    mp.figure(figsize = (10,5))
    mp.title('sold product proportion')
    mp.pie(sold_v, labels = sold_k, autopct = '%.2f%%', startangle = 90)
    # mp.legend(loc = 'upper right')
    mp.show()
    continue
#basket size:
  elif command == 'bas':
    tc = input('All or enter customer name : ')
    tc = tc.upper()
    if tc == 'q':
      continue
    elif tc == 'ALL':
      print()
      y = get_year()
      if y == None:
        continue
      m = get_month()
      if m == None:
        continue
      fi = open('basket.txt', 'r')
      avg_bas = 0
      devide = 0
      while True:
        line = fi.readline()
        if line == '':
          break
        else:
          line = line.strip()
          line = line.split()
          if line[0] == y and line[1] == m:
            avg_bas += int(line[-1])
            devide += 1
          else:
            continue
      fi.close()
      print()
      print('total order :', devide)
      print('Average basket size')
      print('actual :',avg_bas/devide,)
      print('realistic :', int(avg_bas/devide))

    elif tc in customer:
      print()
      y = get_year()
      if y == None:
        continue
      m = get_month()
      if m == None:
        continue
      fi = open('basket.txt', 'r')
      avg_bas = 0
      devide = 0
      while True:
        line = fi.readline()
        if line == '':
          break
        else:
          line = line.strip()
          line = line.split()
          if line[0] == y and line[1] == m and line[3] == tc:
            avg_bas += int(line[-1])
            devide += 1
          else:
            continue
      fi.close()
      print()
      print('Customer :', tc)
      print('total order :', devide)
      print('Average basket size')
      print('actual :',avg_bas/devide,)
      print('realistic :', int(avg_bas/devide))
    else:
      print('Customer is not in customer list.')
#Top customer
  elif command == 'topc':
    print()
    y = get_year()
    if y == None:
      continue
    m = get_month()
    if m == None:
      continue
    fi = open('sold.txt', 'r')
    print('Year :',y ,', Month :',m)
    topc = {}
    while True:
      line = fi.readline()
      if line == '':
        break
      else:
        line = line.strip()
        line = line.split()
        if line[0] == y and line[1] == m:
          ct = line[3]
          pt = int(line[-2]) + int(line[-1])
          topc[ct] = topc.get(ct, 0) + pt
        else:
          continue
    fi.close()
    topc = sorted(topc.items(), key = lambda x: x[1], reverse = True)
    rt = topc[0][1]
    # print(rt)
    topc = dict(topc)
    print()
    print('Top customer')
    # print(topc)
    for i in topc:
      if topc[i] == rt:
        print('Customer name :', i)
        print('Total revenue from', i,':', topc[i])
        print()
      else:
        continue
#Top product
  elif command == 'topp':
    print()
    y = get_year()
    if y == None:
      continue
    m = get_month()
    if m == None:
      continue
    fi = open('sold.txt', 'r')
    print('Year :',y ,', Month :',m)
    topp = {}
    while True:
      line = fi.readline()
      if line == '':
        break
      else:
        line = line.strip()
        line = line.split()
        if line[0] == y and line[1] == m:
          tp = line[4]
          tpa = int(line[-3])
          topp[tp] = topp.get(tp, 0) + tpa
        else:
          continue
    fi.close()
    topp = sorted(topp.items(), key = lambda x: x[1], reverse = True)
    ts = topp[0][1]
    # print(ts)
    topp = dict(topp)
    # print(topp)
    print()
    print('Popular product')
    for i in topp:
      if topp[i] == ts:
        print('Product name :', i)
        print('Total amount sold :', i,':', topp[i])
        print()
      else:
        continue