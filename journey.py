import random


class Land:
    location_list = []

    def __init__(self, traveler, artist, land_name="Antroria"):
        self.hero = traveler
        self.painter = artist
        self.name = land_name
        self.index = 0

        flops= TheMeauwntain(self.painter, self.hero)
        self.location_list.append(self.Location(self.name,
                                                flops,
                                                "mountain",
                                                self.painter))

        steve = AHelpingClaw(self.painter, self.hero)
        self.location_list.append(self.Location(self.name,
                                                steve,
                                                "village",
                                                self.painter))

        cadarn = TheWitchHunter(self.painter, self.hero)
        self.location_list.append(self.Location(self.name,
                                                cadarn,
                                                "village",
                                                self.painter))

        wiz = FaceTheWizard(self.painter, self.hero)
        self.wizard = self.Location(self.name,
                                    wiz,
                                    "tower",
                                    self.painter)

        st = TownInNeed(self.painter, self.hero)
        self.town_in_need = self.Location(self.name,
                                          st,
                                          "village",
                                          self.painter)

    def get_new_location(self):
        # num = random.randint(0, (self.location_list.__len__() - 1))
        out = self.location_list[self.index]
        self.index += 1
        return out

    def final_location(self):
        return self.wizard

    def first_location(self):
        return self.town_in_need

    class Location:
        def __init__(self, land, encounter, location, visonary):
            thing = encounter
            self.land = land
            self.encounter = thing
            self.location = location
            self.visonary = visonary

        def get_location(self):
            return self.location

        def encounter_loc(self):
            self.visonary.print_line(True, self.encounter.get_title())
            self.visonary.empty_line()
            self.visonary.print_line(text=self.encounter.get_description())
            self.visonary.prompt("$: ")
            return self.encounter.run()


class Encounter:
    @classmethod
    def run(self):
        pass

    @classmethod
    def get_title(cls):
        return cls.title

    @classmethod
    def get_description(cls):
        return cls.description


class TheMeauwntain(Encounter):
    # WIP
    def __init__(self, scene, adventurer):
        self.description = "From miles of you could see this giant mountain where cats rule"
        self.title = "The Grand Meauwntain"
        self.challenge_DC = 15
        self.scene = scene
        self.h_adventurer = adventurer

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.text_block("The large mountain of cats looms before you, and as you approach, its feline guardians "
                              "become aware of your presence")
        self.scene.wait_prompt()

        self.scene.text_block("Standing before the large black gates adorned with cat-like visages, a cheetah saunters "
                              "up to you and with a purring voice: 'Greeting traveler, what do you seek, for not many "
                              " {}s walk these lands. If you have come to ask for our aid, I'm certain that our queen "
                              "will support you in your fight with the evil wizard".format(
            self.h_adventurer.get_race()))
        self.scene.empty_line()
        self.scene.text_block("A: I've come to request your aid of the 'greatest' of the felines")
        self.scene.text_block("B: AS my quest has only just begun, I'm humbled by her knowledge and generosity")
        self.scene.text_block("C: Yes, of course, I came here to ask for your assistance")
        self.scene.text_block("D: How did I get here, I'm very allergic to cats, [and run off]")
        in_cat = ""
        choice_list = ["A", "B", "C", "D"]
        while in_cat not in choice_list:
            in_cat = self.scene.prompt("$:[A, B, C, D] ")
        if in_cat == "A" or in_cat == "B":
            self.scene.text_block("The Cheetah nods, and with the loud creaking of the mighty cat-ish gates the path "
                                  "ahead becomes visible.")
        if in_cat == "C":
            self.scene.text_block("The Cheetah looks at you with a sceptical glance but eventually nods, and with the "
                                  "loud creaking of the mighty cat-ish gates the path ahead becomes visible.")
        if in_cat == "D":
            self.scene.text_block("As the Cheetah bears its fangs, you quicly turn around an run, you are certain that"
                                  "you can find other allies, the kind that aren't felines.")
            return
        self.scene.wait_prompt()
        self.scene.text_block("As you proceed furter into the mauntain, you eventually arive at a grand central place, "
                              "in the centre pertched upon a large wooden structure lies a grey feline of which you "
                              "asume would be the feline queen.")
        self.scene.wait_prompt()
        self.scene.text_block("The Queen speaks 'Greetings adventurer, you have great potential, and therefore you "
                              "can call upon our aid whenever you face the grand wizard, now you must venture forth "
                              "and face the wizard as they grow stronger as time passes, head towards his tower")
        self.h_adventurer.get_inventory().add_inv_item("Boon", "Cats")
        return



