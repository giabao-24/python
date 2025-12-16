# r is read ,a is add,w is write
arr = [1,2,3,4,5,6]
with open("num.txt","w",encoding="utf-8") as f:
  for i in arr:
    f.write(f"{i} ")
with open("num.txt","r",encoding="utf-8") as f:
  for i in f:
    print(i)
arr2 = [9,10,11,12]
with open("num.txt","a",encoding="utf-8") as f:
  for i in arr2:
    f.write(f"{i} ")
with open("num.txt","r",encoding="utf-8") as f:
  for i in f:
    print(i)