# Write a function that converts an object into an array, where each element represents a key-value pair in the form of an array.
def convert_to_array(obj):
    list1 = []
    for i in obj:
        list1.append([i, obj[i]])
    return list1

obj = {'a': 1, 'b': 2}
result = convert_to_array(obj)
print(result)
obj = {'shrimp': 15, 'tots': 12}
result = convert_to_array(obj)
print(result)
obj = {}  
result = convert_to_array(obj)
print(result)  


# toArray({ shrimp: 15, tots: 12 }) ➞ [["shrimp", 15], ["tots",12]]
# toArray({}) ➞ []


#Create a function that takes two numbers as arguments (num, length) and returns an array of multiples of num until the array length reaches length.
def array_of_multiples(num, length):
    list1 = []
    for i in range(1, length+1):
        list1.append(num*i)
    return list1

result = array_of_multiples(7, 5)
print(result)
result = array_of_multiples(12, 10)
print(result)
result = array_of_multiples(17, 6)
print(result)

# Create the function that takes an array with objects and returns the sum of people's budgets.
def get_budgets(obj):
    sum1 = 0
    for i in obj:
        sum1 += i['budget']

    return sum1

result = get_budgets([
  { 'name': 'John', 'age': 21, 'budget': 23000 },
  { 'name': 'Steve',  'age': 32, 'budget': 40000 },
  { 'name': 'Martin',  'age': 16, 'budget': 2700 }
])  
print(result)

# Create a function that takes an array of objects like { name: "John", notes: [3, 5, 4]} and returns an array of objects like { name: "John", avgNote: 4 }. If a student has no notes (an empty array) then let's assume avgNote: 0.
def get_student_avg(obj):
    for i in obj:     
        if len(i['notes']) == 0:
            i['avgNote'] = 0
        else:
            i['avgNote'] = sum(i['notes']) / len(i['notes'])
        i.pop('notes')  # Removes 'notes' from the dictionary
    return obj

# Test Case
result = get_student_avg([
  { "name": "John", "notes": [3, 5, 4] },
  { "name": "Steve", "notes": [6, 8, 8] },
  { "name": "Anna", "notes": [] }  # Case with no notes
])          

print(result)


# Create a function that moves all capital letters to the front of a word.
def cap_to_front(s):
    for i in s:
       if i.isupper():
           s = i + s
    return s

# Test Case 
result = cap_to_front("hApPy") #o/p is Happy
print(result)

# Count each occurrence of number(can not use predefined function).
def count_occurrences(lst, val):
    count = 0
    for i in lst:
        if i == val:
            count += 1
    return count

# Test Case 
result = count_occurrences([1, 1, 1, 1, 1], 1)
print(result)


# # Count each occurrence of number(can not use predefined function).
# def count_occurrences(lst, val):
#     count = 0
#     for i in lst:
#         if i == val:
#             count += 1
#     return count

# # Test Case
# result = count_occurrences([1, 1, 1, 1, 1], 1)
# print(result)
# result = count_occurrences([1, 1, 1, 1, 1], 2)
# print(result)
# result = count_occurrences([1, 1, 1, 1, 2], 2)
# print(result)



# Write a function that accepts an array of strings. Return the longest string(can not use predefined function).

def find_longest(lst):
    max_len = 0 #initialize max_len to 0 
    max_str = '' #initialize max_str to empty string
    for i in lst:
        if len(i) > max_len:
            max_len = len(i)
            max_str = i

    return max_str

# Test Case
result = find_longest(["hello", "world", "hi"])
print(result)

# print 2 largest string in array of strings find 2 max strings in array of strings(can not use predefined function).
def find_2_largest(lst):
    max1 = max2 = lst[0]
    for i in lst:
        if len(i) > len(max1):
            max2 = max1
            max1 = i
        elif len(i) > len(max2) and i != max1:
            max2 = i
    return max1, max2


# def find_largest(lst):
#     max1 = max2 = lst[0]
#     for i in lst:
#         if i > max1:
#             max2 = max1
#             max1 = i
#         elif i > max2 and i != max1:
#             max2 = i
#     return max1, max2

# # Test Case
# result = find_largest(["hello", "world", "hi"])
# print(result)

def find_largest(lst):
    max1 = max2 = lst[0]
    for i in lst:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2 and i != max1:
            max2 = i
    return max2

# Test Case
result = find_largest([1, 2, 3, 4, 5])      
print(result)


# Most Commonly Used two Character in String(can not use predefined function)
def most_common_char(s):
    dict1 = {}
    for i in s:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    max1 = max2 = 0
    char1 = char2 = ''
    for i in dict1:
        if dict1[i] > max1:
            max2 = max1
            char2 = char1
            max1 = dict1[i]
            char1 = i
        elif dict1[i] > max2:
            max2 = dict1[i]
            char2 = i
    return char1, char2

