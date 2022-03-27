import random


class Card:
    def __init__(self, sign, value):
        self.sign = sign
        self.value = value

    def show(self):
        print(f"{self.value} of {self.sign}")


class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for v in range(1, 14):
            for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    @staticmethod
    def choice():
        v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        s = ["Spades", "Clubs", "Diamonds", "Hearts"]
        print(f"Random card: {random.choice(v)} of {random.choice(s)}")


deck = Deck()
deck.shuffle()
print("Full deck\n")
deck.show()
