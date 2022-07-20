## There are main 5 types of Variables in Python

##1. String Variable which is also know as "Str"
##Anything which is inside the double inverted comma that represents String value.

##2. Float Varibale which has decimal in the value E.g: "10.0"
## Any Integer values which has a decimal in it is alwys known as Float.

##3. Integer Variable which is basically numbers but without "" or decimal in it.

##4. Boolean Variable is the one which defines TRUE and FALSE in Python.

##5. None Varibale has only None in it which is unknown value.


## The following are the Variable format for refernce.

##String Variable

a= "Shakti" ## its a String
a1="10" # its a string
a2= "10.0" #its a string
a3="True" #its a string
a4= "None" #its a string

## Any value which is in "" are by default know as String
print(type(a3))  #<class 'str'>

####
##Float Varibale
b= 10.2 ##it has decimal point

print(type(b)) #<class 'float'>



###
#Integer Varibale
c=50
print(type(c)) #<class 'int'>

###
##Boolean Varibale

d= True
print(type(d)) #<class 'bool'>


####
##Nonetype Varibale

e= None

print(type(e)) ##<class 'NoneType'>




a=10                #assigned variable
temp=(type(a))      #Assignment Operators

print(type(a))
print (temp)


a = 10      # integer 
a2 = -20    # integer

temp_1 =type(a)
print(temp_1)

print(type(a2))

b = 16.8    # float type
b2 = 3.65   # float type

temp_2=type(b)
print(temp_2)  #<class 'float'>
print(type(b2)) #<class 'float'>

c = "Hello"     # string type
c2 = 'something' # string

c3 = '''CT10'''  #string

c4= """sdkjfla
    asdfadsf
    dsfa"""  # Multi string

c5 = "10"

temp_3= type(c) 
print(temp_3)   #<class 'str'> 

print(type(c2)) #<class 'str'>

d = True    # boolean only True or False
d2 = False  # boolean only True or False

temp_4 = type(d)
print(temp_4)   #<class 'bool'>

print(type(d2)) #<class 'bool'>

