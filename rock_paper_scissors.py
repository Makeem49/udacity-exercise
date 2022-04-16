#!/usr/bin/env python3

import random
import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def print_prompt(message, delay=0):
    """
    Printing greeting message
    :param message: string
    :param delay: integer
    :return: None
    """
    print(message)
    time.sleep(delay)


def validate_input(message, options):
    """
    input validation
    :param prompt: string
    :param options: of of string
    :return: string
    """
    while True:
        option = input(message)
        if option in options:
            return option
        print_prompt(f'Sorry, the option "{option}" is invalid. Try again!')
        print_prompt(f'Only these ---> {options} are valid input')


def win_message(player, delay=1):
    """
    Function displaying win message
    :param player: string
    :param delay: int
    :return : None
    """
    print(f"** PLAYER {player} WINS ** ")
    time.sleep(delay)


def tie_message(delay=1):
    """
    Function displaying tie message
    :param delay: int
    :return : None
    """
    print(f"** TIE ** ")
    time.sleep(delay)


class Player:

    def __init__(self) -> None:
        super().__init__()
        self.score = 0

    def move(self):
        return NotImplementedError("Method can only be implemeted\
            through subclass")

    def learn(self, my_move, their_move):
        return NotImplementedError("Method can only be implemeted \
            through subclass")


class CyclePlayer(Player):
    """CyclePlayer class"""

    def __init__(self) -> None:
        super().__init__()
        self.name = 'CyclePlayer Player'
        self.your_move = []
        self.opponent_move = []

    def move(self):
        total_move = len(self.your_move)
        move = random.choice(moves)
        if total_move == 0:
            self.your_move.append(move)
            return move
        if move in self.your_move:
            self.move()
        else:
            self.your_move.append(move)
            return move
        return move

    def learn(self, my_move, opponent_move):
        self.opponent_move.append(opponent_move)
        # self.your_move.append(my_move)
        for i in range(len(self.opponent_move)):
            self.opponent_move[i]
            # self.your_move[i]

        if len(self.opponent_move) == 1:
            print(f"Opponent past move is {' - '.join(self.opponent_move)}")
            print(f"Your past move is {' - '.join(self.your_move)}")
        else:
            print(f"Opponent past move are {' - '.join(self.opponent_move)}")
            print(f"Your past move are {' - '.join(self.your_move)}")

    def __str__(self) -> str:
        return f"{self.name} created."


class ReflectPlayer(Player):
    """Reflect player class"""

    def __init__(self):
        super().__init__()
        self.name = 'Reflect Player'
        self.your_move = []
        self.opponent_move = []

    def move(self):
        total_move = len(self.opponent_move)
        if total_move == 0:
            return random.choice(moves)
        elif total_move == 1:
            return self.opponent_move[0]
        else:
            return self.opponent_move[1]

    def learn(self, my_move, opponent_move):
        self.opponent_move.append(opponent_move)
        self.your_move.append(my_move)
        for i in range(len(self.your_move)):
            self.opponent_move[i]
            self.your_move[i]

        if len(self.opponent_move) == 1:
            print(f"Opponent past move is {' - '.join(self.opponent_move)}")
            print(f"Your past move is {' - '.join(self.your_move)}")
        else:
            print(f"Opponent past move are {' - '.join(self.opponent_move)}")
            print(f"Your past move are {' - '.join(self.your_move)}")

    def __str__(self) -> str:
        return f"{self.name} created."


class Computer(Player):
    """Computer player blueprint"""

    def __init__(self) -> None:
        super().__init__()
        self.name = 'Computer'
        self.your_move = []
        self.opponent_move = []

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, opponent_move):
        self.opponent_move.append(opponent_move)
        self.your_move.append(my_move)
        for i in range(len(self.your_move)):
            self.opponent_move[i]
            self.your_move[i]

    def __str__(self) -> str:
        return f"{self.name} created."


class HumanPlayer(Player):
    """Human player blueprint"""

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.your_move = []
        self.opponent_move = []

    def move(self):
        next_move = validate_input("What is your next move?", moves)
        return next_move

    def learn(self, my_move, opponent_move):
        self.opponent_move.append(opponent_move)
        self.your_move.append(my_move)
        lenght = len(self.your_move)
        for i in range(lenght):
            self.opponent_move[i]
            self.your_move[i]

        if len(self.opponent_move) == 1:
            print(f"Opponent past move is {' - '.join(self.opponent_move)}")
            print(f"Your past move is {' - '.join(self.your_move)}")
        else:
            print(f"Opponent past move are {' - '.join(self.opponent_move)}")
            print(f"Your past move are {' - '.join(self.your_move)}")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        self.reward(move1, move2)

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def reward(self, move1, move2):
        if move1 == move2:
            # If two moves are equal, we don't need to call beats method.
            tie_message()
        elif beats(move2, move1):  # If beats return true- Player one won
            self.p2.score += 1
            win_message(self.p2.name)
        elif beats(move1, move2):  # If beats return False- Player one won
            self.p1.score += 1
            win_message(self.p1.name)

    def play_game(self):
        print("Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        determine_score(self.p1, self.p2)
        print("Game over!")

    @classmethod
    def play_again(cls, player1, player2):
        """Alternative contructor"""
        new_game = cls(player1, player2)
        new_game.play_game()


def determine_score(player1, player2):
    """
    function to determine who win the game
    :param player1: instance
    :param player2: instance
    :return: None
    """
    print(player1.score)
    print(player2.score)
    if player1.score > player2.score:
        win_message(player1.name)
    elif player1.score < player2.score:
        win_message(player2.name)
    else:
        tie_message()


def start_game():
    """Function that start the game"""
    player1 = HumanPlayer("Human")
    player2 = CyclePlayer()
    game = Game(player1, player2)
    game.play_game()
    determine_score(player1, player2)


if __name__ == '__main__':
    start_game()
    response = validate_input("Will you like to play again?", ['y', 'n'])
    while response == 'y':
        start_game()
        response = validate_input("Will you like to play again?", ['y', 'n'])
    else:
        print_prompt('Thanks for playing rock, paper, scissors... Bye.')
