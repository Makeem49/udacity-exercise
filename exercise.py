import time
items = []


def print_prompt(prompt_message):
    """ Print welcome message"""
    print(prompt_message)
    time.sleep(1)


def welcome_prompt():
    """Welcome message function"""
    print_prompt("You have just arrived at your new job!")
    print_prompt("You are in the elevator.")
    print_prompt(
        "Please enter the number for the floor you would like to visit:")


def pick_id():
    """Pick id from clerk"""
    if "ID" in items:
        print_prompt(
            "The clerk greets you, but she has already given you your ID card, so there is nothing more to do here now.")
    elif "ID" not in items:
        items.append("ID")
        print_prompt("The clerk greets you and gives you your ID card.")

    return items


def pick_handbook():
    """Pick handbook"""
    if "Handbook" in items:
        print_prompt(
            "The HR folks are busy at their desks. There doesn't seem to be much to do here.")
    elif "ID" in items:
        items.append("Handbook")
        print_prompt("HR give you handbook")
    else:
        print_prompt(
            "I can't give you any handbook with having your ID. You will have to get your ID first from the first floor")

    return items


def get_job():
    """User get to his job if ID and Handbook is available"""
    if "ID" in items and not "Handbook" in items:
        print_prompt(
            "Hi Bob, you need to have your Hnadbook before you can star your job")
    elif "ID" in items and "Handbook" in items:
        print_prompt("You can now start you job.")
    else:
        print_prompt(
            "You need to have you ID and Handbook before you can start job here.")


def get_items(choice):
    """Check all the items the user has"""
    if choice == 1:
        pick_id()
    elif choice == 2:
        pick_handbook()
    elif choice == 3:
        get_job()


def floor_list():
    return ["Lobby", "Human Resources", "Engineering department"]


def display_floor():
    """Wil only display floor to choose"""
    index = 1
    floors = floor_list()

    for floor in floors:
        print(f"{index}. {floor}")
        index += 1
    return floors


def is_choice_int():
    """ Confirming user input """
    try:
        choice = int(input("Floor number."))
        if choice:
            return choice
    except ValueError:
        print_prompt("Your choice must be an integer")


def level(choice):
    """This will be responsible for the level the user choose"""
    floors = floor_list()

    if choice not in [1, 2, 3]:
        print('You can only pick 1 or 2 or 3')
        choose_floor()
    elif choice in [1, 2, 3]:
        print_prompt(f"You push the button for the {floors[choice -1]}")
        print_prompt(
            f'After a few moments, you find yourself in the {floors[choice - 1]}')
        get_items(choice)
        print_prompt('Where will you like to go next?')
        choose_floor()


def choose_floor():
    """This will help the user choose a particular follor"""
    floors = display_floor()
    choice = is_choice_int()
    level(choice)


def elevator():
    """Function for calling elevator"""
    welcome_prompt()
    choose_floor()


elevator()
