num = int(input("Enter a number to check palindrome or not"))
temp = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if temp == rev:
    print(rev,"It is a Palindrome Number")
else:
    print(rev,"It is not a Palindrome Number")


print("-------------------------------------------------------131")

num = int(input("Enter a number:"))
sum = 0
i = 1 
print("The divisors of", num, "are:", end=" ")
while i<num:
    if num % i == 0:
        print(i,end=" ")
        sum = sum + i
    i += 1
if sum == num:
    print("\n",num, "is a perfect number")
else:
    print("\n",num, "is not a perfect number")

print("----------------------------------------------")


a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
while b > 0:
    rem = a % b
    a = b
    b = rem
GCD = a
print("GCD of two numbers is:", GCD)

print("-------------------------------------------------")

x = int(input("Enter the first number:"))
y = int(input("Enter the second number"))
if x > y:
    big = x
else:
    big = y
while True:
    if (big % x == 0) and (big % y == 0):
        LCM = big
        break
    big = big + 1
print("LCM of two numbers is:", LCM)

print("------------------------------------------------------")


