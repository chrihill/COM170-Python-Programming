#Christian Hill
#Prgram 06
#COMS-170-OE01
#   This program will read all of the numbers stored in a file,
#calculate the total and display the value as total points, calculate the average score
#then display the value as a percent score, and will handle IOError/ValueError exceptions.
# ----------------------------------------------------------------------------
# Variable              Type                Purpose
# ----------------------------------------------------------------------------
# fltTotal              Integer             Calculates the total sum of the numbers found on the data file
# amount                Float               Calculates the total average percent of the numbers found on the datat file
# count                 Integer             Wil read the rest of the file until there is no more data
              
def main():
    print("--------------------------------------------------------")
    print("This program will take the total and the percent average from a data file")
    print("--------------------------------------------------------")

    try:
        #Start total accumlator at 0
        fltTotal = 0
        count = 0
        
        #open the file for reading
        infile = open('numdata.txt.','r')
     
        #read the first line of the  file
        line = infile.readline()

        #read until no more data
        while line != "":
            #convert string value to number
            fltValue = float(line)
        
            #add to the total
            fltTotal += float(fltValue)
            line = infile.readline()

            #add to the count
            count += 1
              
        #close the file
        infile.close()

        #Display the numbers and print their total
        print('The Numbers are: ', count)
        print('Their total is: ', fltTotal)

        #calculate the percent average amount
        amount = fltTotal/count
        
        #Display the numbers and print their percent amount
        print ('Their average is: ', format (amount,  '9,.2f'), '%')

    except IOError:
        #program encountered a read error
        print('An error(1) occures while reading a data file')

    except ValueError:
        # program encountered a numeric value error
        print('An error(2) occures while reading a data file')
    else:
        #if no errors were encountered
        print("--------------------------------------------------------")
        print("No errors discovered")
    finally:
        # this occurs whether there are errors or not
        print("--------------------------------------------------------")

        
#Call the main function
main()
    

