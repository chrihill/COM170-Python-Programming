#Christian Hill
#Prgram 04
#COMS-170-OE01
#Calculates the value of a savings account with compounding interest after 10 years
# -----------------------------------------------------------------
# Variable          Type            Purpose
# -----------------------------------------------------------------
#  P               float            Principle
#  r               float            Percent interest rate
#  t               Integer          Time in Years
#  n               Integer          Times-per-year
#  amount          float            Total compounded interest

# declare and initialize variables
P = 0
r = 0
t = 0
n = 1

# provide the user directions
print("--------------------------------------------------------")
print("Annual compounded interest calculator")
print("--------------------------------------------------------")
print()
print()

#Loop through 10 years
while n <= 10:
    P = float(input('Enter the principle: '))
    r = float(input('Enter the annual interest rate in decimal: '))
    if(P<=0 or r<=0):
        print('All inputs must be positive')
    t += 1
    n += 1

    amount = P*(1 + r/n)**(n*t)
    print('Final amount = ',amount)

#Display compound interest
print()
print("Total compounded interest: ", format(amount, '.2f'))
