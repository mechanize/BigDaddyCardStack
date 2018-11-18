class Card:
    name, short_text, long_text = "", "", ""
    amount = 0

    def __init__(self, name, short_text, long_text, amount):
        self.name, self.short_text, self.long_text, self.amount = name, short_text, long_text, amount

    def show(self):
        print(self.name + ": " + self.short_text)

    def rule(self):
        print(self.name + ": " + self.long_text)