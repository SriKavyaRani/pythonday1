# # sum of matrix elements
# def sum_of_matrix_elements(matrix):
#     sum1 = 0 #initialize sum to 0
#     for i in matrix: #iterate through the matrix
#         for j in i:     #iterate through the list in matrix one by one value will be stored in j
#             sum1 += j 
#     return sum1

# result = sum_of_matrix_elements([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(result)


# #print first row in matrix

# def print_first_row(matx):
#     for i in range(0,len(matx)): #iterate through the length of the matrix starting from 0 to the length of the matrix
#         print(matx[0][i], end=' ') #matx[0] will give the first row of the matrix and 
#     print()

# # Test Case
# print_first_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#print full 4 row and 4 column of matrix boundary elements
def print_first_row_and_column(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            if not (i == 1 and j == 1):
                print(matrix[i][j], end=' ')
            else:
                print(' ', end=' ')
         
        print()

# result=print_first_row_and_column([[-1,0,9],[1,2,3],[4,5,6]])
# print(result)
result=print_first_row_and_column([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(result)

#sum od matrix boundary elements

def sum_of_matx(matrix):
    sum1=0
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            if i==0 or i==len(matrix)-1 or j==0 or j==len(matrix)-1:
                sum1+=matrix[i][j]
    return sum1

result=sum_of_matx([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(result)   

#SUM OF DIAGONAL ELEMENTS
def sum_of_diagonal_elements(matrix):
    sum1 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                sum1 += matrix[i][j]
    return sum1
# Test Case
result = sum_of_diagonal_elements([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)




           
