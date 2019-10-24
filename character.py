import pygame


class Character:
    def __init__(self, shape, HP, MP, ATK, DEF, SP, bullet_speed):
        self.shape = shape
        self.HP = HP
        self.MP = MP
        self.ATK = ATK
        self.DEF = DEF
        self.SPEED = SP
        self.bullet_speed = bullet_speed


# class Wizard(Character):
#     def __init__(self, shape, HP, MP, ATK, DEF, SP):
#         Character.__init__(self, shape, HP, MP, ATK, DEF, SP)
#
#
# class Warrior(Character):
#     def __init__(self, shape, HP, MP, ATK, DEF, SP):
#         Character.__init__(self, shape, HP, MP, ATK, DEF, SP)
