# Robert Benard
# Function Sample 4
# COMS-170
# 02/22/2016
# This program calculates sales tax and total through a single function
# Variable      Type        Purpose
# fltSubtotal   float       store subtotal
# fltSalesTax   float       store sales tax
# fltTotal      float       store total 

def main():
    print("This application calculates sales tax based on a subtotal entered")
    fltSubtotal = float(input("Enter subtotal: "))
    fltSalesTax, fltTotal = CalcTotal(fltSubtotal)
    print("Item               Amount")
    print("Subtotal", format(fltSubtotal,'16,.2f'))
    print("Tax", format(fltSalesTax,'21,.2f'))
    print("Total", format(fltTotal,'19,.2f'))
    
    

def CalcTotal(fltSubTotalValue):
    # Calc sales tax
    fltSalesTaxAmount = fltSubTotalValue * .06
    # Calc total
    fltGrandTotal = fltSubTotalValue + fltSalesTaxAmount
    # Return sales tax and grand total
    return fltSalesTaxAmount, fltGrandTotal

main()
