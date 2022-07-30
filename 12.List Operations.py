listVarible = [1, 8, 7, 2, 21, 15]  

#We have several subfactors which we can use in list datatype and we can acess them same with setVariable '.'


# 1. sort() updates the list to [1,2,7,8,15,21]

## while using sort type we dont have to hold the sort value into any variable.
## By default it will use ascending order in sort type.

# listVarible.sort()
# print(listVarible) ##  [1, 2, 7, 8, 15, 21] ##it will mutate and change the order into ascending order.

##Now if we want the list variable into descending format than we can use "Reverse" after sort with Boolean.

# listVarible.sort(reverse=True)
# print(listVarible) ##[21, 15, 8, 7, 2, 1]

############################################

##2. reverse() – updates the list to [15,21,2,7,8,1]

## In Reverse type the list of values will reverse from last to first and not in descending or ascending.
## That the differnce between sort.reverse and only Reverse type.

# listVarible.reverse()
# print("the reverse value of list is :", listVarible)
##the reverse value of list is : [15, 21, 2, 7, 8, 1]

############################################

#3. append(8) – adds 8 at the end of the list
# Append will add the element in the set of value by creating new place for the new value.

listVarible.append(1000)
print(listVarible) ## [1, 8, 7, 2, 21, 15, 1000]

##We can also add string or any datatype in List.

listVarible.append("white") ##adding string value

print(listVarible) ##[1, 8, 7, 2, 21, 15, 1000, 'white']

listVarible.append(True)

print(listVarible) ##[1, 8, 7, 2, 21, 15, 1000, 'white', True]

############################################

##insert(3,8) – This will add 8 at 3 index and rest items will shift index by 1

## Insert type is different as compared to Append in List Function.
## Here when we want to insert any value in list then it push the index value forward and make space to new value entered to insert.

listVarible.insert(4,5000)
# ## here the index values has been pushed forward to next index and the enterd value is assigned to existing index value.

print(listVarible) ##[1, 8, 7, 2, 5000, 21, 15, 1000, 'white', True]

############################################

#pop(2) – It will delete the element at index 2 and return its value
#by default it take default last index if not provided

## IN POP type if we do not give any index to pop to delete than automatically it will delete the last index from the list and give the remaining value in in output.

listVarible.pop()  ##Here we have not assigned any value to delete from the list.
print(listVarible) ##[1, 8, 7, 2, 5000, 21, 15, 1000, 'white'] 
## Now by default it has deleted the last value from the index.

## if we want to delete certain valu than we hava to assign the value to POP.

listVarible.pop(0)
print(listVarible) ##[8, 7, 2, 5000, 21, 15, 1000, 'white']

## Now we can see the given index has been deleted from the List of SET.

############################################--

##remove(21) – It will remove 21 from the list

##  Now Remove and Pop are two different functions in List both perform differently.
## Remove will delete the elements directly when assigned to it.

#listVarible.remove(1) #ValueError: list.remove(x): x not in list
##we got error because we deleted the value through pop.
#print(listVarible)

listVarible.remove(8) ##now we have assigned the value to delete from the index.

print(listVarible) ##[7, 2, 5000, 21, 15, 1000, 'white']

## we can see the given value has been deleted from the Set of Lists.

############################################--

