# a= 10+20        #int+int #30
# b= "10"+"20"  #str+str 
# c= 10+"20"    #int+str

# temp=type(a)

# print(temp)       #<class 'int'>

# temp_1=type(b)
# print(temp_1)     #<class 'str'>

#------------------------------------------------------------------------
##TypeCasting
## In Typecasting we can change the type of the datatype using type function.

# avalueint=10   #int
# bvaluefloat=10.5  #float

# print(type(avalueint))  #<class 'int'>

# #Now to convert float into int we have to use the following--

# bvalueint = int(bvaluefloat) #float is converted into int

# print(avalueint+bvalueint)  # the ans. will be => 30

###--------------------------------------------------------------------------------------

# avalueint=10   #int
# bvaluestr="10.5"  #string

# ##when we have decimal into string and we want to add it with the int than first we have to convert the string into float 
# ##and later float can be converted into int.

# #print(avalueint+bvaluestr) #without conversion it will show ERROR

# #Convert the String into Float

# bvaluefloat = float(bvaluestr) ##Conevrted

# print(avalueint+bvaluefloat) ##ans will be => 20.5

#----------------------------------------------------------------------------------------------

# avalueint= 10
# bvaluefloat="20.5"

# ## this is another way to code and convert the datatype and do the addition

# print(avalueint+float(bvaluefloat))

##
a=10
b=10.5
c="Shakti"

d=int(b)

print(type(d)) ##float converted into INT.

