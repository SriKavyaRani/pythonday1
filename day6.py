print('Positive, Negitive or Zero')  #1
user1 = input('Enter a number: ')   #1
if user1.isdigit() or (user1[0] == '-' and user1[1:].isdigit()):  #n
    user11 = int(user1)  #n
    if user11 < 0:  #1
        print(f'{user11} is Negative')  #1
    elif user11 == 0:  #1
        print(f'{user11} is zero')  #1
    elif user11 > 0: #1
        print(f'{user11} is positive')  #1
else:
    print('Invalid input')#1
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(n)')
print(' ')


print('Even or Odd') #1
user2 = input('Enter a number : ')  #1
if(user2.isdigit()):  #n
    user22 = int(user2)  #n
    if(user22 % 2 == 1):  #1
        print(f'{user22} is odd')  #1
    else:
        print(f'{user22} is even')  #1
else:
    print('Invalid')  #1
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(n)')
print(' ')


print('vote validation')  #1
age = input('Enter u r Age : ')  #1
if age.isdigit():  #n
    age1 = int(age)  #n
    if 0 < age1 < 18:  #1
        print('Not Eligible for vote')  #1
    elif(age1 >= 18):  #1
        print('Eligible for vote')  #1
else:
    print('Invalid')  #1
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(n)')
print(' ')

print('Check equal,greater or smaller')
n1,n2 = map(int,input('Enter two numbers with space : ').split())  #n
if (n1 == n2):  #1
    print('equal')  #1 
print(f'{n1} is greater') if (n1 > n2) else print(f'{n2} is greater')  #1
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(n)')
print(' ')


print('check grade to marks')
marks = int(input('Enter marks : '))  #1
print('Pass') if (marks) >=40 else print('Fail')  #1
print('Time Complexity : ','O(1)')
print('Space Complexty : ', 'O(1)')
print(' ')


day = int(input("Enter a number for days : "))  #1
if(day == 1):      #1
 print("Sunday")   #1
elif(day == 2):    #1
 print("Monday")   #1
elif(day == 3):    #1
 print("Tuesday")  #1
elif(day == 4):    #1   
 print("Wednesday")#1  
elif(day == 5):    #1  
 print("Thursday") #1     
elif(day == 6):    #1  
 print("Friday")   #1  
elif(day == 7):    #1   
 print("Saturday") #1     
else:      
 print('Invalid')  #1  
print('Time Complexity : ','O(1)')
print('Space Complexty : ', 'O(1)')
print(' ')  


print('calculator')
a,b = map(int,input('Enter two numbers : ').split())  #n
cal = input('Enter required operation of first three letters or operators : ').lower()  #n

def on(cal):  #1
    if (cal == 'add' or cal == '+'):  #1
        return a+b  #1
    elif (cal == 'sub' or cal == '-'):  #1
        return a-b  #1
    elif (cal == 'mul' or cal == '*'):  #1
        return a*b  #1
    elif (cal == 'div' or cal == '/'):  #1
        if(b == 0):  #1
           return 'divison with 0 is not possible' #1
        return a/b  #1
    else:
        return 'invalid'  #1
print(on(cal))  #1
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(n)')
print(' ')  


try: #1
    mon = int(input("Enter a number for Months : "))  #1
except(ValueError):   #1
    print('Enter non negitive numbers only')   #1
else:
    if(mon == 1):           #1
        print("January")    #1
    elif(mon == 2):         #1
        print("February")   #1
    elif(mon == 3):         #1
        print("March")      #1
    elif(mon == 4):         #1
        print("April")      #1
    elif(mon == 5):         #1
        print("May")        #1    
    elif(mon == 6):         #1    
        print("June")       #1
    elif(mon == 7):         #1
        print("July")       #1    
    elif(mon == 8):         #1
        print("August")     #1    
    elif(mon == 9):         #1        
        print("September")  #1        
    elif(mon == 10):        #1    
        print("October")    #1        
    elif(mon == 11):        #1    
        print("November")   #1        
    elif(mon == 12):        #1        
        print("December")   #1            
    else:  
        print('Invalid')    #1            
