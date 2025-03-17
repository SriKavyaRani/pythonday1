#binary search algorithm will work on sorted list only 
# list1 = [123,341, 566, 23, 11]
# search_elem = 566

# def binary_search(list1, search_elem):
#     low = 0
#     high = len(list1) - 1
#     flag = False

#     while low <= high:
#         mid = (low + high) // 2

#         if list1[mid] == search_elem:
#             return mid

#         elif list1[mid] < search_elem:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1

# result = binary_search(list1, 3)
# print(result)



#

# list1 = [2,1,-3,55,4.7,-32,77,-89]

# for i in range(len(list1)-1):
#     for j in range(len(list1)-1 - i):
#         if list1[j]>list1[j+1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]

#     print(list1)


#find the digits in a number

# def find_missing(input_num):
#     temp = input_num
#     digit_list = []
#     while temp > 0:
#         digit = temp % 10
#         digit_list.append(digit)
#         temp = temp // 10

#     list_max = max(digit_list)
#     list_min = min(digit_list)

#     for i in range(list_min, list_max+1):
#         if i not in digit_list:
#             print(i)
#         else:
#             print('num is present', i)
#     return

# num1= 1237
# find_missing(num1) 





num1 = [-4, -2, 6 ,10,2]
def min_max(num1):
    min_num = num1[0]
    max_num = num1[0]

    for i in num1:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
    return min_num, max_num

result = min_max(num1)
print(result)

#print even numbers and in between that print missing even numbers

num1 = [-4, -2, 6 ,10,2]
list_max = max(num1)
list_min = min(num1)

for i in range(list_min, list_max+1):
    if i % 2 ==0 and i not in num1:
        if i not in num1:
            print(i)
        else:
            print('num is present', i)



# Given array of N integer, the task is to replace each element of the array  by its rank in the array
#    Input: 20 15 26 2 98 6       Output:4 3   5   1  6 2

list1 = [20, 15, 26, 2, 98, 6]
list2 = sorted(list1)
rank = 1
list3 = []
for i in list2:
    list3.append(list1.index(i)+1)  
print(list3)    

def rank_array(list1):
    list2 = sorted(list1)
    rank = 1
    list3 = []
    for i in list2:
        list3.append(list1.index(i)+1)  
    return list3

result = rank_array(list1)
print(result)


# maxinum value in a list
list=[-4,-2,22,10,12]
first_max = float('-inf')

for i in list:
    if i > first_max:
        first_max = i   
print(first_max)

second_max = float('-inf')
for i in list:
    if i > second_max and i != first_max:
        second_max = i
print(second_max)










