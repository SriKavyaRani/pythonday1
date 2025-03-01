for i in range(1,101):
    print(i)

print("------------------------------------------")

n=10
sum=0
for i in range (1,n+1):
    sum+=i
    print(i)

print("------------------------------------------")



print(sum)
print((n*(n+1))/2)

n=1
while n<=50:
    if n%2==0:
        print(n)
    n+=1

print("------------------------------------------")


num=int(input("Enter a number:"))
rev=0
sum=0
count=0
while num>0:
    rem = num % 10
    rev = rev*10 + rem
    num = num // 10
    sum+=rem
    count+=1
print(rev)
print(sum)
print(count)

while True:  
    num = int(input("Enter a number (negative to stop): "))  
    if num < 0:  
        print("Negative number entered. Exiting...")  
        break  # Exit the loop  
    print("You entered:",num)

print("------------------------------------------")




# 4. Print all numbers from 1 to 100 that are divisible by 3 and 5 using a For Loop:

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")

# 5. Implement a menu - driven program when the user can choose to:
#    1. Find the square of a number
#    2. Find the cube of a number
#    3. Exit

num = int(input("Enter a Number"))
num2  = int(input("Enter a number from 1 to 3"))
while True:
    if num2 == 1:
        num=num**2
        print("The square of", num, "is:")
        False
        break
    elif num2 == 2:
        num=num ** 3
        print("The cube of", num, "is:", )
        False
        break
    elif num2 == 3:
        False
        break
    else:
        print("Enter the choice from 1 to 3 only")
        break

print("---------------------------------------------------------")



