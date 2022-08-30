## like List Tuple also has different private methods which can be used only in tuple.

## and they are Count with which we can count the given information same like List Count finction.
## and INdex which gives the elements index number.

######################
##Count Method
## count(1) – It will return the number of times 1 occurs in a.


ATuple= 10,20,30,'white','red','blue','white','white','White'

print('count of given element : ',ATuple.count('white'))  ##one way

### Second Way ###
# CountTuple=ATuple.count('white') 

# print(f"Count of White in ATuple are :{CountTuple}") ### Count of White in ATuple are :3 

#################################################

##Index Method
#index(1) – It will return the index of the first occurrence of 1 in a.

ATuple= 10.5,50,50,60,840,'white','red','blue',50

print(ATuple) ##The output from this command will by default add Round Bracket to Tuple.
#(10.5, 50, 50, 60, 840, 'white', 'red', 'blue')

print('INdex of element:',ATuple.index('white')) #INdex of element: 5

# indexTuple=ATuple.index(50,3)

# print(f"Last Index of '50': {indexTuple}") # Last Index of '50': 8

#################################################
