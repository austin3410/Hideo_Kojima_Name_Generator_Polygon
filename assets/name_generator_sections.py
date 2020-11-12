# Import Section
import random
from pprint import pprint
import pickle
from datetime import datetime
import os

# Establishes the NGS class (Name Generator Sections)
# These sections and questions are pulled directly from Polygons Hideo Kojima Name Generator:
# https://www.scribd.com/document/434442769/Kojima-Name-Generator#fullscreen&from_embed
class NGS:

    # Section 1 decides how many names you have. I've decided to omit this for future implimenation reasons.
    def section1(self):
        
        self.section2()
        return self
    
    # Section 2 - Personal Information
    # Kojima’s characters have names that are directly related to their own character traits. This information will make sure your name fits your personality.
    def section2(self):
        self.full_name = input("What is your full name?\n: ")
        self.occupation = input("What do you do at your occupation?\n: ")
        self.occupation_verb = input("Condense the verb in your answer into a single -er noun. (e.g. if you are a sheep farmer, your answer will be 'farmer')\n: ")
        self.first_pet = input("What was your first pet's specifc species/breed? If you never had a pet, please answer with an animal you wish you owned.\n: ")
        self.embarrassing_memory = input("What's your most embarrassing childhood memory? Be specific.\n: ")
        self.embarrassing_memory_condensed = input("Condense this story into two words.\n: ")
        self.stabbing_object = input("What is the object you'd least like to be stabbed by?\n: ")
        self.good_at = input("What is something you are good at? (Verb ending in -ing)\n: ")
        self.max_carrots = input("How many carrots do you believe you could eat in one sitting, if someone, like, forced you to eat as many carrots as possible?\n: ")
        self.greatest_intangible_fear = input("What is your greatest intangible fear? (e.g. death, loneliness, fear itself)\n: ")
        self.greatest_tangible_fear = input("What is your greatest tangible fear? (e.g. horses)\n: ")
        self.last_action = input("What is the last thing you did before starting this worksheet?\n: ")
        self.current_condition = input("What condition is your body currently in? (Single word answer)\n: ")
        self.favorite_matter = input("Favorite state of matter?\n: ")
        self.name_sound_alike = input("A word your name kinda of sounds like? (e.g. Brian -> Brain)\n: ")
        self.zodiac_sign = input("What is your Zodiac sign?\n: ")
        self.one_word_personality = input("If you had to define your personality in one word, what would it be?\n: ")

        self.section3()
    
    # Section 3 - Kojima Information
    # Kojima character names reflect his own idiosyncrasies. He can't help himself.
    def section3(self):
        self.favorite_film_character = input("Who is your favorite film character?\n: ")
        self.favorite_film_character_action = input("What is something you'd enjoy watching that character do?\n: ")
        self.favorite_film_character_action_word = input("Please condense that into one word.\n: ")
        self.favorite_last_film_word = input("What is the last word of the title of your favorite film?\n: ")
        self.favorite_album_word = input("What is the first word in the title of your favorite album?\n: ")
        self.scientific_term = input("What is a scientific term you picked up from listening to, or watching educational media?\n: ")
        self.military_hardware = input("What is a piece of military hardware you think looks cool even though war is bad?\n: ")

        self.section4()
    
    # Section 4 - Determining Your Name Conditions
    # Sometimes, a character will have a plot-based condition that affects their name. You, too, might have a condition that affects your name.
    # Conditions can stack, so please make note of how many your name has.
    def section4(self):
        input("Press ENTER to roll for the 'THE -MAN CONDITION':")
        roll = random.randint(1, 4)
        if roll == 4:
            print("You rolled a 4 and have the -MAN CONDITION!\nYour last name will include the suffix -man!")
            self.man_condition = True
        else:
            print(f"You rolled a {roll}, which means you do not have the -MAN CONDITION!")
            self.man_condition = False
        
        input("Press ENTER to roll for the 'THE CONDITION CONDITION':")
        roll = random.randint(1, 8)
        if roll <= 5:
            print(f"You rolled a {roll}, which means you do not have the CONDITION CONDITION!")
            self.condition_condition = None
        elif roll == 6:
            print(f"You rolled a {roll}, which means you're big. Your name must have 'Big' at the beginning of it.")
            self.condition_condition = "Big"
        elif roll == 7:
            print(f"You rolled a {roll}, which means you are older than you once were. Your name must have 'Old' at the beginning of it.")
            self.condition_condition = "Old"
        else:
            print(f"You rolled a {roll}, which means you are how you currently are. Your name will have '{self.current_condition}' at the beginning of it.")
            self.condition_condition = self.current_condition

        input("Press ENTER to roll for the 'THE KOJIMA CONDITION':")
        roll = random.randint(1, 100)
        if roll == 69:
            print("Oh no. You rolled a 69 which means you are Hideo Kojima. Hideo Kojima created you and is also you. "\
            "You are the man who created himself and there is nothing you can do about it. You're in Kojima's world-your world-and that's just the breaks, pal."\
            " Your worksheet ends here. You're Hideo Kojima. Go do the things that Hideo Kojima does.")
            self.hideo_kojima = True
            self.kojima_name = "Hideo Kojima"
            quit()
        else:
            print(f"You rolled a {roll}, which means, no, you're not Hideo Kojiman. That's OK though. We're all special in our own way. "\
            "Not as special as Hideo Kojima but hey, we can't all be super heros.")
            self.hideo_kojima = False
        
        self.section5()
    
    # Section 5 - Determining Your Name Category
    # Kojima names fall into a finite number of categories. This section will determine the category if which your name belongs.
    def section5(self):
        input("Press ENTER to roll to determine your name category:")
        roll = random.randint(1, 20)
        if roll == 1:
            print(f"You rolled a {roll}, which means you have a normal name.")
            self.section6()
        elif roll > 1 and roll < 7:
            print(f"You rolled a {roll}, which means you have an occupational name.")
            self.section7()
        elif roll > 6 and roll < 11:
            print(f"You rolled a {roll}, which means you have a horny name.")
            self.section8()
        elif roll > 10 and roll < 14:
            print(f"You rolled a {roll}, which means you have a The name.")
            self.section9()
        elif roll > 13 and roll < 18:
            print(f"You rolled a {roll}, which means you have a cool name.")
            self.section10()
        elif roll > 17 and roll < 20:
            print(f"You rolled a {roll}, which means you have a violent name.")
            self.section11()
        elif roll == 20:
            print(f"You rolled a {roll}, which means you have a name that lacks subtext.")
            self.section12()
        else:
            print("Something went wrong SECTION5!!")

    # Section 6 - NORMAL NAME
    # Kojima's early work includes lots of characters that have names that are widely considered to be "normal". Was this just because, in the early years,
    # he didn't have the power to say, "I'm Hideo Kojima, I can name someone Die-Hardman if I want to" without people questioning him? Probably.    
    def section6(self):
        self.kojima_name = self.full_name
        self.add_section4_conditions()
    
    # Section 7 - OCCUPATIONAL NAME
    # Kojima's characters tend to be driven by the work that they do. That often carries over to their names. You, too, can be nothing more than your job.
    def section7(self):
        input("Press ENTER to roll for your first name:")
        roll = random.randint(1, 4)
        if roll == 1:
            self.kojima_name = self.one_word_personality
        elif roll == 2:
            self.kojima_name = self.good_at
        elif roll == 3:
            self.kojima_name = self.name_sound_alike
        else:
            self.kojima_name = self.favorite_film_character


        self.kojima_name = f"{self.kojima_name} {self.occupation_verb}"

        self.add_section4_conditions()
    
    # Section 8 - HORNY NAME
    # Kojima's characters and stories are irrevocably horny. Weirdly horny, sure, but horny nontheless.
    def section8(self):
        input("Press ENTER to roll for your first name:")
        roll = random.randint(1, 4)
        if roll == 1:
            self.kojima_name = self.favorite_matter
        elif roll == 2:
            self.kojima_name = "Naked"
        elif roll == 3:
            self.kojima_name = self.good_at
        else:
            self.kojima_name = self.zodiac_sign
        
        
        x = input("Would you like your middle name to be 'Lickable'?\nY/N: ")
        if x.upper() == "Y" or x.upper() == "YES":
            self.kojima_name = f"{self.kojima_name} Lickable"
        
        self.kojima_name = f"{self.kojima_name} {self.first_pet}"

        self.add_section4_conditions()
    
    # Section 9 - THE NAME
    # Kojima loves to make people have names that start with the word "The" and they usually symbolize fear or unstoppable forces. 
    # You are now that unstoppable force.
    def section9(self):
        input("Press ENTER to roll for your last name:")
        roll = random.randint(1, 4)
        if roll == 1:
            self.kojima_name = self.greatest_intangible_fear
        elif roll == 2:
            self.kojima_name = self.greatest_tangible_fear
        elif roll == 3:
            self.kojima_name = self.embarrassing_memory_condensed
        else:
            self.kojima_name = self.military_hardware
        
        self.kojima_name = f"The {self.kojima_name}"

        self.add_section4_conditions()
    
    # Section 10 - COOL NAME
    # Kojima loves to be cool. Sometimes, his idea of cool is a bit strange, but it is always cool to Hideo Kojima, and that's what matters.
    def section10(self):
        input("Press ENTER to roll for your last name:")
        roll = random.randint(1, 6)
        if roll == 1:
            self.kojima_name = self.favorite_last_film_word
        elif roll == 2:
            self.kojima_name = self.favorite_album_word
        elif roll == 3:
            self.kojima_name = self.scientific_term
        elif roll == 4:
            self.kojima_name = self.good_at
        elif roll == 5:
            self.kojima_name = self.greatest_intangible_fear
        else:
            self.kojima_name = self.name_sound_alike
        

        self.kojima_name = f"{self.favorite_film_character_action_word} {self.kojima_name}"

        self.add_section4_conditions()
    
    # Section 11 - VIOLENT NAMES
    # Sometimes, a Kojima name can be very threatening and violent, like Sniper Wolf, or The Fury. Now you can also be threatening and violent.
    def section11(self):
        input("Press ENTER to roll for your last name:")
        roll = random.randint(1, 4)
        if roll == 1:
            self.kojima_name = self.scientific_term
        elif roll == 2:
            self.kojima_name = self.favorite_matter
        elif roll == 3:
            self.kojima_name = self.military_hardware
        elif roll == 4:
            self.kojima_name = self.greatest_tangible_fear
        
        self.kojima_name = f"{self.stabbing_object} {self.kojima_name}"
        
        self.save_name()
    
    # Section 12 - NAME THAT LACKS SUBTEXT
    # Sometimes, Kojima gives up and just names a character exactly what they are. Congratulations. You are exactly what you do.
    def section12(self):
        self.kojima_name = self.last_action

        self.add_section4_conditions()

    # This section adds up all of the conditions your names has and creates the perfect Hideo Kojima name just for you.
    def add_section4_conditions(self):
        
        if self.man_condition == True:
            self.kojima_name = f"{self.kojima_name}-man"
        
        if self.condition_condition != None:
            if self.kojima_name.startswith("The "):
                self.kojima_name = self.kojima_name.replace("The ", "")
                self.kojima_name = f"{self.condition_condition} {self.kojima_name}"
                self.kojima_name = f"The {self.kojima_name}"
            else:
                self.kojima_name = f"{self.condition_condition} {self.kojima_name}"
        
        self.save_name()
    
    # This section saves and holds your answers for future reference... or ransom.
    # This section is necessary for future additions to this code.
    def save_name(self):
        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y_%H_%M_%S")
        player = self.__dict__
        while True:
            if os.path.exists("saves"):
                with open(f"saves//{self.full_name}_{date_time}.pickle", "wb") as file:
                    pickle.dump(player, file)
                break
            else:
                os.makedirs("saves")
        

        