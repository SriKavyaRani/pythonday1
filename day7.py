# def check _prime(input_num):
#     if n<1:
#         return False
#     for i in range(2,input_num):
#         if input_num % i == 0:
#             return False

#     return True

# num1 = 1562
# temp = num1
# non_prime_sum = 0


# list=[1,2,"kavya",6]

# for i in list:
#         print(i)
# j=0
# while j<len(list):
#     print(j)
#     print(list[j])
#     j+=1
     
# list1=[1,2,3,4,5,6,7,-7]

# sum=0
# for i in list1:
#     sum+=i
#     print(sum)

# min_num=list1[0]
# max_num=list1[0]

# for i in list1:
#     if i<min_num:
#         mix_num=i
#     if i>max_num:
#         max_num=i
# print(min_num)
# print(max_num)


# list2=[1,2,-5,8,9,-3]

# k=int(input("Enter a number:"))
# print(list2[k])

#0 to len(list) -1
#-len(list1) to len(list1)

# if k>= -1 * len(list2) and k< len(list2):
#     print(list2[k])
# else:
#     print("index is out of range")


# num=[1,2,3,4,5,6,7,3,5,4,3,6,5]
# uniq=[]
# dup=[]
# for i in num:
#     if i not in uniq and i not in dup:
#         uniq.append(i)
#     elif i in uniq:
#         dup.append(i)
#         uniq.remove(i)

# print(uniq)
# print(dup)


# list1=[1,2,3,4,5,6,7,3,5,4,3]
# for i in range(len(list1)):
#     flag=True
#     for i in range(len(list1)):
#         if list[i] == list[j] and i!=j:
#             flag = False
#             print(list[i],"is dup")
#             break
#         # print(list[i],list[j])
#     if flag:
#         print(list[j],"id uniq")





#reverse a num

# num1 = int(input("enter a number"))

# def reverse_number(input_num)
#     temp = input_num
#     rev_num = 0

#     while temp > 0:
#         rem = temp % 10
#         rev_num = rev_num * 10 +rem
#         temp // =10

#     print(rev_num)



# def is_palindrome_number(input_num):
#     temp = input_num
#     rev_num = 0

#     while temp > 0:
#         rem = temp % 10 
#         rev_num = rev_num * 10 + rem 
#         temp //= 10  

#     return rev_num 


# print(is_palindrome_number(121))  
# print(is_palindrome_number(1001))

# factorial

# def factorial(n):
#     """Calculates factorial using a loop."""
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
    
#     result = 1
#     for i in range(1, n + 1):
#         result *= i  # Multiply each number from 1 to n
    
#     return result

# Example usage
# print(factorial(5))  # Output: 120
# print(factorial(3))  # Output: 6
# print(factorial(0))  # Output: 1
# print(factorial(-5)) # Output: "Factorial is not defined for negative numbers."


# # list1 = [1,2.2,True,5.5,6,7]
# def rev_list(input_list):
#     temp_list=[]
#     for i in range(len(input_list)-1,-1,-1):
#         temp_list.append(input_list[i])

#     return temp_list

# list = reverse_list(list1)
# print(list1)


# def reverse_num(input_num):
#     low = 0
#     high = len(input_num) - 1

#     while low < high:
#         input_num[low],input_num[high] = input_num[high],input_num[low]
#         low +=1
#         high -=1

#     return input_num

# print(reverse_num([1,2,3,4,5,6,7,8,9,10]))


# def revs_half_num(list):
#     mid=len(list) // 2
#     list[mid:] = list[mid:][::-1]
#     return list
# print(revs_half_num([1,2,3,4,5,6,7,8]))





#print digit in a list:

# def digit_sum(input_num):
#     temp = input_num
#     sum=0
#     while temp > 0:
#         digit = temp % 10
#         sum +=digit
#         temp //=10
#     return sum

# list1 = [202,89,112,88]
# output_list =[]

# for i in list1:
#     temp_res = digit_sum(i)
#     output_list.append(temp_res)
    
# print(output_list)


# #sum of even digits in a list:


# def digit_sum(input_num):
#     temp = input_num
#     sum=0
#     while temp > 0:
#         digit = temp % 10
#         if digit % 2 == 0:
#             sum +=digit
#         temp //=10
#     return sum

# list1 = [202,89,112,88]
# output_list =[]

# for i in list1:
#     temp_res = digit_sum(i)
#     output_list.append(temp_res)
    
# print(output_list)


print("----------------------------------------------------")




    


# def has_duplicate_digits(n):
#     """Checks if a number has duplicate digits using a while loop."""
#     digit_count = {}  # Dictionary to store digit occurrences
#     temp = n
    
#     while temp > 0:
#         digit = temp % 10  # Extract last digit
#         if digit in digit_count:
#             return True  # Found a duplicate
#         digit_count[digit] = 1
#         temp //= 10  # Remove last digit
    
#     return False  # No duplicates found

# # Input list
# numbers = [202, 89, 112, 88]
# output_list=[]
# for i in numbers:
#     input_list = has_duplicate_digits(i)
#     output_list.append(input_list)

# print(output_list)

# # output_list = [has_duplicate_digits(num) for num in numbers]
# print(output_list)  



# def arr(arr1,arr2):
#     for i in arr1:
#         if i not in arr2:
#             print("not a subset")
#             break
#     return "is subset"

# arr1=[1,3,4,5,2]
# arr2=[2,4,3,1,7,5,15]
# print(arr(arr1,arr2))


# #------------------------------------------------------------
# def arr(arr1,arr2):
#     for i in arr1:
#         if i not in arr2:
#             return False
#         return True

# arr1=[1,3,4,5,2]
# arr2=[2,4,3,1,7,5,15]
# print(arr(arr1,arr2))


# ------------------------------------------

# def num_in_list(list):
#     for num in list:
#         if num==i:
#             return True
#     return False

# i=input("enter a no:")
# print(num_in_list([1,4,10,-5,9.5,7]))


print("----------------------------------------------------")


def check_inc_order(input_num):
    temp = input_num

    prev_digit = 10
    while temp > 0:
        digit = temp % 10 #3 (0 to 9)
        if digit >= prev_digit:  #if we want true value of 223 then we have to write <=
            return False
        prev_digit = digit
        print(digit)
        temp //= 10

       
    return True


list1=[123,341,566,23,11]
print(check_inc_order(223)) 
# print(check_inc_order(2)) #2 is in increasing order
#output=[True,false,false,true,false]































#Ae