print('Time Complexity : ','O(1)')
print('Space Complexty : ', 'O(1)')
print(' ')


print('Greatest of three numbers')
a , b , c = input("Enter three nums seperated by space : ").split()  #n 
if a.isdigit() and b.isdigit() and c.isdigit():  #1
    a1,b1,c1 = int(a),int(b),int(c)  #1
    if (a1 > b1 ) and (a1 > c1):  #1
        print(f'{a1} is greater')  #1
    elif (b1 > a1) and (b1 > c1):  #1
        print(f'{b1} is greater')  #1
    else:
        print(f'{c1} is greater')  #1
else:
    print('Invalid input')  #1
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(n)')
print(' ')


print('check Leap year')
years = input('Enter a year : ')  #1
if (years.isdigit()):  #n
    year = int(years)   #1
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  #1
        print(f'{year} is a leap year.')  #1
    else:
        print(f'{year} is not a leap year.')  #1
else:
    print('Invalid input')  #1
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(n)')
print(' ')


print('Classify Characters')
vowles = 'aeiou'
char = input('Enter a single character : ').lower()  #n
if (len(char)==1):  #1
    if(char.isalpha() or not(char.isalnum())):  #1
        if (char in vowles):  #1
            print(f" '{char}' is vowle")  #1
        elif(char.isalpha()):  #1
            print(f" '{char}' is consonant")  #1
        else:
            print(f" '{char}' is special Character")  #1
    else:
        print('Invalid input')  #1
else:
    print('Enter single char  only')  #1
print('Time Complexity : ','O(1)')
print('Space Complexty : ', 'O(1)')
print(' ')


print('Grade Calculation')
user_marks = input('Enter your marks : ')  #1
if(user_marks.isdigit()):  #n
    marks = int(user_marks)  #1
    if(marks >= 90 and marks <= 100):  #1
        print('Grade A')  #1
    elif(marks >=80 and marks < 90 ):  #1
        print('Grade B')  #1
    elif(marks >=70 and marks < 80):  #1
        print('Grade C')  #1
    elif(marks > 100):
        print('Grade A')
    else:
        print('Fail')  #1
else:
    print("Invalid input")  #1
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(n)')
print(' ')


print('Valig triangle or not : ')
s1,s2,s3 = input("Enter length of three sides seperated by space : ").split()  #n
if s1.isdigit() and s2.isdigit() and s3.isdigit():  #n
    side1,side2,side3 = int(s1),int(s2),int(s3)   #1
    if((side1+side2) > side3 and (side2+side3) > side1 and (side3+side1) > side2):  #1
        print(f'Form a valid Triangle with side lengths {side1},{side2},{side3}.')  #1
    else:
        print(f'Not form valid Triangle with side lengths {side1},{side2},{side3}.')  #1
else:
    print('Invalid Input')  #1
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(n)')
print(' ')


print('print 1 to 100 Numbers')
for i in range(1, 101):  #n
    print(i,end=' ')   #1
print(' ')
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(1)')
print(' ')


print('sum of numbers')
user = input('Enter a range of number : ')  #1
if(user.isdigit()):  #n
    num = int(user)  #1
    print(f' sum of first {user} numbers is : {(num*(num+1))//2}' )  #1
else:
    print("Invalid input")   #1
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(n)')
print(' ')


print('All even and odd numbers between 1 and 50')
even = [] #1
odd = []  #1
i = 1  #1
while i <= 50:  #n
    if(i % 2 == 0):  #1
        even.append(i)  #1
        i=i+1   #1
    else:
        odd.append(i)  #1
        i=i+1  #1
print('even numbers : ',even)  #n
print('odd numbers : ',odd)   #n
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(n)')
print(' ')


print("Multiplication of given number upto 20 multiples")
mul = input('Enter a number for table first 20 multiples : ')   #1
if mul.isdigit() or (mul.count('.') < 2 and mul.replace('.', '', 1).isdigit()):  #n
    table = float(mul)  #1
    for i in range(1, 21):  #1
        result = i * table  #1
        if result.is_integer():  #1
            print(int(table), 'x', i, '=', int(result))  #1 
        else:
            print(table, 'x', i, '=', format(result, '.1f'))   #1
