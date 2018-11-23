#Christian Hill
#Prgram 07
#COMS-170-OE01
# a program that performs an analysis on final grades in a course
# ----------------------------------------------------------------------
# Variable              Type                Purpose
# ----------------------------------------------------------------------
#                             
#                             


#Define initial variables
def main():
    print("--------------------------------------------------------")
    print("This program will display the highest, lowest, and average scores in a course")
    print("--------------------------------------------------------")

    #Get the test scores from the users
    scores = get_scores()

    #get the total of the test scores
    total = get_total(scores)

    #get the highest test score
    highest = max(scores)

    #get the lowest test score
    lowest = min(scores)

    #get the average score
    average = total / (len(scores))
    
    #Display all the info
    print ("           Score information")
    print ("--------------------------------------------------------------")
    print ("--------------------------------------------------------------")
    print ("The Highest Score:               ", highest)
    print ("The Lowest Score:                ", lowest)
    print ("The Average score:           ", format (average,    '9.2f'))
    print ("--------------------------------------------------------------")
    print ("--------------------------------------------------------------")


#This function gets a series of test scores and stores them in a list
def get_scores():
    #creat an empty list
    test_scores = []

    #creat a variable to control the loop
    again = 0

        #get the scores from the user and add them to the list
    while again != 20:
            #Get the scores
            value = float(input('Enter a test score: '))
            #Add the values to the list
            again += 1
            test_scores.append(value)
     
    #return to the list
    return test_scores

#This function accepts the list as an argument and returns the total of the values in the list
def get_total(value_list):
    #creat a variable as an accummlator
    total = 0

    #calculate the total of the list elements
    #was value_list
    for num in value_list:
        total += num

    #return the total
    return total

main()

        






               
                
  
               
       
