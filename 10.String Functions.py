
# avariable = "minimum"
################################################################
#len() function : It returns the length of the string.

# print("Length is:",len(avariable))  ###Length is : 7 
######################################################################

## Endswith Function ##
##Endswith(“rry”)  # We cannot use endswith function like this without any string.
## Endswith function only return in boolean.

# endSWith=avariable.endswith("mum") 

# endSWith_1 = avariable.endswith("umm") 

# print("ends with :",endSWith) #ends with : True

# print("not eends with:",endSWith_1) ## not eends with: False

# # ## We cannot use endswith operation with int datatypes.

######################################################################

# #Count Operation
# #it will show the total count of the available given word to variable.
# ## It returns in int.

# avariable= "minimum"

# Count1 =avariable.count('m') ## count take one argument.

# # the below program is one way to find the count of any word
# print("Count of the given value:" ,Count1) #Count of the given value: 2


# #2nd way to find the count of any word is ---

# ## Optional ===>> 
# #substring= 'i'  ## need to give one variable to find the given value inside the main string.

# print(f"count of subtring:'{Count1}") #count of subtring:,'m': 3

######################################################################

# capitalize Operation()
# # In this opertion the first letters will be converted into Capital Letters

# name1= "geeks"
# name2="of"
# name3="geeks"

# isCaps = name1.capitalize() + name2.capitalize() + name3.upper()    

# # joinCaps = name1.capitalize() + name2.capitalize() + name3.capitalize()

# print("1st letters in Caps:",isCaps) ##1st letters in Caps: ('Geeks', 'Of', 'Geeks')

# # print("join the name:",joinCaps) ## join the name: GeeksOfGeeks

# name="Shakti"
# name2="Patil"

# caps=name.capitalize(),name2.capitalize()

# print("Capital letters:",caps)


# ######################################################################

# ##find Opertion(word) 

# aname= "TheGreenfingersSchool"                                                      

# # substring= "fin"

# bname = aname.find("e")
# print(bname)   ## it will give the first occurance of the letter given inside the find. ## 2                                                        

# substring1="e"

# bname1=aname.find("e",3) # we have to add the number next to the previous substring input to find the second occurance.

# print(bname1)


# ######################################################################------------------------------------------


# aname = "TheGreenfingersSchoolTheGreenfingersSchoolTheGreenfingersSchool"

# # substring = "Green"

# repl_1 = aname.replace('Green','Red')


# print(repl_1)
# ##TheRedfingersSchool

# print(f"updated the value: '{substring}' to new value {repl_1}") ##Second way to update.
# ##updated the value: 'Green' to new value TheRedfingersSchool

# ###When we want to update the new updated value 2nd time.

# repl2= repl_1.replace("Red","White")

# print(repl2) ### TheWhitefingersSchool



########################################

# afind = "Heeeleelo"

# find_sec = afind.find('l',5)

# print(find_sec)

########################################

# areplace = "Hello"

# aRep = areplace.replace('l','z',1)

# print(aRep)

