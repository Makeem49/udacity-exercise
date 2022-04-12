import time
import string
import random

weapon = []


def typewriter_simulator(message):
    """
    Typewriter simulaator function
    :param message: string
    :return : None
    """
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')


def print_prompt(message, delay=0):
    """
    Printing greeting message
    :param message: string
    :param delay: integer
    :return: None
    """
    typewriter_simulator(message)
    time.sleep(delay)


def great_message():
    """Great user on first attempt"""
    print_prompt(
        "You find yourself in an open field,"
        "filled with grass and yellow wildflowers.")
    print_prompt(
        "Rumor has it that a prirate is somewhere around here,"
        "and has been terrifying the nearby village.")
    print_prompt("In front of you is a house.")
    print_prompt("To your right is a dark cave.")
    print_prompt(
        "In your hand you hold your trusty (but not very effective) dagger.")
    print_prompt("Enter 1 to knock on the door of the house.")
    print_prompt("Enter 2 to peer into the cave.")
    print_prompt("What would you like to do?")
    print_prompt("(Please enter 1 or 2.)")


def validating_input(prompt, options):
    """
    input validation
    :param prompt: string
    :param options: of of string
    :return: string
    """
    while True:
        option = input(prompt)
        if option in options:
            return option
        print_prompt(f'Sorry, the option "{option}" is invalid. Try again!')
        print_prompt(f'Only these ---> {options} are valid input')


def house():
    """Enter house logic function"""
    print_prompt("You approach the door of the house", delay=1)
    print_prompt("You are about to know when the door"
                 "opens and out steps a pirate.", delay=1)
    print_prompt("The pirate attack you!", delay=1)
    print_prompt("You feel a bit under-prepared for this,"
                 "what with only having a tiny dagger.", delay=1)
    print_prompt("Would you like to (1) fight or (2) run away?", delay=1)

    response = validating_input('Enter 1 or 2:', ['1', '2'])

    if int(response) == 1:
        print_prompt("You do your best...")
        if weapon:
            print_prompt(
                f"As troll moves to attack, you unsheat your new weapon.")
            print_prompt(
                "The weapon of ogoroth shines brightly in your hand"
                "as you brace yourself for the attack.")
            print_prompt(
                "But the troll takes one look at your shiny \
                                new toy and runs away")
            print_prompt(
                "You have the rid the town of the troll. You are victorious")
        else:
            print_prompt("but your dagger is no match for the pirate.")
            print_prompt("You have been defeated!")

        print_prompt("Would you like to play again?")
        quit = validating_input("Enter y or n : ", ['y', 'n'])
        if quit.lower() == "y":
            print_prompt("starting over again")
            start_game()
        elif quit.lower() == 'n':
            print_prompt("Thanks for playing! See you next time.")

    elif int(response) == 2:
        print_prompt(
            "You run back into the field. You don't \
                                seem to have been followed.")
        print_prompt("Enter 1 to knock on the door of the house.")
        print_prompt("Enter 2 to peer into the cave.")
        print_prompt("What would you like to do?")
        decide()


def choose_weapon():
    """Funtion to give weapon to the user"""
    weapon = random.choice(['cutlass', 'gun', 'granade', 'rocket launcher'])
    return weapon


def cave():
    """Enter cave logic function"""
    if not weapon:
        print_prompt("You peer cautiously into the cave")
        print_prompt("It turns out to be only a very small cave")
        print_prompt("Your eye catches a glint of metal behind a rock.")
        print_prompt("You have found the magical weapon of Ogoroth")

        weapon.append(choose_weapon())
        print_prompt(
            f"You discard your silly old dagger and \
                take the {weapon[0]} with you.")
        print_prompt("You walk back to the filed")
        decide()
    else:
        print_prompt(
            "You have been here before, and gotten all the good stuff."
            "It's just a empty cave now.")
        print_prompt("You walk back to the filed")
        print_prompt('\n')
        print_prompt("Enter 1 to knock on the door of the house.")
        print_prompt("Enter 2 to peer into the cave.")
        print_prompt("What would you like to do?")
        decide()


def decide():
    response = validating_input("Enter 1 or 2", ['1', '2'])
    if int(response) == 1:
        house()
    elif int(response) == 2:
        cave()


def start_game():
    """Start the game"""
    great_message()
    decide()


if __name__ == "__main__":
    start_game()
