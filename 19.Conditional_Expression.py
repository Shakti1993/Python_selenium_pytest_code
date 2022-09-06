#The if statement is how you perform this sort of decision-making. 
#It allows for conditional execution of a statement or group of statements based on the value of an expression. 

##Conditional Expression

## "if" is used to find if the given statement is true or false and accordingly print the result.
## "elif" is used when we are not sure if the 1st given statement is true or not than we use elif to check 2nd statemtent.
## and "Else" is used if both the given statement are wrong than display else statment.

## if one condition is true then it will execute the true statement and end the execution there itself.

## we can also write multiple if statements.

# if (condition1):		// if condition 1 is true
# 	print(“yes”)
# elif (condition2):		// if condition 2 is true
# 	print(“No”)
# else:				// May be
# 	print(“May be”)

####------------------------------------------------------------------------

# a=12
# b=54

# alist = [1,54,a,b]

# if 120 in alist:
#     print("True")
# elif a>b in alist:
#     print("Greater")
# elif 542 in alist:
#     print("true again")
# else:
#     print("false")



# if a<b in alist:
#     print("Greater")
# if 1<a in alist:
#     print("lesser")
# elif 54==b in alist:
#     print("correct")
# else:
#     print("Smaller")


# exp = 15

# if exp>=15:
#     print("Bonus granted")
# if exp>10:
#     print("less bonus")
# if exp>5:
#     print("no bonus")
# else:
#     print("work hard")

###############################################################################################
###############################################################################################

# exp = 15

# if exp==10:
#     print("Well Done")
# elif exp>5:
#     print("need to do better")
# else:
#     print("Do better")


alist = [1,5,1,6,8,1,10,"red"]

## Single line conditional satement 

print("true") if ("Red"in alist) else print("false") ##### Easy way

####

if ("resd" in alist):
    print("true")
if (54 in alist):
    print("right")
elif (10 in alist):
    print("correct")
else:
    print("false")

############################################################
a = 10
 
print("true") if a > 51 else print("false")


a = 10 
if a > 10:
    print("Greater")     # if body statement
                        # if body statement
    print("After only if")  # if body statement
print("Not part of if")