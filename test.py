import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards.append(card)
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += self._get_card_value(card)
        if card.rank == 'A':
            self.aces += 1
        self.adjust_for_ace()

    def _get_card_value(self, card):
        if card.rank in ['J', 'Q', 'K']:
            return 10
        elif card.rank == 'A':
            return 11
        else:
            return int(card.rank)

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.play_again = True

    def start_game(self):
        print("Welcome to Blackjack!")
        while self.play_again:
            self.deck.build()
            self.player_hand = Hand()
            self.dealer_hand = Hand()
            self.player_hand.add_card(self.deck.draw_card())
            self.dealer_hand.add_card(self.deck.draw_card())
            self.player_hand.add_card(self.deck.draw_card())
            self.dealer_hand.add_card(self.deck.draw_card())
            self.hand()
            self.player_turn()
            self.dealer_turn()
            self.calculate_winner()
            self.play_again = input("\nDo you want to play again? (y/n): ").lower() == 'y'

    def hand(self):
        print("\nPlayer's Hand:")
        for card in self.player_hand.cards:
            print(card)
        print("Total value:", self.player_hand.value)
        print("\nDealer's Hand:")
        print("Hidden Card")
        print(self.dealer_hand.cards[1])
        print("Total value: Hidden")

    def player_turn(self):
        if self.player_hand.value == 21 and len(self.player_hand.cards) == 2:
            self._show_full_hand()
            print("Blackjack! You win!")
        else:
            while self.player_hand.value < 21:
                choice = input("\nDo you want to hit or stand? (h/s): ").lower()
                if choice == 'h':
                    self.player_hand.add_card(self.deck.draw_card())
                    self.hand()
                elif choice == 's':
                    break
            self._show_full_hand()

    def dealer_turn(self):
        self._show_full_hand()
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.draw_card())
            self._show_full_hand()

    def calculate_winner(self):
        if self.player_hand.value > 21:
            print("Player busted! Dealer wins.")
        elif self.dealer_hand.value > 21:
            print("Dealer busted! You win.")
        elif self.player_hand.value == self.dealer_hand.value:
            print("It's a tie!")
        elif self.player_hand.value > self.dealer_hand.value:
            print("You win!")
        else:
            print("Dealer wins!")

    def _show_full_hand(self):
        print("\nPlayer's Hand:")
        for card in self.player_hand.cards:
            print(card)
        print("Total value:", self.player_hand.value)
        print("\nDealer's Hand:")
        for card in self.dealer_hand.cards:
            print(card)
        print("Total value:", self.dealer_hand.value)


game = BlackjackGame()
game.start_game()