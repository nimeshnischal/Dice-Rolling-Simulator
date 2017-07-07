#This is a basic python program to simulate the rolling of a dice

import random
import os   

def clear_screen():                     #Function to clear the console screen
    clear = lambda:os.system('cls')
    clear()

def print_welcome_message():
    print("\n********** Welcome to Dice Rolling Simulator **********\n")

def get_user_choice():
    user_choice = None
    while user_choice not in user_choice_options:   #Run the loop unless a valid user's choice is received
        user_choice = input()
        if user_choice not in user_choice_options:
            print("Wrong input, please try again! (y/n):")
            continue
        return user_choice

def ask_user_for_default_choice():
    print("Do you want to use the default 6-faced dice? (y/n)")
    return get_user_choice()

def get_min_max_values():
    if user_choice in user_choice_no_options:
        while True:
            print("Please enter the minimum and maximum values on the dice to simulate.")
            min_value = int(input("Minimum value: "))       #TODO create a function to check if input is int or not
            max_value = int(input("Maximum value: "))
            if min_value >= max_value:          			#Checking for valid entries
                print("Invalid entries, please try again!")
                continue
            else:
                break
    else:
        min_value = 1
        max_value = 6
    return [min_value, max_value]

def get_random_number(min, max):        #Function to generate a random number between two numbers, including those two numbers
    return random.randint(min,max)

def show_exit_message():
    print("\n==================== Thank you for using this app. Developed by Nimesh Nischal. ====================")

def show_rolled_dice_value_and_loop(min_value, max_value):
    user_choice = 'y'
    while user_choice not in user_choice_no_options:
        print("And the dice rolls....................")
        print("\nThe number is: ", get_random_number(min_value, max_value))     #TODO Draw ascii art for numbers (or use number images)
        print("\nRoll again? (y/n)")
        user_choice = get_user_choice()
        if user_choice in user_choice_no_options:
          show_exit_message()
          break
        else:
          clear_screen()
          print_welcome_message()
          continue


#=====================MAIN PROGRAM=====================#

user_choice_options = ['y', 'n', 'Y', 'N','yes', 'no', 'Yes', 'No', 'YES', 'NO']    #Taking most of the possible user inputs in cosideration
user_choice_no_options = ['n', 'N', 'no', 'No', 'NO']                               #Uptil now, no need to defice user_choice_yes_options

clear_screen()
print_welcome_message()

user_choice = ask_user_for_default_choice()

clear_screen()
print_welcome_message()

min_max_values = get_min_max_values()
min_value = min_max_values[0]
max_value = min_max_values[1]

clear_screen()
print_welcome_message()

show_rolled_dice_value_and_loop(min_value, max_value)

#clear_screen()
