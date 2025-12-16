#cau1
"""
toan = float(input("Nhap diem toan"))
van = float(input("Nhap diem van"))
anh = float(input("Nhap diem anh"))
diem_tb = (toan + van + anh) / 3
print("Diem trung binh:", diem_tb)
if diem_tb >= 8 and diem_tb <= 10:
  print("Giỏi")
elif diem_tb >= 6.5 and diem_tb < 8:
  print("Khá")
elif diem_tb >= 5 and diem_tb < 6.5:
  print("Trung bình")
elif diem_tb >= 0 and diem_tb < 5:
  print("Yếu")
"""
#cau2
"""
def check_amstrong(a):
  b = str(a)
  n = len(b)
  sum = 0
  while a > 0:
    number = a % 10;
    sum += number ** n
    a = a // 10
  if sum == int(b):
    return True
  return False
print(check_amstrong(152))"""
#cau3
"""
import math
def check_snt(a):
  if a < 2:
    return False
  for i in range(2,int(math.sqrt(a))+1):
    if a % i == 0:
      return False
  return True
print(check_snt(4))"""
"""
def check_pw(a):
  b = len(a)
  chu_so = False
  chu_ca = False
  ki_tu = False
  if b < 8:
    return False
  for i in a:
    if i.isdigit():
      chu_so = True
    elif i.isupper():
      chu_ca = True
    elif not i.isalnum():
      ki_tu = True
  if chu_so and chu_ca and ki_tu:
    return True
  return False
  
se = set()
arr = []
while True:
  check = True
  dic = {}
  ten = input("Nhap ten: ")
  if ten == "":
    break
  for i in se:
    if ten == i:
      check = False
  if check == False:
    print("Da ton tai")
    continue
  se.add(ten)
  dic["TenDangNhap"] = ten
  dic["MatKhau"] = input("Nhap mat khau ")
  dic["HoTen"] = input("Nhap ho ten ")
  dic["NamSinh"] = int(input("Nhap nam sinh"))
  dic["SDT"] = input("Nhap so dien thoai")
  arr.append(dic)
for i in arr:
  if(2025 - i["NamSinh"] < 30):
    print(i["TenDangNhap"],i["HoTen"],i["SDT"])
for i in arr:
  if i["HoTen"].lower().endswith("nam"):
    print(i["TenDangNhap"],i["HoTen"],i["SDT"])
print("List low pw: \n")
for i in arr:
  if check_pw(i["MatKhau"]) == False:
    print(i["TenDangNhap"],i["HoTen"],i["SDT"])"""

class BankAccount:
  def __init__(self,account_number,account_holder,balance):
    self.soTK = account_number;
    self.chuTK = account_holder;
    self.soDu = balance;
  def napTien(self,amount):
    self.soDu += amount
    print("Nap tien thanh cong. So du hien tai:",self.soDu)
  def rutTien(self,amount):
    if amount > self.soDu or self.soDu - amount < 50000:
      print("So du khong du de rut")
      return  
    self.soDu -= amount
    print("Rut tien thanh cong. So du hien tai:",self.soDu)
  def display_infor(self):
    print(f"So tai khoan: {self.soTK} | Chu tai khoan: {self.chuTK} | So du {self.soDu}")
listTK = []
with open("ThongTinTk.txt","r",encoding = "utf-8") as f:
  for i in f:
    arr = i.strip().split(",")
    tk = BankAccount(arr[0],arr[1],float(arr[2]))
    listTK.append(tk)
#yeucau2
so = input("Nhap STK can rut tien: ")
money = float(input("Nhap so tien can rut "))
check = False
for i in listTK:
  if i.soTK == so:
    check = True
    i.rutTien(money)
if check == False:
  print("Khong tim thay tai khoan")
sort(listTK,key = lambda x: x.soDu)