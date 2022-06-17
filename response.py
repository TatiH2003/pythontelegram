import random


def rock_paper(input_text):

    user_input = str(input_text).lower()

    options = ["/rock", "/paper", "/scissors"]

    while True:

        if user_input not in options:
            return " Error : Sorry, You have to select something from (rock/paper/scissors)."

        r = random.randint(0, 2)
        comp_input = options[r]

        if user_input == "/rock" and comp_input == "/scissors":

            return (
                f'Computer`s choice {comp_input}\n'
                f'You won.\n'
            )
        elif user_input == "/paper" and comp_input == "/rock":

            return (
                f'Computer`s choice {comp_input}\n'
                f'You won.\n'
            )

        elif user_input == "/scissors" and comp_input == "/paper":

            return (
                f'Computer`s choice {comp_input}\n'
                f'You won.\n'
            )

        elif user_input == comp_input:
            return (
                f'Computer`s choice {comp_input}\n'
                f'Ohhh!! It`s a tie.')

        else:

            return (
                f'Computer`s choice {comp_input}\n'
                f'You lost.'
            )
