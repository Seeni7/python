number_1 = ''
number_2 = ''
calc_again = ''
operation = input('''
Please type in the math operation you would like to complete
+ for addition
- for subtraction
* for multiplication
/ for division
''')

def calculate():

 
    number_1 = int(input("Enter your first number: "))
    number_2 = int(input("enter your second number: "))

    


  

    
# Addition 
# 
    if operation == '+':
                 print('{} + {} = '.format(number_1, number_2))
                 print(number_1 + number_2)

        

# Subtraction
    elif operation == '-':
                 print('{} - {} = '.format(number_1, number_2))
                 print(number_1 - number_2)



# Multiplication
    elif operation == '*':
                 print('{} * {} = '.format(number_1, number_2))
                 print(number_1 * number_2)

# Define again() function to ask user if they want to use calculator again


# Division
    elif operation == '/':
                print('{} / {} = '.format(number_1, number_2))
                print(number_1 / number_2)

# Define again() function to ask user if they want to use calculator again



    def again():
    # Take input from user
        calc_again = input('''
        Do you want to calculate again?
        Please type Y for Yes or N for NO.
        ''')
    # If user types Y, run the calculate() function
        if  calc_again.upper() == "Y":
            calculate()

    # If user type N, say good-bye to the user and end the program
        else:  
            calc_again.upper() == 'N'
            print('See you later.') 
    again()
  
# If user types another key, run the function again

calculate()






                    
   









