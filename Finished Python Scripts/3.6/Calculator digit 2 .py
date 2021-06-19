print("Do you want to add subtract multiply or divide")
a = input()
if a=='multiply':
  print("enter value 1")
  m1 = int(input())
  print("enter value 2")
  m2 = int(input())
  mans = int(m1)*int(m2)
  print("your answer is",mans)
  
elif a=='divide':
  print("enter value 1")
  d1 =int(input())
  print("enter value 2")
  d2 = int(input())
  dans = d1/d2
  print("your answer is",dans)
  
elif a=='add':
  print("enter value 1")
  a1 =int(input())
  print("enter value 2")
  a2= int(input())
  aans = a1 + a2
  print("your answer is",aans)
  
elif a=='subtract':
  print("Enter value 1 ")
  s1 = int(input())
  print("enter value 2")
  s2 = int(input())
  sans = s1 - s2
  print("your answer is",sans)
  
else:
  print("choose one of the folowing choises")
