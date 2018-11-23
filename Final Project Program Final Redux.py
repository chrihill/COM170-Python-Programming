#Christian Hill
#Final Project Program
#COMS-170-OE01
#This program will encrypt/decrypt input from the user and display it to the
#screen.

def main ():

     strOption = ""
try:
    #Starting Menu until user wants to exit
    strOption = ""
    while strOption != "X":
          #display the menu with choices
          print()
          print()
          print("-"*50)
          print("Encryption // Decryption Program")
          print("-"*50)
          print("="*50)
          print("1 - Encrypt a Message")
          print("2 - Decrypt a Message")
          print("="*50)
          print("X - Exit")
          print("-"*50)
        #Asks the user to input a message for Encryption/Decryption
          strOption = (input("Enter an option: ")).upper()

          #enter for encryption
          if strOption == "1":
              #encrypt the input
              userinputEn = (input("Enter a Message: ")).upper()
              newinputEn = ""
              i = 0
              #The lists being used to change and decipher the decryption//encryption
              De = ["1","R","5","G","Z","X","2","D","A","E","3","Y","U","I","W","6","7","O","V","8","F","9","L","0","J",".","H","Q","C","N","B","S","P","M","4","T","K"]
              En = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",".","1","2","3","4","5","6","7","8","9","0"]

              #Starting the encryption based on user input
              while i<len(userinputEn):
                  if userinputEn [i:i+1] in En:
                      myIndex=En.index(userinputEn[i:i+1])
                      newinputEn += De[myIndex]
                      .0
                                       
                  else:
                      newinputEn += userinputEn[i:i+1]

                  i+=1
            #print the encryption
              print()
              print("-"*50)
              print("Your message has been encrypted as: ", newinputEn)
              print("-"*50)
              print()


          elif strOption == "2":
                #similar to option 1 only we will decrypt the message
                userinputDe = input("Enter the Message: ").upper()#Encrypts the input message
                newinputDe = ""
                i = 0
                 
             #The lists being used to change and decipher the decryption//encryption again
                De = ["1","R","5","G","Z","X","2","D","A","E","3","Y","U","I","W","6","7","O","V","8","F","9","L","0","J",".","H","Q","C","N","B","S","P","M","4","T","K"]
                En = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",".","1","2","3","4","5","6","7","8","9","0"]

                 #Starting the decryption based on input
                while i<len(userinputDe):
                     if userinputDe [i:i+1] in De:
                         myIndex=De.index(userinputDe[i:i+1])
                         newinputDe += En[myIndex]

                     else:
                         userinputDe += newinputDe[i:i+1]

                     i+=1
                 #print the decryption
                print()
                print("-"*50)
                print("Your message has been decrypted as: ", newinputDe)
                print("-"*50)
                print()


          else:
                 #Restart the program
                 print()
                 print("="*50)
                 print("ERROR RESTARTING PROGRAM")
                 print("="*50)
                 print()

    #incorrect input display error        
except ValueError:
        print()
        print("="*50)
        print("ERROR RESTARTING PROGRAM")
        print("="*50)
        print()
        
finally: print()


main ()
    


                                       
                                       
                                    
              
              
              

