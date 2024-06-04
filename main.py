import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
        suits = ['♥', '♦', '♠', '♣']
        return suits[self.suit] + values[self.value] + suits[self.suit]

    def __str__(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
        suits = ['♥', '♦', '♠', '♣']
        return suits[self.suit] + values[self.value] + suits[self.suit]


class Deck:
    def __init__(self):
        self.deck = []
        for i in range(4):
            for j in range(13):
                card = Card(j,i)
                self.deck.append(card)

    def __repr__(self):
        return str(self.deck)

    def __str__(self):
        return str(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def pop(self):
        return self.deck.pop()


class Discard:
    def __init__(self):
        self.discard = []

    def __repr__(self):
        return str(self.discard[-1])

    def __str__(self):
        return str(self.discard[-1])

    def add_card(self, card):
        self.discard.append(card)

    def pop(self):
        return self.discard.pop()


class Player:
    def __init__(self):
        self.hand = []
        self.lives = 3

    def draw(self, deck):
        c = deck.pop()
        self.hand.append(c)
        return c

    def discard(self, discard, i):
        c = self.hand.pop(i-1)
        discard.add_card(c)
        return c

    def lose_life(self):
        self.lives -= 1

    def reset_hand(self):
        self.hand = []


def score_hand(hand):
    scores = [2,3,4,5,6,7,8,9,10,10,10,10,11]

    if hand[0].value == hand[1].value == hand[2].value:
        return 30
    elif hand[0].suit == hand[1].suit == hand[2].suit:
        return scores[hand[0].value] + scores[hand[1].value] + scores[hand[2].value]
    elif hand[0].suit == hand[1].suit:
        return max(scores[hand[0].value] + scores[hand[1].value], scores[hand[2].value])
    elif hand[0].suit == hand[2].suit:
        return max(scores[hand[0].value] + scores[hand[2].value], scores[hand[1].value])
    elif hand[1].suit == hand[2].suit:
        return max(scores[hand[1].value] + scores[hand[2].value], scores[hand[0].value])
    else:
        return max(scores[hand[0].value], scores[hand[1].value], scores[hand[2].value])


def play_hand(player1, player2):

    player1.reset_hand()
    player2.reset_hand()

    deck = Deck()
    discard = Discard()
    deck.shuffle()

    player1.draw(deck)
    player1.discard(discard, 1)

    for i in range(3):
        player1.draw(deck)
        player2.draw(deck)

    round = 0

    while True:
        round += 1
        print("-----------------------")
        print("ROUND" + str(round))

        print('Top of Discard Pile: ' + str(discard))
        print('Deck Size: ' + str(len(deck.deck)))
        print('Your Hand: ' + str(player1.hand))
        print('')

        x = input('Input 1 to draw from deck, 2 to draw from discard pile, or 3 to knock: ')
        if int(x) == 1:
            c = player1.draw(deck)
            print('You drew ' + str(c))
        elif int(x) == 2:
            player1.draw(discard)
        elif int(x) == 3:
            break

        print('')
        print('Your Hand: ' + str(player1.hand))
        x = input('Choose a card to discard: ')
        player1.discard(discard, int(x))

        y = random.randint(0, 1)
        if y:
            player2.draw(deck)
            c = player2.discard(discard, random.randint(1, 4))
            print('Computer drew from the deck and discarded ' + str(c))
        else:
            a = player2.draw(discard)
            c = player2.discard(discard, random.randint(1, 4))
            print('Computer drew ' + str(a) + ' from the discard pile and discarded ' + str(c))

    print("-----------------------")
    print('Final Hands')
    print('Your Hand: ' + str(player1.hand) + ' = ' + str(score_hand(player1.hand)))
    print('Computer Hand: ' + str(player2.hand) + ' = ' + str(score_hand(player2.hand)))
    if score_hand(player1.hand) == score_hand(player2.hand):
        print('TIE, NO ONE LOSES A LIFE')
    elif score_hand(player1.hand) > score_hand(player2.hand):
        print('COMPUTER LOSES!')
        player2.lose_life()
    else:
        print('YOU LOSE!')
        player1.lose_life()
    print("-----------------------")


p1 = Player()
p2 = Player()
random.seed()

print("Welcome to 31")

hand_num = 0
while p1.lives > 0 and p2.lives > 0:
    hand_num += 1
    print("HAND: " + str(hand_num))
    print('Your Lives: ' + str(p1.lives))
    print('Computer Lives: ' + str(p2.lives))
    play_hand(p1, p2)

print("Final Score")
print('Your Lives: ' + str(p1.lives))
print('Computer Lives: ' + str(p2.lives))
print("Thanks for playing!")



