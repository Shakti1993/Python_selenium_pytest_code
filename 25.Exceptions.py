# In Exceptions we need to write either except or finally to close the syntax and execute the program succesfully..
# While writing any specific error exception we need to write except command at the end of the code.

# # Exceptions occurred when program or statement is syntactically correct but it resulted in error


# a =[10,285,12,32,54,25]

# try:
#     print(a[1])
#     print(a[2])
#     print(a[3])
#     try:
#         print(a[9])
#     except IndexError as R:
#         print("Error of Index:=",R)
# except Exception as ex:
#     print("Error Occured in Exceptions:=",ex)
# finally:
#     print("whatever the result finally block will execute")



#####################---------------------------------------------------------------------

# a = input("Enter a number to divide 200 := ")

# try:
#     result = 200/int(a)
#     print ("Division of the given input :",result)
# except ValueError as V:
#     print("If Value_Error occured:=",V)
# except SyntaxError as Sy:
#     print("If Syntax error occured :=",Sy)    
# except Exception as ex:
#     print("If any Error occured :", ex)
# finally:
#     print("what is wrong please find.")

#####################---------------------------------------------------------------------


a = [10,20,21,5,4,3,54]

try:
    print(a[1])
    try:
        print(a[5])
    finally:
        print('finally executed')
        try:
            print(a[9])
        finally:
            print("second try failed")
except Exception as e:
    print('error occured',e)
else:
    print('try executed')