else:
    print('Invalid input')  #1
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(1)')
print(' ')


print('Reverse a number and its sum')
user= input("Enter a number for reverse : ")  #1
if user.isdigit():  #n
    user_num=int(user)  #1
    i = 0  #1
    sum = 0   #1
    while user_num > 0:  #d
        last = user_num % 10  #1
        sum = sum+last  #1
        i = i * 10 + last  #1
        user_num =  user_num // 10  #1
    print(f'Reversed number of {user} is ', i)  #1
    print(f'Sum of digits in {user} is ', sum)   #1
else:
    print('Invalid input')   #1
print('Time Complexity : ','O(log n)')
print('Space Complexty : ', 'O(1)')
print(' ')


print('Count the digits of a number')
user6= input("Enter a number : ")   #1
if user6.isdigit():  #n
    user=int(user6)   #1
    i = 0   #1
    while user > 0:  #d
        i=i+1  #1
        user = user // 10   #1
    print(f'Total no of digits in {user6} is {i}')   #1
else:
    print('Invalid input')   #1
print('Time Complexity : ','O(log n)')
print('Space Complexty : ', 'O(1)')
print(' ')


print('Enter a numbers until enter a negitive numbers')
while "jagan" == "jagan":  #1
    user = input("Enter a number: ")  #1
    if user.isdigit() or (user.startswith('-') and user[1:].isdigit()):  #n
        wish = int(user)  #1
        if (wish < 0): #1
            print("Negative number entered. Exiting loop.")  #1
            break  #1
    else:
        print("Invalid input. Please enter a valid number.")  #1
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(1)')
print(' ')


print('first 10 fibinocci series numbers')
first = 0  #1
second = 1   #1
for jagan in range(10):  #1
    print(first,end=" ")  #1
    first,second = second,first+second   #1
print()
print('Time Complexity : ','O(1)')
print('Space Complexty : ', 'O(1)')
print(' ')


def check_prime(n):  #1
    if not n.isdigit():  #n
        return "Invalid input"  #1
    num = int(n)  #1
    if num <= 1:  #1
        return f"{num} is not a prime number"  #1
    for i in range(2,num):  #num
        if num % i == 0:  #1
            return f"{num} is not a prime number"  #1
    return f"{num} is a prime number"  #1
user_input = input("Enter a number to check if it's prime: ")  #1
print(check_prime(user_input))  #1
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(1)')
print(' ')


user=input('Enter a number for factorial : ')  #1
if(user.isdigit()):  #n
    fact = int(user)    #1
    i=1  #1
    res = 1  #1
    while i <= fact:   #fact
        res = res * i  #1
        i = i+1  #1
    print(f'The factorial of {user} is {res}.')  #1
else:
    print("Invalid input")  #1
print('Time Complexity : ','O(n)')
print('Space Complexty : ', 'O(1)')
print(' ')


print('numbers from 1 to 100 that are divisible by 3 and 5 are :')
for i in range(15,101,15):  #1
        print(i,end=" ")  #1
print()
print('Time Complexity : ','O(n/15)')
print('Space Complexty : ', 'O(1)')
print(' ')


name = input('User Name : ')  #1
def password():  #1
    print('password : 123456')  #1
    print()  #1
    real = '123456'  #1
    attempt = 0  #1
    while attempt < 3:  #1
        user_pass = input('Enter your password : ')  #n
        if user_pass == real:  #1
            print('Login successful!')  #1
            break  #1
        else:
            attempt+=1  #1
            remain = 3 - attempt  #1
            if remain > 0:  #1
                print(f"Incorrect password. You have {remain} attempts left.")  #1
            else:
                print("Access denied. You have used all your attempts.")  #1
                print(f'The correct password is {real}')  #1
password()
print('Time Complexity : ','O(1)')
print('Space Complexty : ', 'O(1)')
print(' ')