# Test Case
result = most_common_char("hello world")
print(result)



# Write a program to print below pattern based on rows

# rows = 7
# output: 
#     *
#    * *
#   * * *
#  * * * *
#   * * *
#    * *
#     *

def print_pattern(rows):
    for i in range(1, rows+1):
        if i <= rows//2:
            print(' '*(rows-i) + '* '*i)
        else:
            print(' '*(i-1) + '* '*(rows-i+1))

# Test Case
print_pattern(7)


# Take an array of objects
# input: [{event:"Marriage",time:"06:30"},{event:"Farewell",time:09:00},{event:"FreshersParty",time:12:45}
# ]
# output: Farewell

def find_event(arr):
    min_time = 24
    event = ''
    for i in arr:
        time = int(i['time'].split(':')[1])
        if time < min_time:
            min_time = time
            event = i['event']
    return event

# Test Case
result = find_event([{"event":"Marriage","time":"06:30"},{"event":"Farewell","time":"09:00"},{"event":"FreshersParty","time":"12:45"}])
print(result)


# Count each occurrence of number(can not use predefined function).
# Input: [1,6,3,1,5,9,7,2,1,9,3,7,8,9,10] , no find=7
# 			Output: 1 present 2 times.
# 				   2 present 1 times.
# 				   3 present 2 times.
# 				   5 present 1 times …….  Etc

def count_occurrences(lst, val):
    dict1 = {}
    for i in lst:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    for i in dict1:
        print(i, 'present', dict1[i], 'times')

# Test Case
count_occurrences([1,6,3,1,5,9,7,2,1,9,3,7,8,9,10], 7)


#transpose of matrix
def transpose_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

# Test Case
result = transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)

#print only boundary elements 
def print_boundary_elements(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == 0 or i == len(matrix)-1 or j == 0 or j == len(matrix)-1:
                print(matrix[i][j], end=' ')
            else:
                print(' ', end=' ')
        print()

# Test Case
print_boundary_elements([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def print_boundary_elements(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == 0 or i == len(matrix)-1 or j == 0 or j == len(matrix)-1:
                print(matrix[i][j], end=' ')
            else:
                print(' ', end=' ')
        print()

# Test Case
print_boundary_elements([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Write a function that takes a string and returns a string with the correct case for character titles.
def correct_title(txt):
    return txt.title()

# Test Case
result = correct_title("jOn SnoW, kINg IN thE noRth.")
print(result)

# Write a function that takes a string and calculates the number of letters and digits within it. Return the result in a dictionary.
def count_all(txt):
    letters = 0
    digits = 0
    for i in txt:
        if i.isalpha():
            letters += 1
        elif i.isdigit():
            digits += 1
    return {'LETTERS': letters, 'DIGITS': digits}

# Test Case
result = count_all("Hello World123")
print(result)



# Create a function that moves all capital letters to the front of a word.
# 	Examples :

# capToFront("hApPy") ➞ "HAPpy"

# capToFront("moveMENT") ➞ "MENTmove"

# capToFront("shOrtCAKE") ➞ "OCAKEshrt"
def cap_to_front(s):
    return ''


    # Reverse a Number Using while Loop
def reverse_number(number):
    reverse = 0 #initialize reverse to 0 because we need to store the reverse number 
    while number > 0:#if number is greater than 0 then we need to reverse the number be
        remainder = number % 10
        reverse = reverse * 10 + remainder
        number = number // 10
    return reverse


    # Program to Display Characters from A to Z Using Loop with count.
    # Output: A1 B2 C3 D4 E5 F6 ……. Z26 


def display_characters():
    count = 1
    for i in range(65, 91):
        print(chr(i) + str(count), end=' ')
        count += 1

# Test Case
display_characters()



#  Program to count vowels and consonants in a given String.

# 			Input: i am ram
# 			Output: 3 vowels 3 consonants.
def count_vowels_consonants(s):
    vowels = 0
    consonants = 0


    for i in s:
        if i.lower() in 'aeiou':
            vowels += 1
        elif i.isalpha():
            consonants += 1
    return vowels, consonants

# Test Case
result = count_vowels_consonants("i am ram")
print(result)

# program to print whether a number is prime or not

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Test Case
result = is_prime(int(input("Enter a number: ")))
print(result)


#prime or even number
def is_prime_even(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True if num % 2 == 0 else False
# Test Case
result = is_prime_even(int(input("Enter a number: ")))
print(result)

# Program to print the Fibonacci series.
def fibonacci_series(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a+b
# Test Case
fibonacci_series(10)    
