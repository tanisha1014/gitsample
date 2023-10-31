# code to find sum of digits
n=int(input("enter any number"))
sum=0
while(n!=0):
    r=n%10
    sum=sum+r
    n=n//10
print("the sum of digits of a number is",sum)    
#moving towards second one
print("the sum is",sum)
