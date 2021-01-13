# -*- coding: utf-8 -*-
"""
Date: 12/3/2020
Author: Stuart Page
"""
toboggan_run = []
with open('test_input.txt', 'r') as f:
    data = f.readlines()
for line in data:
    line = line.rstrip()
    toboggan_run.append(line*100000)


class toboggan(object):
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.hit_trees = 0


    def getPosition(self):
        return self.x_position, self.y_position

    def getTreesHit(self):
        return self.hit_trees


    def didIHitATree(self):
        if toboggan_run[self.y_position][self.x_position] == '#':
            self.hit_trees = self.hit_trees + 1
            return 'Yes'
        else:
            return 'No'


    def move(self):
        self.x_position = self.x_position + 1
        self.y_position = self.y_position + 2
        self.didIHitATree()
        return self.x_position, self.y_position

    def atTheBottom(self, toboggan_run):
        if self.y_position == len(toboggan_run) - 1:
            return True
        else:
            return False

jase = toboggan(0,0)

while not jase.atTheBottom(toboggan_run):
    jase.move()


print(jase.getTreesHit())