import re
# Get user's name
name = input("Please enter name:")
# while name has incorrect characters
while re.search('[^a-zA-Z\n]',name):
    #Print out an error
    print("illegal name - Please use only letters")
    #Ask for the name again(if it's incorrect, while loop starts again)
    name = input("Please enter name:")
print("The name inputted is...", name)