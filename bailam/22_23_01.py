#bai1 clean string
"""
def cleanstring(s):
  result = ""
  for i in range(0,len(s)):
    if s[i].isalpha():
      result += s[i]
  return result
s = input("Nhap chuoi ")
print(f"Chuoi sau khi lam sach la {cleanstring(s)}")"""

#bai2
arr = []
while True:
  dic = {}
  value1 = input("Nhap ten mat hang")
  if len(value1) == 0:
    break
  value2 = int(input("Nhap so luong"))
  value3 = float(input("Nhap gia ban"))
  dic["tenhang"] = value1
  dic["soluong"] = value2
  dic["giaban"] = value3
  arr.append(dic)
for i in range(0,len(arr)):
  if arr[i]["soluong"] < 5:
    print(f"Mat hang {arr[i]['tenhang']}")
tongtienhang = 0
for i in range(0,len(arr)):
  tongtienhang = tongtienhang + arr[i]["soluong"] * arr[i]["giaban"]
print(f"Tong tien hang la {tongtienhang}")
#