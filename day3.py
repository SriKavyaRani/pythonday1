#feb n num

n=int(input("Enter a number:"))
num1=0
num2=1

print(num1)
print(num2)

for i in range(1,n-1):
    temp=num1+num2
    print(temp)
    num1=num2
    num2=temp


print("----------------------------------------------------")


#prime number -- one and it self
#Example-1
num1 = int(input("Enter num to check for prime"))

if num1 in [0,1]:
    print("Not a prime")
else:
    count=0
    for i in range(1,num1 + 1):
        if num1 % i ==0:
            count +=1
    print("prime number") if count == 2 else print("not a prime")

#Example-2 and 3:

num1 = int(input("Enter num to check for prime"))
spy = True
for i in range(2, int(num1**1/25)+1):    #in mun1 palce ne can write (2,num1//2+1)
    if num1 % i==0:
        spy = False
        print("not a prime")
        break

if spy:
    print("Prime")


#Example 4: In place of num1 we can write (int(num1**0.5)+1)




