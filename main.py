from dotenv import load_dotenv
import sys

load_dotenv()

from OrgesChefGPT import ChefOrges

chefs = [ChefOrges]
found_chef = False
while not found_chef:
    user_input = input("\n Please type of chef you would want advice from : \n")
    if user_input.lower() in [chef.name for chef in chefs]:
        print("Found the chef.")
        found_chef = True
    else:
        print("Typed chef is currently unavailable!")


while True:
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        user_input = input(
            "\n Type the name of the dish, a set of ingredients, or a recipe for a dish:\n"
        )

    ChefOrges.query(user_input)
