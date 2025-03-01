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
