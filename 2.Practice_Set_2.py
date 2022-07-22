# #1. Write a python program to print the contents of a directory using os module. 

# # import os
# # print (os.getcwd())  ## we will get current workng directory(path)
# ##PS F:\Credence IT Classes\My_Python_Code>

# ###########------------------------------------------------------------
# #####--------------
# ##2.Install an external module and use it to perform an operation of your interest. 
# #(e.g. play MP3 audio)  
# from audioop import avg
# import playsound
# #we will use pip to install external module (playsoun) to play mp3
# # Pip Command is ##pip install playsound
# # once the module is installed then we will write the program

# # from playsound import playsound
# # playsound("F:\Bhool_Bhulaiyaa.mp3") ##executed
# ## and to stop the music we will use Cntrl+C in terminal and the music will stop##

# ########################--------------------------------------------------------
# ###-----------------------------------
# ###3.Write a Python program to add two numbers.

a=10
b=20
print(a+b) #30 ##with variables
print(10+20) #30 ##without varibales

# ########################--------------------------------------------------------
# ###-----------------------------------

# ####4.Write a Python program to find the remainder when a number is divided by Z(Integer).

# ## Reminder is the value which is left after the divison of two integer.

x=10
z=7

a=x%z
print(a)

# ########################--------------------------------------------------------
# ###-----------------------------------
# ##
# # 5.Check the type of the variable assigned using the input() function.

a="Hello"
b= 10.5
c=None
d=True

input(type(a)) ##<class 'str'>
input(type(b)) ##<class 'float'>
input(type(c)) ##<class 'NoneType'>
input(type(d))  ##<class 'bool'>

# ########################--------------------------------------------------------
# ###-----------------------------------

# #
# #6.Use a comparison operator to find out whether a given variable a is greater than b or not. 

a=34
b=80

print(a==b) ##False ## a is not equal to b
print(a>b)  ##False ##a is not greater than b
print(a<b) ##True ##a is smaller than b
print(a!=b) ## True ## a is not equal to b so its True.

# ########################--------------------------------------------------------
# ###-----------------------------------

# #7.Write a Python program to find the average of two numbers entered by the user.
# Average of two numbers 
a = input("enter first number") 
b = input("enter second number") 
print((a+b)/2) 

a=500
b=1050

print((a+b)/2)

# ########################--------------------------------------------------------
# ###-----------------------------------

# ##8.Write a Python program to calculate the square of a number entered by the user.

from math import pow

#input a integer
digit= int(input("Enter an integer number"))

#Square Calculation
square= int(pow(digit,2))

#print
print(f"Square of :  {digit} is {square}")  

# ##################################################################################################################
















































































































































































































































