class Inventory:
    def __init__(self, hero):
        self.class_gear = {"Barbarian": {"Weapons": {"Greatsword":      "Weapon"},
                                        },
                           "Bard":      {"Armour":  {"Leather Armour":  "Armour"},
                                         "Weapons": {"Dagger":          "Weapon"},
                                         "Magic":   {"Lute":            "Magic"}
                                        },
                           "Cleric":    {"Armour":  {"Chain mail":      "Armour"},
                                         "Weapons": {"Mace":            "Weapon"},
                                         "Magic":   {"Holy Symbol":     "Magic"}
                                        },
                           "Druid":     {"Armour":  {"Hide":            "Armour"},
                                         "Weapons": {"Quarterstaff":    "Weapon"},
                                         "Magic":   {"Antlers":         "Magic"}
                                        },
                           "Fighter":   {"Armour":  {"Chain Mail":      "Armour"},
                                         "Weapons": {"Longsword":       "Weapons"},
                                         "Shield":   {"Shield":         "Shield"}
                                        },
                           "Monk":      {"Weapons": {"Quarterstaff":    "Weapons"},
                                        },
                           "Paladin":   {"Armour":  {"Chain Mail":      "Armour"},
                                         "Weapons": {"Longsword":       "Weapons"},
                                         "Shield":   {"Shield":         "Shield"}
                                        },
                           "Ranger":    {"Armour":  {"Studded Armour":  "Armour"},
                                         "Weapons": {"Longbow":         "Weapons"},
                                         "Ammo":   {"20 Arrows":        "Ammo"}
                                        },
                           "Rogue":     {"Armour":  {"Studded Armour":  "Armour"},
                                         "Weapons": {"2 Daggers":       "Weapons"},
                                         "Tools":   {"Thieves Tools":   "Tools"}
                                        },
                           "Sorcerer":  {"Magic":   {"Orb":             "Magic"}
                                        },
                           "Warlock":   {"Armour":  {"Leather Armour":  "Armour"},
                                         "Weapons": {"Dagger" :         "Weapon"},
                                         "Magic":   {"Arcane Rod":      "Magic"}
                                        },
                           "Wizard":    {"Magic":   {"Spellbook":       "Magic"}
                                        }
                           }
        self.inventory = {}
        self.hero = hero
        self.gold = 10

    def manage_inventory(self):
        pass

    def has_item(self, type, item):
        if self.has_item_type(type):
            if item in self.inventory[type]:
                return True
        return False

    def has_item_type(self, item_type):
        if item_type in self.inventory:
            return True
        else:
            return False

    def initial_inventory(self, p_class):
        self.inventory = self.class_gear[p_class]

    def add_inv_item(self, type, item):
        # self.hero.world_view.print_line(text="You get a {}".format(item))
        if type not in self.inventory.keys():
            self.inventory[type] = {item:type}
        else:
            self.inventory[type][item] = type

    def add_gold(self, ammount):
        self.hero.world_view.print_line(text="You get {} gold pieces".format(ammount))
        self.gold += ammount

    def get_gold(self):
        return self.gold

    def lose_gold(self, ammount):
        self.hero.world_view.print_line(text="You lose {} gold pieces".format(ammount))
        self.gold -= ammount

    def remove_inv_item(self, type, item):
        del(self.inventory[type][item])

