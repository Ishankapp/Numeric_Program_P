def fibonacci(tcount):
 a=0
 b=1
 print(f"{a},{b}",end=",")
 sum=0
 count=2
 while(count<=tcount):
  sum=a+b
  a=sum
  b+=sum
  print(f'{a},{b}',end=',')
  count+=1
fibonacci(int(input("enter the numeber of elements that need to be printed")))
