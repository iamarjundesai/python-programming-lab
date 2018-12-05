num=int(input("enter the number"))

factorial =1

if num<0:
   print("Sorry")
elif num==0:
   print("fact is one")
else:
     for i in range(1,num+1):
              factorial = factorial*i
     print("the fact of",num,"is", factorial) 
