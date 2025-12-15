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