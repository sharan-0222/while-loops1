num=int(input("pls enter a number- "))
sum=0
temp=num
while temp>0 :
    div=temp%10 
    sum=sum+div**3
    temp=temp//10
if sum==num :
    print(f"{num} is an armstrong number")
else :
    print(f"{num} is not an armstrong number")
