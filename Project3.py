#Christian Hill
#Prgram 03
#COMS-170-OE01
#Program asks user to enter the numerical equivilent for a date.
#Variables used: intDate as an integer to store numerical date, intName to display the month

#Dispaly Asking the Date
print ('What is the date?')


#Get choice from user

intDate = 0

#User Input if wrong then "Error" is displayed
intDate = int(input('Enter your selection: '))

if intDate == 1:
    print ('It is the month of: January')
elif intDate == 2:
    print ('It is the month of: February')
elif intDate == 3:
    print ('It is the month of: March')
elif intDate == 4:
    print ('It is the month of: April')
elif intDate == 5:
    print ('It is the month of: May')
elif intDate == 6:
    print ('It is the month of: June')    
elif intDate == 7:
    print ('It is the month of: July')
elif intDate == 8:
    print ('It is the month of: August')
elif intDate == 9:
    print ('It is the month of: September')
elif intDate == 10:
    print ('It is the month of: October')
elif intDate == 11:
    print ('It is the month of: November')
elif intDate == 12:
    print ('It is the month of: December')

else:
    print ('Error') #This is not a number 1-12
