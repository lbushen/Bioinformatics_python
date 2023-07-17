'''
Write a function that keeps prompting for a filename 
until a valid file is entered by the user (print out "file found, 
   thanks") or until five attempts have failed (print out "you did not 
   enter a valid file name"). Call the function from the main part of 
   your program. The function in this case does not return any value. 
   Show the entire program (not just the function).

Nadim.

Hint: You will need to use the os module here, 
to make sure the file exists. Refer back to week 3. 
'''
import os

def filefound():
    count = 0
    while count < 5:
        
        filename = input("Please enter a filename: ")
        x = "File found, thanks."
        found = False
        
        if filename in os.listdir("."):
            found = True
            print(x)
            break
        else:
            count += 1
    if found == False:
        print("\nYou did not enter a valid filename.")       
                
  
filefound()

