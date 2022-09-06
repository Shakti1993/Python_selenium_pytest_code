# # #Set is a collection of non-repetitive elements

# # # In Set no duplicate values are allowed.
# # # Set is Unindexed and Unordered so to print any elements we cannot use index in Set.
# # #Elements in Sets are immutable but whole set is mutable.
# # #Set is also form by using curly barcket but in Set we only have one element.
# # #In Set we can write multiple data types elements
# # # In Set no elements can be duplicated and there will only one occurance of the elements.

# # ##by mistake even if we write two same elements in the Sets it will only take one occurance of the element.

# # ##---------------------------------------------------------------------------------------------

# # aSet = {10,20,26,154,'white','red',15,4,'white','red'} ##This is called a Set.
# # # print(type(aSet)) ##<class 'set'>

# # ##---------------------------------------------------------------------------------------------

# # ##To find the length of the set we use length operation.

# # print(len(aSet))   ## Length of Set is 8.

# # ## In the above set we can see two duplicated values which is 21 so the set has removed the duplicated value and displayed the actual length.


# # ##---------------------------------------------------------------------------------------------
# # # 2. Remove Operations (remove() : Updates the set and removes element from Set)
# # # In remove operations we can delete the particular element from Set.

# # # aSet.remove(20)
# # # print(aSet)  #{131, 10, 'white', 235, 1613, 21, 215, 154, 156}

# # ##---------------------------------------------------------------------------------------------

# # #3.pop() : Removes an random element from the set and returns the element removed.
# # # Pop operation is different than remove operations.
# # # In pop any random value will be removed from the set.


# # # print(aSet) # {'red', 4, 26, 10, 15, 20, 'white', 154}

# # # print(aSet.pop()) ## this will remove any random element from SET. #red is removed

# # # print(aSet) # {4, 26, 10, 15, 20, 'white', 154}

# # # print(len(aSet)) #7 length

# # ##---------------------------------------------------------------------------------------------

# # ##4.clear() : Empties the complete set

# # #aSet.clear() 

# # #print(aSet) ##set() By using clear operations in set we can empty or we can clear everything from inside the Set.

# # ##---------------------------------------------------------------------------------------------

# # # 5. union({8, 11}) : Returns a new set with all items from both sets. 

# # # When we use Union than it will tempararly add the given elements to the Sets but not any duplicate value.

# # aset = aSet.union({452,10,54,466}) #{26, 4, 452, 10, 15, 466, 20, 54, 'white', 154, 'red'}

# # print(aset)  #{26, 4, 10, 15, 20, 'white', 154, 'red'}


# # ##---------------------------------------------------------------------------------------------

# # # 6.intersection({8, 11}) : Returns a set which contains only items in both sets. #{8}

# # # print(aSet.intersection({452,10}))  ##{10}

# # ##---------------------------------------------------------------------------------------------

# # # Note : If we specify empty set with {} then by default the type will be considered as dictionary <class 'dict'>


# # if 100 in aSet: ####This statement is false
# #     print("Something is wrong")  
# # elif 101 in aSet:  ####This statement is also false
# #     print("Correctly used") 
# # elif 10 in aSet:  ####This statement is also true
# #     print("Good") ##So this is executed
# # else:
# #     print('good to go') 

# ##########################################################################################
# ##########################################################################################

# ### Operations in Sets ########

# # set = {1,8,5,6,'red',50,60,70,80,90,100,100,200}

# # to find the length from set we use below command..
# ## 1. Len Operators. Returns the length of the set

# # print(len(set))  ##12

# ###############################################################

# ## 2. Remove Operators ## takes argument
# # remove will update the set and remove the given element from the sets.
# ## set will be always unorganised and unindexed.

# # print(set)  

# # set.remove('red')

# # print(set) 

# ###############################################################

# ##3. POP() takes no argument
# ## Same in List the POP operators will remove any random value from the given set.

# # print(set) 

# # #set.pop(1) ##TypeError: set.pop() takes no arguments (1 given)

# # set.pop()

# # print(set)  

# ###############################################################

# # 4.##Clear() : Empties the set S

# # ## Clear operators will empty the set and return the cleared set in terminal.

# # set.clear() ##takes no argument

# # print(set)  ##set()

# # print(set)

# ###############################################################

# ##5. union({8, 11}) : Returns a new set with all items from both sets. #{1,8,2,3,11}
# ## If we want to add new set in the previous set than we can create a new set and with new variable we can add both the sets.
# ## Both combined sets will be assigned to new varibale where the new variable will return all the items from both sets.

# # set = {1,8,5,6,20,40,'red'}
# # set_1 = {10,20,30,40,8,'red'}

# # combined_Set = set.union(set_1)

# # print(combined_Set) 

# ###############################################################

# ##6. intersection()
# ## Returns a set which contains only items in both sets.
# ## Intersection operators combined two sets and return the common elements from both the sets in terminal.

# set = {1,8,5,6,20,40,'red'}
# set_1 = {10,20,30,40,8,'red'}

# print(set.intersection(set_1))

# ###############################################################



