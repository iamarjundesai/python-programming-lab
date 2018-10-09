def armn(x):                         #defines function
     sum=0                           #considers sums value is 0
     a=x                             #defines variable value to x
     while (a>0):                    #starts while loop
        l=a%10                       #extracts last digit 
        sum+=l**3                    #cube of extracted digit 
        a=a//10                      #gives quotient of the input
     if sum==x:                      #checks if sum equals the input
        return "Armstrong No"        #
     else:
        return "NOT armstrong no"
x=int(input())
print(armn(x))
