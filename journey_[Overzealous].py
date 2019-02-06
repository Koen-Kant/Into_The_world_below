import random


class Land:
    location_list = []

    def __init__(self, traveler, artist, land_name="Antroria"):
        self.hero = traveler
        self.painter = artist
        self.name = land_name

        wiz = FaceTheWizard(self.painter, self.hero)
        self.wizard = self.Location(self.name,
                                    wiz,
                                    "tower",
                                    self.painter
        )

        st = TownInNeed(self.painter, self.hero)
        self.town_in_need = self.Location(self.name,
                                          st,
                                          "village",
                                          self.painter)

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

        rak = GoblinAttack(self.painter, self.hero)
        self.location_list.append(self.Location(self.name,
                                                rak,
                                                "village",
                                                self.painter))

        troll = TrollBridge(self.painter, self.hero)
        self.location_list.append(self.Location(self.name,
                                                troll,
                                                "forest",
                                                self.painter))

        two_word = SwordInTheLake(self.painter, self.hero)
        self.location_list.append(self.Location(self.name,
                                                two_word,
                                                "forest",
                                                self.painter))

        irv = HellishAttackers(self.painter, self.hero)
        self.location_list.append(self.Location(self.name,
                                                irv,
                                                "castle",
                                                self.painter))

        bal = BMIGivesAHand(self.painter, self.hero)
        self.location_list.append(self.Location(self.name,
                                                bal,
                                                "village",
                                                self.painter))

        cad = TheWitchHunter(self.painter, self.hero)
        self.location_list.append(self.Location(self.name,
                                                cad,
                                                "village",
                                                self.painter))

        chiek = AMurderOfKenku(self.painter, self.hero)
        self.location_list.append(self.Location(self.name,
                                                chiek,
                                                "forest",
                                                self.painter))

        river = ARiverOfWoe(self.painter, self.hero)
        self.location_list.append(self.Location(self.name,
                                                 river,
                                                "castle",
                                                self.painter))

    def get_new_location(self):
        num = random.randint(0, (self.location_list.__len__() - 1))
        out = self.location_list[num]
        del(self.location_list[num])
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
            self.encounter.run()


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
        self.scene.text_block("You have heard many stories of this gargantuan mountain, it is guarded, controlled, "
                              "protected and controlled by all kinds of cats of various sizes. Now you must venture "
                              "forth, as there as as many rumours of various powerful boons as well.")
        self.scene.wait_prompt()
        self.scene.text_block("You step into the spacious ravine which is the main access point into this mountain, "
                              "you can (P)ress on and hope that you don't encounter the guardians, find a (C)ave and "
                              "evade the prying eyes, Find the (G)uardians and thry to appease them or (S)kulk around "
                              "and try and steal their most sacret possessions, What do you do?")
        choice = "X"
        while choice not in ["P", "C", "G", "S"]:
            choice = self.scene.prompt("$:[P, C, G or S]")
        if choice == "P":
            self.scene.text_block("You follow the crevasse, and move further, steering clear of the central part of "
                                  "the feline kingdom, the journey progresses nicely until you come across a large cliff"
                                  "which is only crossable via a small rickety rope bridge")
            choices = ""
            choice_list = ["C", "P", "A"]
            if self.h_adventurer.get_inventory.has_item(type="Util", item="Rope"):
                choices += "You can try to use your (R)ope to climb down and follow the path from there, "
                choice_list.append("R")
            choices += "you can try to (C)ross the flimzy bridge, "
            choices += "You can try to find another (P)ath or "
            choices += "You can tyr to make (A)nother bridge"
            choice = "X"
            while choice not in [choice_list]:
                choice = self.scene.prompt("$:{} ".format(choice_list))
                if choice == "R":
                    self.scene.text_block("You easily get down from the ledge, and it not long before you find another "
                                          "adventurer who didn't have a rope and fell to their demise, you lost your "
                                          "rope as it is still tied up above.")
                    self.h_adventurer.get_inventory.remove_inv_item("Util", "Rope")
                    success = True
                elif choice == "C":
                    self.scene.text_block("You step on the bridge, and you make it half way before you see a tiger "
                                          "chewing on where the rope is attached to the side from where you came!"
                                          "Your only chance it getting to the other size quickly!")
                    if self.h_adventurer.roll_dice(visible=True, dice_size="d20") >= self.DC:
                        self.scene.text_block("You made it just in time!, and not long after you find something stuck "
                                              "in a tree")
                        success = True
                    else:
                        self.scene.text_block("As the wooden planks fall away from under you, you brace for the fall")
                        self.h_adventurer.take_damage(self.h_adventurer.roll_dice("1d6"))
                        success = False
                    pass
                elif choice == "P":
                    self.scene.text_block("You look around and leave the 'sturdy path' for the unstable surounding area"
                                          "lets hope you find something and don'get lost")
                    if self.h_adventurer.roll_dice(visible=True, dice_size="d20") >= (self.DC-5):
                        self.scene.text_block("You make your way trough the treacherous terrain, and come out unharmed")
                        success = False
                    else:
                        self.scene.text_block("You become lost and eventualy are attacked by a lion")
                        self.h_adventurer.take_damage(self.h_adventurer.roll_dice("1d4"))
                        success = False
                else:
                    self.scene.text_block("You look around and find a procariously placed pile of stones with a tree "
                                          "on top, you attempt to push it over:")
                    if self.h_adventurer.roll_dice(visible=True, dice_size="d20") >= self.DC \
                            or self.h_adventurer.get_class_ability() == "Rage" :
                        self.scene.text_block("The pile collapses with a grand crash and a path is visible")
                        success = False
                    else:
                        self.scene.text_block("The pile finnaly topples but not in the right direction")
                        self.h_adventurer.take_damage(self.h_adventurer.roll_dice("1d4"))
                        success = False
                    pass
                if success:
                    self.h_adventurer.get_inventory.add_inv_item("Util", "Rope")
                    self.h_adventurer.get_inventory.add_inv_item("Util", "lantern")
                    self.h_adventurer.get_inventory.add_gold(13)

        elif choice == "C":
            self.scene.text_block("You find cave")
            choices = ""
            choice_list = ["B", "C", "D"]
            if self.h_adventurer.get_inventory.has_item(type="X", item="Y"):
                choices += "You can try to use your (R)ope to climb down and follow the path from there, "
                choice_list.append("R")
            choices += "C2, "
            choices += "C3 or "
            choices += "C4"
            choice = "X"
            while choice not in [choice_list]:
                choice = self.scene.prompt("$:{} ".format(choice_list))
            if choice == "A":
                self.scene.text_block("You find it")
                self.h_adventurer.get_inventory.remove_inv_item("Util", "Rope")
                success = True
                # item
                pass
            elif choice == "B":
                self.scene.text_block("You find No-it")
                if self.h_adventurer.roll_dice(visible=True, dice_size="d20") >= self.DC:
                    self.scene.text_block("Success")
                    success = True
                else:
                    self.scene.text_block("Fail")
                    self.h_adventurer.take_damage(self.h_adventurer.roll_dice("1d6"))
                    success = False

                # No-item
                pass
            elif choice == "B":
                self.scene.text_block("You find Pa")
                # passive
                if self.h_adventurer.roll_dice(visible=True, dice_size="d20") >= self.DC:
                    self.scene.text_block("Success")
                    success = True
                else:
                    self.scene.text_block("Fail")
                    self.h_adventurer.take_damage(self.h_adventurer.roll_dice("1d6"))
                    success = False
            else:
                self.scene.text_block("You find Ag")
                # Agresive
                if self.h_adventurer.roll_dice(visible=True, dice_size="d20") >= self.DC:
                    self.scene.text_block("Success")
                    success = True
                else:
                    self.scene.text_block("Fail")
                    self.h_adventurer.take_damage(self.h_adventurer.roll_dice("1d6"))
                    success = False
            if success:
                self.h_adventurer.get_inventory.add_inv_item("type", "item")
                self.h_adventurer.get_inventory.add_inv_item("type", "item")
                self.h_adventurer.get_inventory.add_gold(X)

        elif choice == "G":
            # Appease the Guardians
            self.scene.text_block("You find the uardians")
            choices = ""
            choice_list = ["B", "C", "D"]
            if self.h_adventurer.get_inventory.has_item(type="X", item="Y"):
                choices += "You can try to use your (R)ope to climb down and follow the path from there, "
                choice_list.append("R")
            choices += "C2, "
            choices += "C3 or "
            choices += "C4"
            choice = "X"
            while choice not in [choice_list]:
                choice = self.scene.prompt("$:{} ".format(choice_list))
            if choice == "A":
                self.scene.text_block("You find it")
                self.h_adventurer.get_inventory.remove_inv_item("Util", "Rope")
                success = True
                # item
                pass
            elif choice == "B":
                self.scene.text_block("You find No-it")
                if self.h_adventurer.roll_dice(visible=True, dice_size="d20") >= self.DC:
                    self.scene.text_block("Success")
                    success = True
                else:
                    self.scene.text_block("Fail")
                    self.h_adventurer.take_damage(self.h_adventurer.roll_dice("1d6"))
                    success = False

                # No-item
                pass
            elif choice == "B":
                self.scene.text_block("You find Pa")
                # passive
                if self.h_adventurer.roll_dice(visible=True, dice_size="d20") >= self.DC:
                    self.scene.text_block("Success")
                    success = True
                else:
                    self.scene.text_block("Fail")
                    self.h_adventurer.take_damage(self.h_adventurer.roll_dice("1d6"))
                    success = False
            else:
                self.scene.text_block("You find Ag")
                # Agresive
                if self.h_adventurer.roll_dice(visible=True, dice_size="d20") >= self.DC:
                    self.scene.text_block("Success")
                    success = True
                else:
                    self.scene.text_block("Fail")
                    self.h_adventurer.take_damage(self.h_adventurer.roll_dice("1d6"))
                    success = False
            if success:
                self.h_adventurer.get_inventory.add_inv_item("type", "item")
                self.h_adventurer.get_inventory.add_inv_item("type", "item")
                self.h_adventurer.get_inventory.add_gold(X)

        else:
            self.scene.text_block("You skulk")
            choices = ""
            choice_list = ["B", "C", "D"]
            if self.h_adventurer.get_inventory.has_item(type="X", item="Y"):
                choices += "You can try to use your (R)ope to climb down and follow the path from there, "
                choice_list.append("R")
            choices += "C2, "
            choices += "C3 or "
            choices += "C4"
            choice = "X"
            while choice not in [choice_list]:
                choice = self.scene.prompt("$:{} ".format(choice_list))
            if choice == "A":
                self.scene.text_block("You find it")
                self.h_adventurer.get_inventory.remove_inv_item("Util", "Rope")
                success = True
                # item
                pass
            elif choice == "B":
                self.scene.text_block("You find No-it")
                if self.h_adventurer.roll_dice(visible=True, dice_size="d20") >= self.DC:
                    self.scene.text_block("Success")
                    success = True
                else:
                    self.scene.text_block("Fail")
                    self.h_adventurer.take_damage(self.h_adventurer.roll_dice("1d6"))
                    success = False

                # No-item
                pass
            elif choice == "B":
                self.scene.text_block("You find Pa")
                # passive
                if self.h_adventurer.roll_dice(visible=True, dice_size="d20") >= self.DC:
                    self.scene.text_block("Success")
                    success = True
                else:
                    self.scene.text_block("Fail")
                    self.h_adventurer.take_damage(self.h_adventurer.roll_dice("1d6"))
                    success = False
            else:
                self.scene.text_block("You find Ag")
                # Agresive
                if self.h_adventurer.roll_dice(visible=True, dice_size="d20") >= self.DC:
                    self.scene.text_block("Success")
                    success = True
                else:
                    self.scene.text_block("Fail")
                    self.h_adventurer.take_damage(self.h_adventurer.roll_dice("1d6"))
                    success = False
            if success:
                self.h_adventurer.get_inventory.add_inv_item("type", "item")
                self.h_adventurer.get_inventory.add_inv_item("type", "item")
                self.h_adventurer.get_inventory.add_gold(X)


