# Dictionary is a collection of key-value pairs.


Dict = {"key":"value","name":"Shakti","Birth":10081993,"time":1.30} 

print(type(Dict))       #<class 'dict'>
print(Dict["Birth"])    # 10081993
#when we have dictionary and need to extract the value from the dicitonary than we should always use key from dictionary in square bracket.

#--------------------------------------------------------------------

Dict["Birth"] = "10_Aug_1993"
print(Dict["Birth"])
# when we want to update the value then we can directly assign or update the value of key by using above method.

#--------------------------------------------------------------------

#In Dicitionary Key is Immuatable and the value is mutable. Where in we can change the value in dicitonary and not the Key.
#Key will always be unique in the Dicitonary.
#we can add new key and its value directly by using the below method.

Dict["Colours"] = ['white','red','black'] 

print(Dict)

cl = (Dict["Colours"])

print(cl[1])

# if we find a list inside the Dictionary and we want to extract the specific value from the list than we can use the above method.
#By assiging the list to variable and then printing the variable with index.

#--------------------------------------------------------------------

