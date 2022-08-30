#Dicitonary Methods
## In dictionary we can add list as well as tuple.

Dict = {"key":"value","name":"Shakti","Birth":10081993,"time":1.30} 
Dict['colours'] = ['white','red','black','blue']


#1. items() : returns a list of (key,value) tuple.

#whenever we use items operations in dicitonary then the output will be dispalyed in tuple and each key annd value will be seprated by using tuple.

# print(Dict.items())  ##dict_items([('key', 'value'), ('name', 'Shakti'), ('Birth', 10081993), ('time', 1.3)])

#================================================================================================================

#2.	keys() : returns a list containing dictionary’s keys.
# With the help of key operation we can find all the keys present inside the dicitonary.

#print(Dict.keys())                 #dict_keys(['key', 'name', 'Birth', 'time'])

#================================================================================================================

# 3. Update({“friend”: “Sam”}) : updates the dictionary with supplied key-value pairs.#
# With Update operation in Dicitionary we can update or add new key values and also we can add multiple key values.
# Basically update is used to add bulk key values and where in with the help of assign operators we can only add one key value.

# Whenever we use udpate operation to add any key values in DIcitonary than we must use curly barckets.{}

Dict.update({'fav_colours':'white','fav_city':'Pune'})

print(Dict)  #{'key': 'value', 'name': 'Shakti', 'Birth': 10081993, 'time': 1.3, 'fav_colours': 'white', 'fav_city': 'Pune'}
 
#================================================================================================================

# 4.get(“name”) : returns the value of the specified keys. (and value is returned)

#With get operation in we get the value of the given specified key then be it list or tuple.

Dict['num'] = (1,2,)
 
print(Dict.get('name'))    #Shakti

print(Dict.get('colours'))  ##['white', 'red', 'black', 'blue']

print(Dict)
