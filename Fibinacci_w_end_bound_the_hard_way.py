end_of_list = 10
n1 = 0
n2 = 1
count = 0
lst = []


if end_of_list == 1:
   print("Fibonacci sequence up to %s: " %end_of_list)
   print(1)
else:
   print("Fibonacci sequence up to %s: " % end_of_list)
   while count < end_of_list:
       count+=1
       nth = n1 + n2
       n1 = n2
       n2 = nth
       lst.append(n1)

for a in lst:
  print(a,)
