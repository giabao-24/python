def clean_str(a):
  result = ""
  for i in a:
    if i.isalpha():
      result += i
  return result
print(clean_str("py12thon34"))