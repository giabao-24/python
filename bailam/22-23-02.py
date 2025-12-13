#cau1
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