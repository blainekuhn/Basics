a = 0
b = 1
print(a)
while len(str(a)) < 10:
  a, b = b, b + a
  print(a)
