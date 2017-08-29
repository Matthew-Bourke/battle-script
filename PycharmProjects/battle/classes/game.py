import random


class bcolours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.action = ["Attack", "Magic", "Use item"]

    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(bcolours.OKBLUE + bcolours.BOLD + "Actions:" + bcolours.ENDC)
        for item in self.action:
            print("  " + str(i) + ". ", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolours.OKBLUE + bcolours.BOLD + "\nSpells:" + bcolours.ENDC)
        for spell in self.magic:
            print("  " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1
        print("  0. Back")

    def choose_item(self):
        i = 1
        print(bcolours.OKBLUE + bcolours.BOLD + "\nItems:" + bcolours.ENDC)
        for item in self.items:
            print("  " + str(i) + ".", item["item"].name, ":", item["item"].description, "(x", str(item["quantity"]) +
                  ")")
            i += 1
        print("  0. Back")

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolours.FAIL + bcolours.BOLD + "Target:" + bcolours.ENDC)
        for enemy in enemies:
            if enemy.hp != 0:
                print("  " + str(i) + ".  " + enemy.name)
                i += 1
        choice = int(input("Choose target:")) - 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (((self.hp / self.maxhp) * 100) / 2)

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        max_hp_string = str(self.maxhp) + "/" + str(self.maxhp)
        current_hp = str(self.hp) + "/" + str(self.maxhp)
        hp_space_length = len(max_hp_string) - len(current_hp)
        blank_hp = ""

        if hp_space_length > 0:
            i = hp_space_length
            while i > 0:
                blank_hp += " "
                i -= 1

        max_mp_string = str(self.maxmp) + "/" + str(self.maxmp)
        current_mp = str(self.mp) + "/" + str(self.maxmp)
        mp_space_length = len(max_mp_string) - len(current_mp)
        blank_mp = ""

        if mp_space_length > 0:
            i = mp_space_length
            while i > 0:
                blank_mp += " "
                i -= 1

        print(bcolours.BOLD + "                             __________________________________________________" +
              bcolours.ENDC)
        print(bcolours.BOLD + self.name + ":         " + blank_hp + current_hp + "|" +
              bcolours.FAIL + hp_bar + bcolours.ENDC + bcolours.BOLD + "|")

    def get_stats(self):

        hp_bar_ticks = (((self.hp / self.maxhp) * 100) / 4)
        hp_bar = ""

        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        mp_bar_ticks = (((self.mp / self.maxmp) * 100) / 10)
        mp_bar = ""

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        max_hp_string = str(self.maxhp) + "/" + str(self.maxhp)
        current_hp = str(self.hp) + "/" + str(self.maxhp)
        hp_space_length = len(max_hp_string) - len(current_hp)
        blank_hp = ""

        if hp_space_length > 0:
            i = hp_space_length
            while i > 0:
                blank_hp += " "
                i -= 1

        max_mp_string = str(self.maxmp) + "/" + str(self.maxmp)
        current_mp = str(self.mp) + "/" + str(self.maxmp)
        mp_space_length = len(max_mp_string) - len(current_mp)
        blank_mp = ""

        if mp_space_length > 0:
            i = mp_space_length
            while i > 0:
                blank_mp += " "
                i -= 1

        print(bcolours.BOLD + "                           _________________________               __________" +
              bcolours.ENDC)
        print(bcolours.BOLD + self.name + ":           " + blank_hp + current_hp + "|" +
              bcolours.OKGREEN + hp_bar + bcolours.ENDC + bcolours.BOLD + "|    " + blank_mp + current_mp + "|" +
              bcolours.OKBLUE + mp_bar + bcolours.ENDC + bcolours.BOLD + "|" + bcolours.ENDC)
