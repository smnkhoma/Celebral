from celebral_logic import *
from rich import print
import random

# The colours below will be used by rich to output coloured text
colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
chosen_color = random.choice(colors)




# main function continously loops until game is manually exited
def main():
    print(f"[{chosen_color}]This is a game called Celebral. Type in the answers to the mathematical problems, and hit ENTER. Hitting enter without attempting the question aborts the game. Be quick. Have fun, thats an order.[/{chosen_color}]")


    while True:

        input("Hit enter when ready to continue")
        play_game()
        chosen_color2 = random.choice(colors)
        print(f"[{chosen_color2}]That was fun. Lets do it again!/[{chosen_color2}]")


if __name__ == "__main__":
    main()
