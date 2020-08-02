#Author: Alec Blyth
#Date: 13/01/2016
#Description: Customer Login Task

#This is sequence file operation, this opens and reads data on a text file. 
text_file = open("customers.txt", "r") #This reads the file and stores the information as an array
UserList = text_file.readlines()

def CustomerTextFile(UserList): #This is user-defined function sets the text file with parameter passing  
    length = len(UserList)

    CustomerNum = str(input("Enter in your customer number: ")) #This asks the user to input their customer number

    count = 0
    searchValue = CustomerNum + '\n' #In order for the program search properly, added a \n 

    for i in range(0, length): #This pseduocode sets the search value to the user's input and counts how many times the input has appeared in the list 
        if UserList[i] == searchValue: 
            count += 1
    if count >= 1:
        print("You have logged in " + str(count) + " times") #If user inputted number is found this will be printed 
    else:
        print("You have entered an invalid customer number.") #Otherwise this will be displayed and end the program `
    text_file.close() #This closes the text file and ends the program 

CustomerTextFile(UserList) #This ends the function
