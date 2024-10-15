#Devesh Sukhdeo
#Period 1-2 
#10/15/24
'''
GrubHub Program
Version 1: If the user responds “yes” - say great!
If the user responds with anything else say: “NO?! So who is cooking?”
'''

x = str(input("Did you order delivery?"))
if x == "yes" or x == "Yes" or x == "YES" or x == "Y" or x =="y":
    print("Great!")
else:
    print("NO?! So who is cooking?")
