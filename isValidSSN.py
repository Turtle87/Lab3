def isValidSSN(userInput):
    validity = 0
    number = 0
    userInput2 = userInput
    if userInput == "Done":
        return userInput
    
    # Count the number of digits
    for lines in userInput:
        for ch in lines:
            if ch.isalpha():
                return False
            if ch.isdigit():
                number += 1
    #Check if input is a 9 didgit number.
    if number == 9:
        validity += 1
        
    #Test for proper format.  
    if len(userInput) == 11 and userInput[3] =="-" and userInput[6] =="-":
        validity += 1
    #If the veriable = 2 then the input is valid.       
    if validity == 2:
        return True
        
    else:
        return False
