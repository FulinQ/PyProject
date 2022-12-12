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

customer = sorted(customer.items())
print(customer)