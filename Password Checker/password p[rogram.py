#simple password system
#allow the user to type in something, save it to variable, save it  to the variable called "password"

#lets create a loop
while True:
    #we must ask it each time, or we cannot replace the value for "password"
    password = input  ("What is the password?")
    #determine if the password is correct
    if password == "abc123":
         print ("ACCESS GRANTED")
         #we also must stop this loop when the user gets it correct
         break
    #the else statement covers all situations where the if statement fails to execute
    else:
         print("ACCESS DENIED")

    #highlighting code and pressing tab can group-tab
