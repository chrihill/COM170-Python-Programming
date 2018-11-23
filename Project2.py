#Christian Hill
#Prgram Assignment number
#COMS-170-OE01
#This application calculates the totsl bill at a resturant
#Variables: intSubtotal as the subtotal input, ftTip as the 18% tip, ftTax as the 6% tax, ftGrandtotal as the total input of all the variables

intSubtotal = int(input('Enter subtotal of Bill: '))

ftTip = int(intSubtotal * 0.18)
ftTax = int(intSubtotal * 0.06)

#Calculate Grand total
ftGrandtotal = float(intSubtotal + ftTip + ftTax)

#Diplay to user
print('Subtotal \t', intSubtotal)
print('Tip \t', ftTip)
print('Tax \t', ftTax)
print('Grandtotal \t', format(ftGrandtotal, ' .2f'))
