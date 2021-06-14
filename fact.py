#factorial of number
num=int(input("enter number"))
num=5
if num<0:
   print("sorry,factorial doesnt exit")
elif num==0:
   print("factorial of 0 is 1")
else:
   f = 1
   for i in range(1,num+1):
    f=f*i
print("factorial of num is",f)