class AHelpingClaw(Encounter):
    def __init__(self, scene, adventurer):
        self.description = "From the Dark a clawed hand aids you"
        self.title = "A Black Tabaxi"
        self.challenge_DC = 8
        self.scene = scene

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.print_line(text="you encountered {}".format(self.title))
        self.scene.wait_prompt()
        # arrive
        # 4 actions
        # challenge
        # 4 actions
        # conclusion
        pass


class GoblinAttack(Encounter):
    def __init__(self, scene, adventurer):
        self.description = "They're everywhere, run for the hills!!"
        self.title = "Goblin attack on caravan"
        self.challenge_DC = 12
        self.scene = scene

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.print_line(text="you encountered {}".format(self.title))
        self.scene.wait_prompt()
        # arrive
        # 4 actions
        # challenge
        # 4 actions
        # conclusion
        pass


class TrollBridge(Encounter):
    def __init__(self, scene, adventurer):
        self.description = "A nice bridge, as long as you can pay the t(r)oll"
        self.title = "T(r)oll bridge"
        self.challenge_DC = 13
        self.scene = scene

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.print_line(text="you encountered {}".format(self.title))
        self.scene.wait_prompt()
        # arrive
        # 4 actions
        # challenge
        # 4 actions
        # conclusion
        pass


