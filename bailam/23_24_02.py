arr1 = [] #qtht
arr2 = [] #thi
se = set()
print("List diem qua trinh hoc tap")
for i in range(0,3):
  dic1 = {}
  dic1["masv"] = input("Nhap ma sv ")
  se.add(dic1["masv"])
  value = float(input("Nhap diem qua trinh "))
  dic1["diemqt"] = value
  arr1.append(dic1)
print("List diem thi")
for i in range(0,2):
  dic2 = {}
  dic2["masv"] = input("Nhap ma sv ")
  value = float(input("Nhap diem thi "))
  dic2["diemthi"] = value
  arr2.append(dic2)
for masv in se:
  diemqt = 0
  diemthi = 0
  for dic1 in arr1:
    if dic1["masv"] == masv:
      diemqt = dic1["diemqt"]
  for dic2 in arr2:
    if dic2["masv"] == masv:
      diemthi = dic2["diemthi"]
  if diemqt == 0 or diemthi == 0:
    diemtb = 0
  else:
    diemtb = diemqt * 0.4 + diemthi * 0.6
  print(f"Ma sv: {masv} Diem tb: {diemtb}")
def delete_special_char(a):
  result = ""
  for i in a:
    if(i.isalpha() or i.isdigit() or i.isspace()):
      result += i;
    else:
      result += " ";
  return result

save_data = ""
with open("data.txt","w",encoding= "utf-8") as f:
  f.write("Hello@World#2024\nThis$is%a^test&file*\n")
new_data = save_data.split("\n")

