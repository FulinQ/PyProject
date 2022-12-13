from datetime import date

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

# y = get_year()
# if y == None:
#   continue
# m = get_month()
# if m == None:
#   continue