# Import Section
from assets.name_generator_sections import NGS

# Initializes the NGS class into a usable form.
NGS = NGS()

banner = "===============================\n"\
         "= Hideo Kojima Name Generator =\n"\
         "===============================\n"
print(banner)

# This starts the questioning process and then returns a variable with all of the question+answer attributes.
player = NGS.section1()

# Uncomment this to see the pure dictionary of question variable names and provided answers.
#print(player.__dict__)

# This prints out the players kojiman_name attribute which is the final name the scripts generates.
print(f"Your Hideo Kojima name is:\n{player.kojima_name}")

