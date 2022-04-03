import time

weapon = []


def print_prompt(message):
    """Printing greeting message"""
    print(message)
    time.sleep(1)


def great_message():
    """Great user on first attempt"""
    print_prompt(
        "You find yourself in an open field, filled with grass and yellow wildflowers.")
    print_prompt(
        "Rumor has it that a prirate is somewhere around here, and has been terrifying the nearby village.")
    print_prompt("In front of you is a house.")
    print_prompt("To your right is a dark cave.")
    print_prompt(
        "In your hand you hold your trusty (but not very effective) dagger.")
    print_prompt("Enter 1 to knock on the door of the house.")
    print_prompt("Enter 2 to peer into the cave.")
    print_prompt("What would you like to do?")
    print_prompt("(Please enter 1 or 2.)")


def house():
    """Enter house logic function"""
    print("You approach the door of the house")
    time.sleep(1)
    print("You are about to know when the door opens and out steps a pirate.")
    time.sleep(1)
    print("The pirate attack you!")
    time.sleep(1)
    print('You feel a bit under-prepared for this, what with only having a tiny dagger.')
    time.sleep(1)
    print("Would you like to (1) fight or (2) run away?")

    try:
        response = int(input("1 or 2 : "))
    except ValueError:
        print_prompt("You enter wrong input")

    if response == 1:
        print_prompt("You do your best...")
        time.sleep(1)
        if weapon:
            print_prompt(
                "As troll moves to attack, you unsheat your new sword.")
            print_prompt(
                "The sword of ogoroth shines brightly in your hand as you brace yourself for the attack.")
            print_prompt(
                "But the troll takes one look at your shiny new toy and runs away")
            print_prompt(
                "You have the rid the town of the troll. You are victorious")
        else:
            print_prompt("but your dagger is no match for the pirate.")
            print_prompt("You have been defeated!")

        print_prompt("Would you like to play again?")
        quit = input("n/y : ")
        if quit.lower() == "y":
            print_prompt("starting over again")
            decide()
        elif quit.lower() == 'n':
            print_prompt("Thanks for playing! See you next time.")
        else:
            print_prompt("Enter either n or y as input.")

    elif response == 2:
        print_prompt(
            "You run back into the field. You don't seem to have been followed.")
        print_prompt("Enter 1 to knock on the door of the house.")
        print_prompt("Enter 2 to peer into the cave.")
        print_prompt("What would you like to do?")
        decide()
    else:
        print_prompt("Enter proper input. Either 1 0r 2")
        decide()


def cave():
    """Enter cave logic function"""
    if not weapon:
        print_prompt("You peer cautiously into the cave")
        print_prompt("It turns out to be only a very small cave")
        print_prompt("Your eye catches a glint of metal behind a rock.")
        print_prompt("You have found the magical sword of Ogoroth")

        weapon.append('sword')
        print_prompt(
            "You discard your silly old dagger and take the sword with you.")
        print_prompt("You walk back to the filed")
        decide()
    else:
        print_prompt(
            "You have been here before, and gotten all the good stuff. It's just a empty cave now.")
        print_prompt("You walk back to the filed")
        print('\n')
        print_prompt("Enter 2 to peer into the cave.")
        print_prompt("What would you like to do?")
        decide()


def decide():
    response = int(input("1 or 2 : "))
    if response == 1:
        house()
    elif response == 2:
        cave()


def start_game():
    """Start the game"""
    great_message()
    decide()


start_game()
