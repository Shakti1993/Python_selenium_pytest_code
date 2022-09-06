
# items = [1,5,8,10.5,54,87,63,7489,5465,1,2,5,4,9,4,52,7,6,3,4,8,41,31,]



# ## Find the Int greater than 10 from the above list.
# for item in items:
#     if str(item).isnumeric() and item>10:
#         print(item)


# for item in items:
#     if item == 100:
#         print("list of element:",item)
#     elif item > 10:
#         print("list of ele:",item) 
# else:
#     print("good to go")   

# #################################_-----------------------------------
# # Assignment

# ## Add the interger from below string.
# userWord = "C4e7d9n6e"
# sum= 0

# for char in userWord:
#     if char.isdigit():
#         sum+=(int(char))
# print(sum)       


# for item in range(0,6):
#     print(items[item])

# #################################_-----------------------------------

# list = [1,5,8,10.5,54,87,63,7489,5465,1,2,5,4,9,4,52,7,6,3,4,8,41,31,]

# # for item in list:
# #     print("element of items",item)



# userWord = "C4e7d9n6e"

# sum = 0

# for item in userWord:
#     if item.isdigit():
#         sum+=(int(item))
# print(sum)

# #################################_-----------------------------------

list = [1,5,8,10.5,54,87,63,7489,"red",'white',5465,1,2,5,4,9,4,52,7,6,3,4,8,41,31,]

# for item in list:
#     print("element of items",item)

# for item in list:
#     if str(item).isnumeric() and item > 100:
#         print(item)

# for item in list:
#     if str(item).isalpha():
#         print(item)


# #################################_-----------------------------------
# #################################_-----------------------------------



# # program to print duplicate numbers in a given list
# # provided input
# list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9,10,10,10,20,30,51,21,51,23,23]
 
# new = []  # defining output list
 
# # condition for reviewing every
# # element of given input list
# for a in list:
 
#      # checking the occurrence of elements
#     n = list.count(a)
 
#     # if the occurrence is more than
#     # one we add it to the output list
#     if n > 1:
 
#         if new.count(a) == 0:  # condition to check
 
#             new.append(a)
 
# print(new)
 


# #################################_-----------------------------------
# #################################_-----------------------------------

## Find the duplicate from the list using for loop and conditional expressions

lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
x = []
y = []
for i in lis:
    if i not in x:
        x.append(i)
for i in x:
    if lis.count(i) > 1:
        y.append(i)
print(y)

