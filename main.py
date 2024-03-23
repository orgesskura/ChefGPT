from dotenv import load_dotenv

load_dotenv()

from OrgesChefGPT import ChefOrges


dish = ChefOrges.query("byrek")
print(dish)
