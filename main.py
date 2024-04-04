from dotenv import load_dotenv
import sys

load_dotenv()

from OrgesChefGPT import ChefOrges
from RGRChef import RGRChef
from AngryChef import AngryChef

chefs = [ChefOrges, RGRChef, AngryChef]
found_chef = False
while not found_chef:
    user_input = input("\n Please type of chef you would want advice from : \n")
    for chef_class in chefs:
        if user_input.lower() == chef_class.name.lower():
            print("Found the chef.")
            found_chef = True
            WHATCHEF = chef_class  # Instantiate the chef
            break
    else:
        print("Typed chef is currently unavailable!")

while True:
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        user_input = input(
            "\n Type the name of the dish, a set of ingredients, or a recipe for a dish:\n"
        )

    WHATCHEF.query(user_input)
