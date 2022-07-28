##1.Write a program to detect double spaces in a string. (count of double space or count of any char)

# aName = "The Green Fingers School"
##To find the count of spaces.

# subString = " "
# countof=aName.count(subString)
# print(f"count of space in: '{aName}' is {countof}") 
#Ans: count of space in: 'The Green Fingers School' is 3
 
##To find the count of specific Char.

# subString = "e"
# charCount=aName.count(subString)

# print(f"Count of Letter:{subString} is {charCount}")

##Ans:- Count of Letter:e is 4

############################################-----------------------------------------------------------------
# #2.	Write a program to format the following letter using escape sequence characters.
# Dear  Candidate, 
# 	We are delight to inform you that you have cleared all rounds of interview and we are extending offer to join us.
# Thank you,
# HR
##Answer is Below
##Note: While writing with escape sequence we have to always use backslash.

import email


aEmail= ('Dear Candidate,\n\t\tWe are delighted to inform you that you have cleared all rounds of interview and we are extending offer to join us.\nThanks, \nHR.')
# print(aEmail)

############################################-----------------------------------------------------------------

# 3. From above solution (2) replace ‘Candidate’ with your name and HR name with some other name. By using some string operation function

ReplaceName=aEmail.replace("Candidate","Shakti")

##Ans:- 
print(f"replace the name from the email to:\n {ReplaceName}")

##Output:- replace the name from the email to:
#Dear Shakti,
#         We are delighted to inform you that you have cleared all rounds of interview and we are extending offer to join us.
# Thanks,
# HR.

############################################-----------------------------------------------------------------
#4.	Replace the double spaces from problem 3 with single spaces.
##Ans:-  

subStringSpace= "  "
rep=aEmail.replace("\t\t","")
print(rep)

############################################-----------------------------------------------------------------