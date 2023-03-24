# """list comprehension is a way to create a new list with less syntax"""
# # list =[expression for item in iterable]
# """ expression is here i*i
# for item => for i 
# iterable => in range(1,11) """
# # squares=[]
# # for i in range(1,11):
# #     squares.append(i)
# # print(squares)

# # this can be done within less line of code using list comprehension

# sq=[i for i in range(1,11)]
# print(sq)



# students=[100,20,49,84,92,44,23,11]
# # passed_students=[i for i in students if i>=60]
# passed_students=[i if i>=60 else "FAILED" for i in students ]
# print(passed_students)

