##Note: While writing with escape sequence we have to always use backslash.

## While writing Escape sequence we have certain keywords we use which are as follows : 

# \n : Represents new line 

# \t : Represents tab (also we can consider it as space tab)

# \' : Represents single quote 

# \\ : Represents backlash

############################################-----------------------------------------------------------------


# Write a program to format the following letter using escape sequence characters.

# Dear  Candidate, 
# 	We are delight to inform you that you have cleared all rounds of interview and we are extending offer to join us.
# Thank you,
# HR
# #Answer is Below
# #Note: While writing with escape sequence we have to always use backslash.

# import email


aEmail= ('Dear Candidate,\nWe are delighted to inform you that you have cleared all rounds of interview and we are extending offer to join us.\nThanks, \nHR.')
print(aEmail)


# email = ('Dear Sir,\n\t We are really happy to be in Credence CLass.\n\t We have learned everything that we need to get a prefect job.\n\t Yours faithfully,\n\t Student.')

# print(email)


# # 3. From above solution (2) replace ‘Candidate’ with your name and HR name with some other name. By using some string operation function

# ReplaceName=email.replace("Sir","Shakti")

# ##Ans:- 
# print(f"replace the name from the email to:\n {ReplaceName}")

# ##Output:- replace the name from the email to:
# #Dear Shakti,
# #         We are delighted to inform you that you have cleared all rounds of interview and we are extending offer to join us.
# # Thanks,
# # HR.

############################################-----------------------------------------------------------------
#4.	Replace the double spaces from problem 3 with single spaces.
# ##Ans:-  

# subStringSpace= "  "
# rep=email.replace("\t\t","")
# print(rep)

# ############################################-----------------------------------------------------------------