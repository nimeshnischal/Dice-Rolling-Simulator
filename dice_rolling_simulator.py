#This is a basic python program to simulate the rolling of a dice

import nimesh_app_basics


def get_min_max_values(user_choice_default_dice_boolean):
    if not user_choice_default_dice_boolean:
        while True:
            print("Please enter the minimum and maximum values on the dice to simulate.")
            min_val = nimesh_app_basics.get_int_input("Minimum: ")
            max_val = nimesh_app_basics.get_int_input("Maximum: ")
            # Checking for valid entries
            if min_val >= max_val:
                print("Invalid entries, please try again!")
                continue
            else:
                break
    else:
        min_val = 1
        max_val= 6
    return [min_val, max_val]


def show_rolled_dice_value_and_loop(min_value, max_value):
    play_again_boolean = True
    while play_again_boolean:
        print("And the dice rolls....................")
        print("\nThe number is: ", nimesh_app_basics.get_random_int_in_range(min_value, max_value))     #TODO Draw ascii art for numbers (or use number images in GUI)
        play_again_boolean = nimesh_app_basics.get_valid_y_n_opinion("\nRoll again? ( y / n ): ")
        if not play_again_boolean:
          nimesh_app_basics.print_exit_message(app_name)
          break
        else:
          nimesh_app_basics.clear_screen()
          nimesh_app_basics.print_welcome_message(app_name)
          continue


#===================== MAIN PROGRAM =====================#
app_name = "Dice Rolling Simulator"

nimesh_app_basics.clear_screen()
nimesh_app_basics.print_welcome_message(app_name)

user_choice_default_dice_boolean = nimesh_app_basics.get_valid_y_n_opinion("Do you want to use the default 6-faced dice? ( y / n ): ")

nimesh_app_basics.clear_screen()
nimesh_app_basics.print_welcome_message(app_name)

min_max_values = get_min_max_values(user_choice_default_dice_boolean)
min_value = min_max_values[0]
max_value = min_max_values[1]

nimesh_app_basics.clear_screen()
nimesh_app_basics.print_welcome_message(app_name)

show_rolled_dice_value_and_loop(min_value, max_value)
