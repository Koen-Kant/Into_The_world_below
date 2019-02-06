import random


class DM:
    def __init__(self, party, vision):
        self.hero = party
        self.vision = vision
        self.CR = 3
        self.time = 0

    def advance_time(self):
        self.time = self.time+1
        self.vision.full_line()
        self.vision.print_line(text="A day passes, The Evil Wizard Grows Stronger")
        self.vision.print_line(text="It is now {D} day(s) since the attack on the village.".format(D=self.time))
        self.vision.full_line()

    def print_player_stats(self):
        stats = self.hero.get_stats()
        self.vision.print_line(text="Name: {Name:10s} # HP   : {Cur:4d}/{Max:4d}".format(Name=stats["Name"],
                                                                                         Cur=stats["cHP"],
                                                                                         Max=stats["mHP"]))
        self.vision.print_line(text="Race: {R:10s} # Class: {C:10s}".format(C=stats["Class"],
                                                                            R=stats["Race"]))

    def player_choice(self):
        self.vision.clear_screen()
        self.vision.full_line()
        if self.time < self.CR:
            self.vision.print_line(text="What Do you want to Do?")
            done = False
            while not done:
                # self.vision.print_line(text="(R)est, (P)roceed, To (T)own (Re)tire")
                # choice = self.vision.prompt("$:[R, P, T or Re] ")
                self.vision.print_line(text="(P)roceed or (Re)tire")
                choice = self.vision.prompt("$:[P or Re] ")
                self.vision.full_line()
                self.vision.clear_screen()
                if choice == "P":
                    done = True
                    self.hero.venture()
                # elif choice == "R":
                #     done = True
                #     self.hero.rest()
                # elif choice == "T":
                #     done = True
                #     self.hero.go_to_town()
                elif choice == "Re":
                    self.hero.retire("gave up")
                    return False
                else:
                    done = False
                    self.vision.full_line()
                    self.vision.print_line(text="That wasn't an option.")
            return True
        else:
            self.vision.print_line(text="it is time to face The Evil Wizard")
            if self.hero.the_grand_final():
                self.vision.wait_prompt()
                self.hero.victory()
            else:
                self.vision.wait_prompt()
                self.hero.defeat()
            self.hero.end_game()
            return False

    def set_challenge(self):
        done = False
        while not done:
            self.vision.print_line(text="(E)asy, (M)edium or (H)ard")
            challenge = self.vision.prompt("$:[E, M or H] ")
            if challenge == "H":
                done = True
                self.CR = 10
                self.vision.empty_line()
            elif challenge == "M":
                done = True
                self.CR = 5
                self.vision.empty_line()
            elif challenge == "E":
                done = True
                self.CR = 3
                self.vision.empty_line()
            else:
                self.vision.print_line(text="That wasn't an option:")

    def describe(self, place):
        loc = place.upper()
        if place == "forest":
            self.vision.full_line()
            self.vision.empty_line()
            self.vision.empty_line()
            self.vision.empty_line()
            self.vision.empty_line()
            self.vision.print_line(text=r"             ,@@@@@@@,                ")
            self.vision.print_line(text=r"     ,,,.   ,@@@@@@/@@,  .oo8888o.    ")
            self.vision.print_line(text=r"  ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o   ")
            self.vision.print_line(text=r" ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'  ")
            self.vision.print_line(text=r" %&&%&%&/%&&%@@\@@/ /@@@88888\88888'  ")
            self.vision.print_line(text=r" %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'   ")
            self.vision.print_line(text=r" `&%\ ` /%&'    |.|        \ '|8'     ")
            self.vision.print_line(text=r"     |o|        | |         | |       ")
            self.vision.print_line(text=r"     |.|        | |         | |       ")
            self.vision.print_line(text=r"  \\/ ._\//_/__/  ,\_//__\\/.  \_//__/")
            self.vision.empty_line()
            self.vision.empty_line()
            self.vision.empty_line()
            self.vision.empty_line()
            self.vision.print_line(True, loc)

        elif place == "castle":
            self.vision.full_line()
            self.vision.print_line(text=r"                   |>>>               ")
            self.vision.print_line(text=r"                   |                  ")
            self.vision.print_line(text=r"     |>>>      _  _|_  _         |>>> ")
            self.vision.print_line(text=r"     |        |;| |;| |;|        |    ")
            self.vision.print_line(text=r" _  _|_  _    \\.    .  /    _  _|_  _")
            self.vision.print_line(text=r"|;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;")
            self.vision.print_line(text=r"\\..      /    ||;   . |    \\.    .  ")
            self.vision.print_line(text=r" \\.  ,  /     ||:  .  |     \\:  .  /")
            self.vision.print_line(text=r"  ||:   |_   _ ||_ . _ | _   _||:   | ")
            self.vision.print_line(text=r"  ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  | ")
            self.vision.print_line(text=r"  ||:   ||.    .     .      . ||:  .| ")
            self.vision.print_line(text=r"  ||: . || .     . .   .  ,   ||:   | ")
            self.vision.print_line(text=r"  ||:   ||:  ,  _______   .   ||: , | ")
            self.vision.print_line(text=r"  ||:   || .   /+++++++\    . ||:   | ")
            self.vision.print_line(text=r"  ||:   ||.    |+++++++| .    ||: . | ")
            self.vision.print_line(text=r"_ ||: . ||: ,  |+++++++|.  . _||_   | ")
            self.vision.print_line(text=r"  '--~~__|.    |+++++++|----~    ~`-- ")
            self.vision.print_line(text=r"                   ~---__|,--~'       ")
            self.vision.print_line(True, loc)

        elif place == "mountain":
            self.vision.full_line()
            self.vision.print_line(text=r"           /   \              / \     ")
            self.vision.print_line(text=r"\     / .,/     \_         .,'   \    ")
            self.vision.print_line(text=r"     /            \      _/       \_  ")
            self.vision.print_line(text=r"    /              \    /           \/")
            self.vision.print_line(text=r" \_/                \  /',.,''\     \\")
            self.vision.print_line(text=r"                  _  \/   /    ',../',")
            self.vision.print_line(text=r"    /           _/m\  \  /    |       ")
            self.vision.print_line(text=r"  _/           /MMmm\  \_     |       ")
            self.vision.print_line(text=r" /      \     |MMMMmm|   \__   \      ")
            self.vision.print_line(text=r"         \   /MMMMMMm|      \   \     ")
            self.vision.print_line(text=r"          \  |MMMMMMmm\      \___     ")
            self.vision.print_line(text=r"           \|MMMMMMMMmm|____.'  /\_   ")
            self.vision.print_line(text=r"           /'.,___________...,,'   \  ")
            self.vision.print_line(text=r"          /       \          |      \ ")
            self.vision.print_line(text=r"        _/        |           \     \\")
            self.vision.print_line(text=r"       /                              ")
            self.vision.empty_line()
            self.vision.empty_line()
            self.vision.print_line(True, loc)

        elif place == "start":
            self.vision.full_line()
            self.vision.print_line(text=r"                   |>>>               ")
            self.vision.print_line(text=r"                   |                  ")
            self.vision.print_line(text=r"     |>>>      _  _|_  _         |>>> ")
            self.vision.print_line(text=r"     |        |;| |;| |;|        |    ")
            self.vision.print_line(text=r" _  _|_  _    \\.    .  /    _  _|_  _")
            self.vision.print_line(text=r"|;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;")
            self.vision.print_line(text=r"\\..      /    ||;   . |    \\.    .  ")
            self.vision.print_line(text=r" \\.  ,  /     ||:  .  |     \\:  .  /")
            self.vision.print_line(text=r"  ||:   |_   _ ||_ . _ | _   _||:   | ")
            self.vision.print_line(text=r"  ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  | ")
            self.vision.print_line(text=r"  ||:   ||.    .     .      . ||:  .| ")
            self.vision.print_line(text=r"  ||: . || .     . .   .  ,   ||:   | ")
            self.vision.print_line(text=r"  ||:   ||:  ,  _______   .   ||: , | ")
            self.vision.print_line(text=r"  ||:   || .   /+++++++\    . ||:   | ")
            self.vision.print_line(text=r"  ||:   ||.    |+++++++| .    ||: . | ")
            self.vision.print_line(text=r"_ ||: . ||: ,  |+++++++|.  . _||_   | ")
            self.vision.print_line(text=r"  '--~~__|.    |+++++++|----~    ~`-- ")
            self.vision.print_line(text=r"                   ~---__|,--~'       ")
            self.vision.print_line(True, loc)

        elif place == "end":
            self.vision.full_line()
            self.vision.print_line(text=r"                   |>>>               ")
            self.vision.print_line(text=r"                   |                  ")
            self.vision.print_line(text=r"     |>>>      _  _|_  _         |>>> ")
            self.vision.print_line(text=r"     |        |;| |;| |;|        |    ")
            self.vision.print_line(text=r" _  _|_  _    \\.    .  /    _  _|_  _")
            self.vision.print_line(text=r"|;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;")
            self.vision.print_line(text=r"\\..      /    ||;   . |    \\.    .  ")
            self.vision.print_line(text=r" \\.  ,  /     ||:  .  |     \\:  .  /")
            self.vision.print_line(text=r"  ||:   |_   _ ||_ . _ | _   _||:   | ")
            self.vision.print_line(text=r"  ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  | ")
            self.vision.print_line(text=r"  ||:   ||.    .     .      . ||:  .| ")
            self.vision.print_line(text=r"  ||: . || .     . .   .  ,   ||:   | ")
            self.vision.print_line(text=r"  ||:   ||:  ,  _______   .   ||: , | ")
            self.vision.print_line(text=r"  ||:   || .   /+++++++\    . ||:   | ")
            self.vision.print_line(text=r"  ||:   ||.    |+++++++| .    ||: . | ")
            self.vision.print_line(text=r"_ ||: . ||: ,  |+++++++|.  . _||_   | ")
            self.vision.print_line(text=r"  '--~~__|.    |+++++++|----~    ~`-- ")
            self.vision.print_line(text=r"                   ~---__|,--~'       ")
            self.vision.print_line(True, loc)

        elif place == "camp":
            self.vision.full_line()
            self.vision.empty_line()
            self.vision.empty_line()
            self.vision.empty_line()
            self.vision.print_line(text=r"                     __,--\           ")
            self.vision.print_line(text=r"               __,--'    :.\.         ")
            self.vision.print_line(text=r"          _,--'             \`.       ")
            self.vision.print_line(text=r"        /|\       `          \ `.     ")
            self.vision.print_line(text=r"       / | \        `:        \  `/   ")
            self.vision.print_line(text=r"      / '|  \        `:.       \      ")
            self.vision.print_line(text=r"     / , |   \                  \     ")
            self.vision.print_line(text=r"    /    |:   \              `:. \    ")
            self.vision.print_line(text=r"   /| '  |     \ :.           _,-'`.  ")
            self.vision.print_line(text=r"  ' |,  / \   ` \ `:.     _,-'_|    `/")
            self.vision.print_line(text=r"    '._;   \ .   \   `_,-'_,-'        ")
            self.vision.print_line(text=r"   \'    `- .\_   |\,-'_,-'           ")
            self.vision.print_line(text=r"               `--|_,`'               ")
            self.vision.print_line(text=r"                        `/""          ")
            self.vision.print_line(text=r"                   __,--'\            ")
            self.vision.print_line(True, loc)

        elif place == "tower":
            self.vision.full_line()
            self.vision.print_line(text=r"                  |\                  ")
            self.vision.print_line(text=r"                  |_\                 ")
            self.vision.print_line(text=r"                  |                   ")
            self.vision.print_line(text=r"                  |                   ")
            self.vision.print_line(text=r",__,              /                   ")
            self.vision.print_line(text=r"0000)            /\                   ")
            self.vision.print_line(text=r"000)    __      /# \                  ")
            self.vision.print_line(text=r"8889)  (00)    /### \                 ")
            self.vision.print_line(text=r"90OO0)(0000)  /a#### \                ")
            self.vision.print_line(text=r"(0000000)    /####### \    sSSsS,     ")
            self.vision.print_line(text=r"             |a'aaaaa |   ssSSSs8     ")
            self.vision.print_line(text=r"             |aa'  aa |   SSSSSSs'    ")
            self.vision.print_line(text=r"             |aa'  a' |   s\\Ss/Ss    ")
            self.vision.print_line(text=r"             |a'aaaaa |    s\\//S     ")
            self.vision.print_line(text=r"             |aaa'aa| |      |/       ")
            self.vision.print_line(text=r"           #8|a|aaaaa |#     ||       ")
            self.vision.print_line(text=r"          # 8|aaa|aaa||###8  ||       ")
            self.vision.print_line(text=r"         #8###aaaaaaa |88##8###  ##   ")
            self.vision.print_line(True, loc)

        elif place == "village":
            self.vision.full_line()
            self.vision.empty_line()
            self.vision.empty_line()
            self.vision.empty_line()
            self.vision.empty_line()
            self.vision.print_line(text=r"  ~         ~~          __            ")
            self.vision.print_line(text=r"       _T      .,,.    ~--~ ^^        ")
            self.vision.print_line(text=r" ^^   // \                    ~       ")
            self.vision.print_line(text=r"      ][O]    ^^      ,-~ ~           ")
            self.vision.print_line(text=r"   /''-I_I         _II____            ")
            self.vision.print_line(text=r"__/_  /   \ ______/ ''   /'\_,__      ")
            self.vision.print_line(text=r"  | II--'''' \,--:--..,_/,.-{ },      ")
            self.vision.print_line(text=r"; '/__\,.--';|   |[] .-.| O{ _ }      ")
            self.vision.print_line(text=r":' |  | []  -|   ''--:.;[,.'\,/       ")
            self.vision.print_line(text=r"'  |[]|,.--'' '',   ''-,.    |        ")
            self.vision.print_line(text=r"  ..    ..-''    ;       ''. '        ")
            self.vision.empty_line()
            self.vision.empty_line()
            self.vision.empty_line()
            self.vision.print_line(True, loc)

        else:
            self.vision.full_line()
            for i in range(0,18):
                self.vision.empty_line()
            self.vision.print_line(True, loc)

