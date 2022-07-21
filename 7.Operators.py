#Arithmetic Operators (+, -, *, /, etc.)
## In arthmatic operators we can add,substract,etc.

a=10
b=20

print(a+b) ##30
print(a-b) ##-10
print(a*b) ##200
print(a/b) ##0.5

a=a+b
print(a) ##30

#------------------------------------------------------------------------------------------
##Assignment Operators (=, +=, -=, *=, /=, etc.)

a=10
b=20
print(a+b) #30 Normal Arthmatic Addition operators

a=a+b
#print(a) ## a value is assgined as 10+20 so it will give 30 value to a

a+=b 
#steps 
# 1st it will add a+b and then it will do a=a+b.
# here the assignment operators will work as first it will operate the first given value and then operate with the next.
##eg: 1st + will be operated and than = will operate

print(a) ## now here the ans will be ##50.

a-=b
print(a)

#-------------------------------------------------------------------------------------------

##Comparison Operators (==, >=, <=, >, <, !=, etc.)


##In Comparssion Operators both the value and the datatype should be same to have the result TRUE
##If the datatype or the value which is compared is not the same than it will show false.


aint= 10
bint= 11
# int
print(aint==bint) ##False
print(aint==bint) ##True
print(aint>=bint) ##False
print(bint>=aint) ##True
print(aint<=bint) ##True as the the aint value is greater than bint

bfloat=10.5
print(aint==bfloat)
bfloat= 20.5
cstr="25.5"
cstr1="25.5"
print(cstr==cstr1)

####----------------------------------------------------------------------------------
#Logical Opertors (and,or,not)
#In Logical Operator the last value will be executed.
a=50
b=40
c=2.5
print(a and b)

print(b==c and a==b)
print(a==b and c==a)

print(a or b)

######################################################



