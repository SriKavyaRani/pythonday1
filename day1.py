#rite a program to check if a given number is positive, negative, or zero.

num=float(input("enter a number"))
if num>0:
    print("positive")
elif num==0:
    print("zero")
else:
     print("negative")

print("-------------------------------")

#Determine if a number is odd or even. 


num1=int(input("enter a number"))
if num1%2==0:
    print(num1,"even")
else:
    print(num1,"odd")

print("----------------------------------------------")

#Check if a person is eligible to vote (age >= 18). 

age=int(input("enter a age"))
if age>=18:
    print(age,"i can vote")
else:
    print(age,"i cannot vote")

print("------------------------------")

#Wrint "Pass" if a student scores more than 40 marks; otherwise, print "Fail." 

num2=int(input("enter a num2:"))
num3=int(input("enter a num3:"))
if num2>num3:
    print(num2,"is gratest")
else:
    print(num3,"is smallest")

print("-----------------------------------------")

#print "Pass" if a student scores more than 40 marks; otherwise, print "Fail." 

num5=40
if num5<=40:
    print("pass")
else:
    print("fail")

print("---------------------------------------------")

#write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.).

num=int(input("Enter a number:"))
if num==1:
    print(num,"Monday")
elif num==2:
    print(num,"Tuesday")
elif num==3:
    print(num,"Wednesday")
elif num==4:
    print(num,"Thursday")
elif num==5:
    print(num,"Friday")
elif num==6:
    print(num,"Saturday")
elif num==7:
    print(num,"Sunday")
else:
    print("not a weeks")

print("------------------------------------------")

#Implement a simple calculator to perform addition, subtraction, multiplication, and division. 

num8=int(input("enter a number"))
num9=int(input("enter a number"))
imp=input("enter an operation")
if imp=="add":
    print(num8+num9)
elif imp=="sub":
    print(num8-num9)
elif imp=="mul":
    print(num8*num9)
elif imp=="div":
    print(num8/num9)
else:
    print("invalid")


print("-----------------------------------------------")

#Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.). 

num10=int(input("Enter a number:"))
if num10==1:
    print(num10,"January")
elif num10==2:
    print(num10,"Feb")
elif num10==3:
    print(num10,"March")
elif num10==4:
    print(num10,"April")
elif num10==5:
    print(num10,"May")
elif num10==6:
    print(num10,"June")
elif num10==7:
    print(num10,"July")
elif num10==8:
    print(num10,"Aug")
elif num10==9:
    print(num10,"Sep")
elif num10==10:
    print(num10,"Oct")
elif num10==11:
    print(num10,"NOv")
elif num10==12:
    print(num10,"Dec")
else:
    print("INVALID")

print("------------------------------------------")

#Write a program to find the greatest of three numbers.

num11=int(input("Enter a number1:"))
num12=int(input("Enter a number2:"))
num13=int(input("Enter a number3:"))
if num11>num12 and num12>num13:
    print("num12 is grater")
elif num11>num12 and num11>num13:
    print("num11 is grater")
elif num13 > num11 and num13>num12:
    print("num13 is grater")
else:
    print("all three are grater  number")

print("-----------------------------------------------")

#Check if a year is a leap year. 

year=int(input("Enter a year:"))
if(year%4==0 and year%100!=0) or (year%400==0 and year%100 == 0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")


print("-----------------------------------")

#Calculate the grade of a student based on the marks they 

marks=int(input("Enter marks:"))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<=89:
    print("Grade B")
elif marks>=70 and marks<=79:
    print("Grade c")
elif marks<70:
    print("Fail")
else:
    print("INVALID")

print("-----------------------------------------------")

#Write a program to check if three sides length form a valid  triangle
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("It is a valid triangle.")
else:
    print("It not a valid triangle.")




