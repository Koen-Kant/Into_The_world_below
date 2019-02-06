import random
from DM import DM
from Artist import Artist
from journey import Land
from inventory import Inventory


class Hero:

    class_list = {"Barbarian": "Rage",
                  "Bard": "Music",
                  "Cleric": "Turn Undead",
                  "Druid": "Shapechange",
                  "Fighter": "Second wind",
                  "Monk": "Flurry of Blows",
                  "Paladin": "Divine Smite",
                  "Ranger": "Tracker",
                  "Rogue": "Sneak Attack",
                  "Sorcerer": "Innate Magic",
                  "Warlock": "Patron",
                  "Wizard": "Sea of Knowledge"}

    def __init__(self):
        self.name = ""
        self.p_race = ""
        self.p_class = ""
        self.max_hp = 10
        self.current_hp = 10
        self.base_attack = 1
        self.base_defence = 1
        self.c_ability = "None"
        self.inventory = Inventory(self)
        self.world_view = Artist(20)
        self._DM = DM(party=self, vision=self.world_view)
        self.quest = Land(traveler=self, artist=self.world_view)

    def get_stats(self):
        return {"Name": self.name[:10],
                "cHP": self.current_hp,
                "mHP": self.max_hp,
                "Class": self.p_class[:10],
                "Race": self.p_race[:10]}

    def the_adventure_begins(self):
        place = self.quest.first_location()
        self.arrive_at_location(place.get_location())
        return place.encounter_loc()

    def the_grand_final(self):
        place = self.quest.final_location()
        self.arrive_at_location(place.get_location())
        return place.encounter_loc()

    def end_game(self):
        self.world_view.kill_music()
        self.world_view.end_clear()

    def rest(self):
        self.arrive_at_location("camp")
        self.world_view.full_line()
        self.world_view.print_line(text="{N} Rested and Healed their wounds".format(N=self.name))
        self.world_view.full_line()
        self.world_view.wait_prompt()
        self._DM.advance_time()
        self.world_view.wait_prompt()
        # heal
        # prepare

    def go_to_town(self):
        self.arrive_at_location("city")
        self.world_view.full_line()
        self.world_view.print_line(text="{N} went to town".format(N=self.name))
        self.world_view.full_line()
        self.world_view.wait_prompt()
        self._DM.advance_time()
        self.world_view.wait_prompt()
        # find town
        # et_town actions

    def venture(self):
        place = self.quest.get_new_location()
        self.arrive_at_location(place.get_location())
        place.encounter_loc()
        self.world_view.full_line()
        self.world_view.wait_prompt()
        self.world_view.clear_screen()
        self._DM.advance_time()
        self.world_view.wait_prompt()

    def retire(self, reason):
        self.world_view.full_line()
        self.world_view.print_line(text=self.name + " " + reason)
        self.world_view.full_line()
        self.world_view.wait_prompt()
        self.end_game()
        # retire with reason && end_game

    def victory(self):
        self._DM.describe("end")
        self.world_view.print_line(text="With the Evil Wizard slain, the land is free once more!")
        self.world_view.print_line(text="Congratulations hero, you made a difference")
        self.world_view.print_line(text="Your reward lies below the puple star")
        self.world_view.wait_prompt()

    def defeat(self):
        self._DM.describe("end")
        self.world_view.print_line(text="As you feel your life fading, you know you have failed!")
        self.world_view.wait_prompt()

    def arrive_at_location(self, location):#, encounter):
        self._DM.describe(location)
        self._DM.print_player_stats()

    def roll_dice(self, visible=False, dice_size=None):
        self.world_view.prompt("$:[Roll a {}]".format(dice_size or "d100"))
        if dice_size == "d4":
            max_val= 4
        elif dice_size == "d6":
            max_val = 6
        elif dice_size == "d8":
            max_val = 8
        elif dice_size == "d10":
            max_val = 10
        elif dice_size == "d12":
            max_val = 12
        else:
            max_val = 100
        out = random.randint(1, max_val)
        if visible:
            self.world_view.print_line(text="You rolled a {} on the {}".format(out, dice_size or "d100"))
        return out

    def start_quest(self):
        self.world_view.start_music("Mus.mp3")
        self.character_creation()
        if self.the_adventure_begins():
            x = True
            while x:
                x = self._DM.player_choice()

    def character_creation(self):
        self.world_view.clear_screen()
        self._DM.describe("start")
        self.world_view.print_line(text="Greetings Hero, How can we call you?")
        self.name = self.world_view.prompt("&:[name] ")
        self.world_view.print_line(text="Nice to meet you {Name}".format(Name=self.name))
        self.world_view.print_line(text="I see you are a: ")
        self.p_race = self.world_view.prompt("&:[Race] ")
        self.world_view.print_line(text="{Name} the {Race}, is this correct?".format(Name=self.name, Race=self.p_race))
        if self.world_view.prompt("&:[(y)/n] ") == "n":
            out = False
            while not out:
                self.world_view.print_line(text="I must have misheard,")
                self.world_view.print_line(text="# how was it was it again?")
                self.name = self.world_view.prompt("$:[Name] ")
                self.p_race = self.world_view.prompt("$:[Race] ")
                self.world_view.print_line(text="{Name} the {Race}, is this correct?".format(Name=self.name,
                                                                                             Race=self.p_race))
                if self.world_view.prompt("&:[(y)/n] ") == "y":
                    out = True
        self.world_view.print_line(text="Good, it has been a while since we had an adventurer in town,")
        self.world_view.print_line(text="What is your class?")
        self.p_class = self.world_view.prompt("&:[Class] ")
        self.world_view.print_line(text="A {Class}, is this Correct?".format(Class=self.p_class))
        in_put = self.world_view.prompt("&:[(y)/n] ")
        if in_put == "n" or self.p_class not in self.class_list:
            out = False
            while not out:
                self.world_view.print_line(text="I must have misheard,")
                self.world_view.print_line(text="# how was it was it again?")
                i = 0
                s_out, s_out2 = "", ""
                _len = self.class_list.__len__()
                for _class in self.class_list:
                    i += 1
                    if i< _len/2:
                        s_out += _class + ", "
                    elif i <_len-1:
                        s_out2 += _class + ", "
                    elif i < _len:
                        s_out2 += _class + " or "
                    else: s_out2 += _class

                self.world_view.print_line(text="Choose one from: {L}".format(L=s_out))
                self.world_view.print_line(text=s_out2)
                self.p_class = self.world_view.prompt("$:[Class] ")
                self.world_view.print_line(text="A {Class}, is this correct?".format(Class=self.p_class))
                in_put = self.world_view.prompt("&: (y/n) ")
                if not(in_put == "n" or self.p_class not in self.class_list):
                    out = True
        self.set_class_ability()
        self.world_view.print_line(text="Your {Ab} will be useful.".format(Ab=self.c_ability))
        self.inventory.initial_inventory(self.p_class)
        self.world_view.empty_line()
        self.world_view.print_line(text="Well, {N} the {R} {C}".format(N =self.name, R=self.p_race, C=self.p_class))
        self.world_view.wait_prompt()
        # self._DM.set_challenge()

    def set_class_ability(self):
        self.c_ability = self.class_list[self.p_class]

    def get_class_ability(self):
        return self.c_ability

    def get_class(self):
        return self.p_class

    def take_damage(self, damage):
        self.world_view.print_line(text="You take {} point of damage".format(damage))
        self.current_hp = self.current_hp - damage

    def heal_damage(self, healed):
        self.current_hp = self.current_hp + healed

    def get_inventory(self):
        return self.inventory

    def get_race(self):
        return self.p_race

    def increase_stat(self, stat, value):
        if stat == "Def":
            self.base_defence += value
        elif stat == "Att":
            self.base_attack += value
        elif stat == "mHP":
            self.max_hp += value
            self.current_hp +=value

    def decrease_stat(self, stat, value):
        if stat == "Def":
            self.base_defence -= value
        elif stat == "Att":
            self.base_attack -= value
        elif stat == "mHP":
            self.max_hp -= value
            if self.current_hp > self.max_hp:
                self.current_hp = self.max_hp