class AHelpingClaw(Encounter):
    # WIP
    def __init__(self, scene, adventurer):
        self.description = "From the Dark a clawed hand aids you"
        self.title = "A Black Tabaxi"
        self.challenge_DC = 8
        self.scene = scene
        self.h_adventurer = adventurer

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.text_block("As you stop to hunt, you go in for the kill as you have a perticular good shot, but "
                              "just before you can loosen the arrow, a black shape jumps on your target and kills it. "
                              "As the figure stands, you notice it is a black Tabaxi, and they look in your direction "
                              "'Greetings {}".format(self.h_adventurer.get_race()))
        self.scene.wait_prompt()
        self.scene.text_block("A: Greetings cat-kin, your skills show")
        self.scene.text_block("B: Hey, that was mine!, saves me an arrow though")
        self.scene.text_block("C: Well, that was unexpected, care for sharing?")
        self.scene.text_block("D: MORE CATS!! I'm outa HERE!!")
        in_cat = ""
        choice_list = ["A", "B", "C", "D"]
        while in_cat not in choice_list:
            in_cat = self.scene.prompt("$:[A, B, C, D] ")
        if in_cat == "A" or in_cat == "B":
            self.scene.text_block("Thank you, I have trained, but as I have exerted myself I must rest, "
                                  "care to make camp?")
        if in_cat == "C":
            self.scene.text_block("'Sharing', sure food is better with a friend, provided you cook it.'")
        if in_cat == "D":
            self.scene.text_block("You loosen the arrow and it strikes true, killing the tabaxi, but you don't notice, "
                                  "you are long gone")
            return
        self.scene.wait_prompt()
        self.scene.text_block("As you prepare the creature while your new ally is sleeping, you notice the tabaxi is "
                              "watching you. As you do the cat 'awakes' and they greedily accept the meat you offer "
                              "them, thank you traveler, I have heard about your quest, and I'm willing to aid you "
                              "in your quest, you will see me arrive. When the dinner is completed, the tabaxi walks "
                              "into the forest")
        self.h_adventurer.get_inventory().add_inv_item("Boon", "Steve")
        return



class TheWitchHunter(Encounter):
    def __init__(self, scene, adventurer):
        self.description = "When driven into corner, few are a deadly as him"
        self.title = "A Two sided Word"
        self.challenge_DC = 0
        self.scene = scene
        self.h_adventurer = adventurer

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.text_block("The road is long, and the dark tower is still far away. As you stop for a rest, you "
                              "find yourself surrounded by a group a bandits: 'Hand over your valuables {}, and "
                              "nothing will happen'".format(self.h_adventurer.get_race()))
        self.scene.wait_prompt()
        self.scene.text_block("A: My values are my own, be aware that I'm a {}".format(self.h_adventurer.get_class()))
        self.scene.text_block("B: tut, tut, my deck is stronger than you are")
        self.scene.text_block("C: Stand down, I'm on a quest to save these lands")
        self.scene.text_block("D: BANDITS!? NOPE, NOPE, I'm outta here!!")
        in_cat = ""
        choice_list = ["A", "B", "C", "D"]
        while in_cat not in choice_list:
            in_cat = self.scene.prompt("$:[A, B, C, D] ")
        if in_cat == "A" or in_cat == "B":
            self.scene.text_block("'A feisty one, well well well, that will be fun', as the bandits walk closer "
                                  "their stink and visages are disturbing to say the least")
        if in_cat == "C":
            self.scene.text_block("'A hero, ha, haha, hoho, that is a good one. Well hero where is your white steed?")
        if in_cat == "D":
            self.scene.text_block("Before the bandits can react you dash off, carrying your items and are save once "
                                  "again.")
            return
        self.scene.wait_prompt()
        self.scene.text_block("As you prepare you self for battle, a sudden 'shinng' of a sword being drawn draws "
                              "your and the bandit's attention. A flurry of swords later and when you finally recover "
                              "from the skirmish you notice a large half-orc wielding a part of swords, one of which "
                              "resembles a wolf. They speak 'greetings traveler, your skills speak for themselves, I've "
                              "heard about your quest, and as it happens that our goals align, I offer an alliance', "
                              "You accept and with your new companion you travel towards the tower in the distance")
        self.h_adventurer.get_inventory().add_inv_item("Boon", "Cadarn")
        return


