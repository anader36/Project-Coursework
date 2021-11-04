#Psuedorandom Number Generator using LCG and taking the seed stored inside the text file

from time import sleep
import sys

string = "Welcome to my True Random Number Generator using the system's time \n This project is done by Ahmed Nader \n  Hope you'll like it and have a good day \n   :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) \n" # Whatever string you want

for letter in string:
  sleep(0.05) # In seconds
  sys.stdout.write(letter)
  sys.stdout.flush()

#The above function is used to create the so called "python typing effect" as you've seen in the above example 

input("Please Press 'Enter' to start the program:\n")

#Variable for requesting the user to press 'Enter' in order to run the program

#Function used to get the number from a text file and storing it
with open('number.txt') as f:
    contents = int(f.read())
num = contents
#Calling the 'contents' variable as 'num' to make it easier for the user to understand 
print("Seed stored inside the file is : ", contents )
     
#Setting the values for each variable
a = 134775813
#A is the multiplier
c = 1
#C is the increment 
m = 2**32
#M is the modulus

#Defining a function which calculates the random number using linear congruential generator 
def lcg(num):
    num = ((a*num)+c)%m 
    return num

values= ""
#Stores the output number as a string 

for i in range(1,35):   
#For loop to print out the list of numbers  
    values += str(lcg(num))+ " "
#Storing the number printed as a string and making the results on one line   
    num = lcg(num)
    
print("LCG Results: ")    
print(values)
#Calling the function to print
        