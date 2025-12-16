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

