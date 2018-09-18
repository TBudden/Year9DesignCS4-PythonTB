#Input
fName = input("What is your first name: ")
lName = input("What is your last name: ")
#Process
result = fName[0] + "." + lName
#create codename using letters of 1st and last name
lenlName = len(lName)
codename = fName[0:3] + "." + lName[2] + lName[4]
#Output
print("Hi "+result)
print("your codename is: "+codename)