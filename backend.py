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
    # save the editing history

class pr_Database:
  def __init__(self):
    self.db = []

  def add(self,product):
    self.db.append(product)

  def findid_pr(self, pr_name):
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

pr_database = pr_Database()