class SwordInTheLake(Encounter):
    def __init__(self, scene, adventurer):
        self.description = "A glimmer of ligth is at the bottom of the lake"
        self.title = "The Lake of the Lady"
        self.challenge_DC = 20
        self.scene = scene

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.print_line(text="you encountered {}".format(self.title))
        self.scene.wait_prompt()
        # arrive
        # 4 actions
        # challenge
        # 4 actions
        # conclusion
        pass


class HellishAttackers(Encounter):
    def __init__(self, scene, adventurer):
        self.description = "The Duke's castle is under attack, he needs YOU!"
        self.title = "When Beelzebub comes knocking"
        self.challenge_DC = 15
        self.scene = scene

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.print_line(text="you encountered {}".format(self.title))
        self.scene.wait_prompt()
        # arrive
        # 4 actions
        # challenge
        # 4 actions
        # conclusion
        pass


class BMIGivesAHand(Encounter):
    def __init__(self, scene, adventurer):
        self.description = "A caravan with a familiar lofo rolls into town"
        self.title = "The BMI Caravan"
        self.challenge_DC = 15
        self.scene = scene

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.print_line(text="you encountered {}".format(self.title))
        self.scene.wait_prompt()
        # arrive
        # 4 actions
        # challenge
        # 4 actions
        # conclusion
        pass


