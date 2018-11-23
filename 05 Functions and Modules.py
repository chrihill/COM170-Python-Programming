#Christian Hill
#Prgram 05
#COMS-170-OE01
#A payroll program that pays time and a half for anything over 40 hours
# ----------------------------------------------------------------------------
# Variable              Type                Purpose
# ----------------------------------------------------------------------------
# hours                 float               hours worked
# rate                  float               payrate
# strtime               integer             amount of hours worked
# overtimehr            integer             amount of overtime hours worked
# overtime              integer             overtime pay
# regular               integer             regular hours and payrate
# totalpay              integer             total pay after total hours worked
               
def main ():

    print()
    print("This application calculates payroll")
    print()
    
    hours, rate = getinput()

    strtime, overtimehr, overtime  = calculate_hours (hours,rate)

    regular, totalpay  = calculate_payregular (hours, rate, overtime)

    calprint  (rate, strtime, overtimehr, regular, overtime, totalpay)



def getinput ():

    #calculate total hours worked and the wage earned to return to main
    #ask for the hours worked input
    print ()
    print ('How many hours were worked?')
    print ('Hours worked must be at least 8 and no more than 86.')
    hours = float(input('Enter total hours worked: '))

    #validate the hours
    while hours < 8 or hours > 86: 
        print ('Error--- The hours worked must be atleast 8 and no more than 86.')
        hours = float (input('Please try again:'))

    #Ask for the pay rate input
    print ('What is the pay rate?')   
    rate = float(input('Enter hourly wage:'))
    print ('The pay rate must be at least $8.50 and not more than $50.00.')
   
    #validate the payrate
    while rate < 8.50 or rate > 50: 
        print ('Error--- The pay rate must be at least $7.00 and not more than $50.00.')
        rate = float (input('Please try again:'))

    #set the return ratio
    return hours, rate
   
    

def calculate_hours (hours,rate):

    #calculate hours and overtime worked to return to main
    #If hours exceed 40 hrs
    if hours < 40:
        strtime = hours
        overtimehr = 0
    else:
        strtime = 40
        overtimehr = hours - 40
        
    #If hours does not exceed 40 hrs
    if hours > 40:
        overtimerate = 1.5 * rate
        overtime = (hours-40) * overtimerate
    else:
        overtime = 0

    #set the new return ratio    
    return strtime, overtimehr, overtime


def calculate_payregular (hours,rate,overtime):

    #calculate the the regular pay, overtime pay, and the total pay to return to main
    
    regular = hours * rate

    totalpay = overtime + regular

    #set the new return ratio
    return regular, totalpay
    

def calprint (rate, strtime, overtimehr, regular, overtime, totalpay):

    #Display all the info
    print ("           Payroll Information")
    print ()
    print ("Pay rate                $", format (rate,  '9,.2f'))
    print ("Regular Hours            ", format (strtime,  '9,.2f'))
    print ("Overtime hours           ", format (overtimehr,  '9,.2f'))
    print ("Regular pay             $", format (regular,  '9.2f'))
    print ("Overtime pay            $", format (overtime,  '9.2f'))
    print ("Total Pay               $", format (totalpay,  '9.2f'))

main ()
    
