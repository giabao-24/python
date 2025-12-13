#cau1
""""
def checksnp(a):
    for i in range(0, len(a)):
        if a[i] != '0' and a[i] != '1':
            return False
    return True

def convert(a):
    result = 0
    b = int(a)
    i = 0
    while b != 0:
        num = b % 10
        result = result + num * (2 ** i)
        i = i + 1
        b = b // 10
    return result

a = input("Nhap so nhi phan: ")

if checksnp(a):
    print(f"snp la {convert(a)}")
else:
    print("Khong phai so nhi phan")


#cau2
main = []
for i in range(0,7):
  matrix = []
  for j in range(0,7):
    value = int(input(f"Nhap gia tri cua hang {i+1} cot {j+1}"))
    matrix.append(value)
  main.append(matrix)
print(main)

check = int(input("Enter a value"))
for i in range(0,7):
  for j in range(0,7):
    if check == i+1:
      if main[i][j] == 1:
        print(j+1)
"""
#cau3
class HangHoa:
   def __init__(self,ma = "H01",ten = "",soluong = 3,gia = 1):
      self.ma_hang = ma
      self.ten_hang = ten
      self.so_luong = soluong
      self.gia_ban = gia
   #setters
   def set_ma_hang(self,ma):
      self.ma_hang = ma
   def set_ten_hang(self,ten):
      self.ten_hang = ten
   def set_so_luong(self,soluong):
      self.so_luong = soluong
   def set_gia_ban(self,gia):
      self.gia_ban = gia
    #getters
   def get_ma_hang(self):
    return self.ma_hang
   def get_ten_hang(self):
      return self.ten_hang
   def get_so_luong(self):
      return self.so_luong
   def get_gia_ban(self):
      return self.gia_ban
   def display_infor(self):
      print(f"Ma hang: {self.ma_hang}")
      print(f"Ten hang: {self.ten_hang}")
      print(f"So luong: {self.so_luong}")
      print(f"Gia ban: {self.gia_ban}")
arr = []  
se = set()   
while True:
   a = HangHoa()
   check = True
   ma = input("Nhap ma hang: ")
   if len(ma) == 0:
      print("Ket thuc nhap")
      break
   for i in se:
      if i == ma:
          print("Ma hang da ton tai, vui long nhap lai")
          check = False
          break
   if check == False:
      continue
   se.add(ma)
   ten = input("Nhap ten hang: ")
   soluong = int(input("Nhap so luong: "))
   gia = float(input("Nhap gia ban: "))
   a.set_ma_hang(ma)
   a.set_ten_hang(ten)
   a.set_so_luong(soluong)
   a.set_gia_ban(gia)
   arr.append(a)
print(arr[0].display_infor())
with open("hanghoa.txt","w") as f:
   for i in arr:
      f.write(f"{i.get_ma_hang()},{i.get_ten_hang()},{i.get_so_luong()},{i.get_gia_ban()}\n")
with open("hanghoa.txt","r") as f:
   for line in f:
      print(line)
#