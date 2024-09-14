#Create a 2-D list
matrix= [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

print(matrix)

#Number of rows
print(len(matrix))

#Number of columns
print(len(matrix[0]))

#Accessing an element 
print(matrix[1][2])

#Creating a matrix by taking input from user
rows= int(input("How many rows do you want?"))
columns= int(input("How many columns do you want?"))
mat1= []

for i in range(rows):
    temp= []
    for i in range(columns):
        x= int(input("Enter the element-"))
        temp.append(x)
    mat1.append(temp)
print(mat1)


             