class TownInNeed(Encounter):
    def __init__(self, scene, adventurer):
        self.description = "As you walk in, people start screaming, and running, the town in in peril!"
        self.title = "Town Attack"
        self.challenge_DC = 0
        self.scene = scene
        self.h_adventurer = adventurer

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.text_block("It took some time, but eventually you have arrived in the city of 'Arcanum', the place "
                              "where -according to your findings- you could find the three Magical Surges. From a "
                              "distance the town seems quiet, but as you come closer, you notice the chaos. ")
        self.scene.wait_prompt()
        self.scene.text_block("As you run into the city, you notice various beast rampaging trough the city,"
                              "from zombies to tyrannosaurus rexs, from fiery archers to fire throwing alchemists, "
                              "what will you do?")
        self.scene.wait_prompt()
        self.scene.text_block("A: I'v come to far to fail now, and I have some tricks up my sleeves")
        self.scene.text_block("B: People of Arcanum, fear not for I have arrived, your savior!")
        self.scene.text_block("C: Find someplace to hide, regroup and mount a ounter attack.")
        self.scene.text_block("D: A F***ING T-REX!!! NOPE, NOPE, NOPE, I'M OUTA HERE!!!!")
        in_city = ""
        choice_list = ["A", "B", "C", "D"]
        while in_city not in choice_list:
            in_city = self.scene.prompt("$:[A, B, C, D] ")
        if in_city == "A" or in_city == "B":
            self.scene.text_block("Your words ring trough the city, and emboldens the scattered people of Arcanum, and "
                                  "with your new vigor and you as a powerful ally do they manage to drive back the"
                                  "attackers!, a of combatants die on both sides, but it was a T-REX after all. You "
                                  "have made it clear how you deal with those that oppose you")
            self.scene.wait_prompt()
        if in_city == "C":
            self.scene.text_block("It takes some time, but eventually you have gained the trust of the local people "
                                  "and manage to drive away the attackers, and the stealthy approach has saved the "
                                  "lives of many who would have otherwise died in direct conflict.")
            self.scene.wait_prompt()
        if in_city == "D":
            self.scene.text_block("As you turn around an walk away, the sounds of the carnage fading away and the "
                                  "sounds of birds filling the air, you realize that it is better this way.")
            self.h_adventurer.retire("The Hero Left to be never seen again")
            return False

        self.scene.text_block("With the city in rubble and many of its inhabitans death of wounded you realize that "
                              "it could've been much worse. As you gaze over the death and destruction, the voice "
                              "of the what you presume mayor reaches your ears 'thank you adventurer, I know you have "
                              "done much already, but I fear the worst is yet to come. I ask of you to venture forth "
                              "and aquire the aid of the cats from the Meauwntain, they are out only hope, and if you "
                              "do so, you shall be rewared beyond you wildest dreams!', with little choice, you set "
                              "out into the wilderness, to hopefuly find this 'Meauwntain'")
        self.scene.wait_prompt()

        return True

class FaceTheWizard(Encounter):
    def __init__(self, scene, adventurer):
        self.description = "After many days, you have finally made it, now you must face him"
        self.title = "The Final Conflict"
        self.challenge_DC = 0
        self.scene = scene
        self.h_adventurer = adventurer

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.text_block("You have finally arrived at the tower of the wizard, and you gaze upon its black walls, "
                              "as you do, you notice a small door open and an old man peeks out 'INTRUDER YOU DIE "
                              "NOW!' he yells, and ...")
        self.scene.wait_prompt()
        if not self.h_adventurer.get_inventory().has_item("Boon", "Steve"):
            self.scene.text_block("As you desperately find to hide, you find none, and the blast of the Fireball "
                                  "blows you to pieces.")
            self.scene.wait_prompt()
            return False

        self.scene.text_block("As you see the mage preparing a spell, you curse for not having counter spells. But "
                              "just before they finish. you hear a familair voice coming from the tower '{}', this "
                              "way, following the voice you notice the tabaxi from before holding secret door open.".format(
            self.h_adventurer.get_race()))
        self.scene.wait_prompt()

        self.scene.text_block("A: The halls are filled with blades, runes and other traps, both wirring and sparrking, "
                              "You carefully walk forward, but the traps are various and enventually you trigger one, "
                              "as the blade courses down, you curse 'Cat!'...")
        self.scene.wait_prompt()
        if not self.h_adventurer.get_inventory().has_item("Boon", "Cats"):
            self.scene.text_block("The blade cuts trough and your adventure ends")
            self.scene.wait_prompt()
            return False

        self.scene.text_block("As you close your eyes and wait for the chop that doesn't come. Eventually you open "
                              "your eyes and loop into the greenish eyes of a black feline which is perched upon the "
                              "gnarly blade")
        self.scene.wait_prompt()

        self.scene.text_block("You made you way into the central room and managed to get the drop on the wizard, and "
                              "partly because of your {} you managed to fend of the mage for a while, but now he has you "
                              "cornered and it looks grim...".format(self.h_adventurer.set_class_ability()))
        self.scene.wait_prompt()
        if not self.h_adventurer.get_inventory().has_item("Boon", "Cadarn"):
            self.scene.text_block("The mage proves to strong, and you eventually succumb to their magic.")
            self.scene.wait_prompt()
            return False

        self.scene.text_block("With a loud roar the Half-orc you met on the road runs in and in one slice "
                              "he decapitates the Wizard! You are vicortious!")
        return True