class TheWitchHunter(Encounter):
    def __init__(self, scene, adventurer):
        self.description = "When driven into corner, few are a deadly as him"
        self.title = "A Two sided Word"
        self.challenge_DC = 0
        self.scene = scene

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.print_line(text="you encountered {}".format(self.title))
        self.scene.wait_prompt()
        # arrive
        # 4 actions
        # challenge
        # 4 actions
        # conclusion
        pass


class AMurderOfKenku(Encounter):
    def __init__(self, scene, adventurer):
        self.description = "A flock of black humanoid bars your path, don seem to smart"
        self.title = "Le Chiekien noir"
        self.challenge_DC = 0
        self.scene = scene

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.print_line(text="you encountered {}".format(self.title))
        self.scene.wait_prompt()
        # arrive
        # 4 actions
        # challenge
        # 4 actions
        # conclusion
        pass


class ARiverOfWoe(Encounter):
    def __init__(self, scene, adventurer):
        self.description = "You can't proceed, for .. it .. is .. a .. river!"
        self.title = "A bridge to far"
        self.challenge_DC = 0
        self.scene = scene

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.print_line(text="you encountered {}".format(self.title))
        self.scene.wait_prompt()
        # arrive
        # 4 actions
        # challenge
        # 4 actions
        # conclusion
        pass


class TownInNeed(Encounter):
    def __init__(self, scene, adventurer):
        self.description = "As you walk in, people start screaming, and running, the town in in peril!"
        self.title = "Town Attack"
        self.challenge_DC = 0
        self.scene = scene

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.print_line(text="you encountered {}".format(self.title))
        self.scene.wait_prompt()
        # arrive
        # 4 actions
        # challenge
        # 4 actions
        # conclusion
        pass


class FaceTheWizard(Encounter):
    def __init__(self, scene, adventurer):
        self.description = "After many days, you have finally made it, now face him"
        self.title = "The Final Conflict"
        self.challenge_DC = 0
        self.scene = scene

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def run(self):
        self.scene.print_line(text="you encountered {}".format(self.title))
        self.scene.wait_prompt()
        # arrive
        # 4 actions
        # challenge
        # 4 actions
        # conclusion
        pass