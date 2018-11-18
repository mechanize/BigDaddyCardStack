import Card
import Main
import random
class Stack:
    stack = []
    active_card = Card

    def __init__(self):

    def draw(self):
        self.active_card = random.choice(self.stack)
        self.active_card.show()

    def rule(self):
        self.active_card.show()

    def shuffle(self):

