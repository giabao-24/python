"""def clean_str(a):
  result = ""
  for i in a:
    if not i.isdigit():
      result += i
  return result
print(clean_str("py12thon34"))"""
"""
def check_np(a):
  check = True
  for i in a:
    if i != '0' and i != '1':
      check = False
  if check == False:
    return False
  return True
def sum_a(a):
  total = 0
  k = len(a)
  for i in a:
    total += int(i) * (2**(k-1))
    k = k - 1
  return total
s = input("Nhap so nhi phan: ")
if check_np(s) == True:
  print(sum_a(s))
"""
"""
def check_tin(a):
  count = 0
  result = ""
  for i in a:
    if count == 3:
      break
    count += 1;
    result += i
  if result == "TIN":
    return True
  return False
n = int(input("Nhap so luong"))
arr = []
for i in range(0,n):
  dic = {}
  dic["MaHP"] = input("Nhap ma hoc phan: ")
  dic["TenHP"] = input("Nhap ten hoc phan: ")
  dic["SoTC"] = int(input("Nhap so tin chi: "))
  arr.append(dic)
for i in arr:
  if i["SoTC"] >= 3:
    print(i["MaHP"], i["TenHP"], i["SoTC"])
with open("hocphanCNTT.txt","w",encoding = "utf-8") as f:
  for i in arr:
    if check_tin(i["MaHP"]):
      f.write(f"{i["MaHP"]},{i["TenHP"]},{i["SoTC"]} \n")
with open("hocphanCNTT.txt","r",encoding="utf-8") as f:
  for i in f:
    print(i)
"""
class HTRON:
  def __init__(self,a,b,bk):
    self.x = a
    self.y = b
    self.banKinh = bk
  def nhap(self):
    self.x = float(input("Nhap toa do x "))
    self.y = float(input("Nhap toa do y "))
    self.banKinh = float("Nhap ban kinh ")
  def xuat(self):
    print(f"Toa do x {self.x} ,Toa do y {self.y} , Ban kinh {self.banKinh}")
  #setters
  def set_x(self,a):
    self.x = a
  def set_y(self,b):
    self.y = b
  def set_bk(self,bk):
    self.banKinh = bk
  #getters
  def get_x(self):
    return self.x
  def get_y(self):
    return self.y
  def get_bk(self):
    return self.banKinh
  def s_tron(self):
    return (self.banKinh ** 2) * 3.14 
