import os
os.chdir('/Users/fulinq/Documents/KMITL/Y1/T1/IntroToProgramming/PyProject/')
customer = {}
fi = open('customer.txt', 'r')
cus_count = 0
# try:
while True:
    lines = fi.readline()
    if lines == '':
        break
    else:
     line = line.split()
     key = line[0]
     customer[key] = line[1]
     cus_count += 1
# except:
#   print('Customer\'s File Error')

print(customer)