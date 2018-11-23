#Christian Hill
#Prgram 08
#COMS-170-OE01
#  a program with a function that accepts a string and an argument
#and returns a copy of the string with the first character of each
#sentence capitilized
# ----------------------------------------------------------------------
# Variable              Type                Purpose
# ----------------------------------------------------------------------
#                             
#                             


print("--------------------------------------------------------")
print("This program Capitalizes your sentences for you")
print("--------------------------------------------------------")

#ask the user their name and info
strName = input("Type anything you want: ", )
print("----------------------------------------------------------")

strCapitalize = strName.capitalize() # capitalize first character

strSentences = ""
words = list(strName.split(". ")) # create list based on each sentence
for i  in range(len(words)): # loop through list which is each sentence
    words[i] = words[i].strip() # remove any leading or trailing spaces
    words[i] = words[i].strip(".") # remove any periods

    words[i] = words[i][:1].upper() + words[i][1:] # concantenate string with first letter upper
    strSentences += words[i] + ". " # concantenate a final string with all sentences

print("Capitalized Sentences: ", strSentences) # print results
print()


    
  
               
       
