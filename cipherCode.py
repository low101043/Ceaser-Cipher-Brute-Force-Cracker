
from termcolor import cprint, colored
def input_Cipher(Cipher, shift):


    Clear = ""    #the plaintext message 
    for character in Cipher:      #For every letter in the Cipher
        if character == " ":      #If the character is a space add the space to the plaintext
            Clear = Clear + " "     
        elif character == ".":    #For every letter which is a fullstop add a fullstop to the plaintext
            Clear = Clear + "."
        elif character.isalpha() == True:                           #If the character is anything but a fullstop/ space (Need to work it with other punctuation)  DON'T USE @ IT MESSES UP Cipher
            asciiValue = ord(character)       #Find AsCII value
            characterTwo = asciiValue - shift        #Take/Add the the shift.  CAN CHANGE THIS
            if characterTwo < 97 :            #If the shift is add change to >90 and if shift os minus change to <65
                characterTwo = characterTwo + 26      #Add shift Change to -26 Minus shift change to + 26
            clearCharacter = chr(characterTwo)    #Change the ascii value back to a letter then added to the plaintext
            Clear = Clear + clearCharacter
     
    return Clear

def word_checker(message):
    
    """Checks for words in message"""
    wordToUse = ""
    rightMessage = False
    
    for letter in message:
        if letter == " ":
            if wordToUse in ["the", "be", "to", "of", "and", "in", "that", "have", "it", "for", "an", "well", "only", "even", "back", "is"]:
                rightMessage = True
                wordToUse = ""
            else:
                wordToUse = ""
        elif letter == ".":    #For every letter which is a fullstop add a fullstop to the plaintext
                pass
        else:
            wordToUse = wordToUse + letter
    return rightMessage
        
print(colored("Welcome to a ceaser Cipher Brute force cracker.  Please enter your text and the program will try and break it.", "cyan"))
cprint("By Nathaniel Lowis", "blue", "on_white")

print(colored("Please check my other program up by searching NathanielLowis", attrs = ['underline']))

cipherToUse = input("Enter Cipher:") #Just inputs the cipher DON'T CHANGE
cipher = cipherToUse.lower()
for i in range(1,26): 
    finalMessage = input_Cipher(cipher, i)
    yesOrNo = word_checker(finalMessage)
    if yesOrNo == True:
        print("\n", finalMessage, "\nThis could be the right message.  It has a shift of {}".format(i))  
    else:
        pass
    
