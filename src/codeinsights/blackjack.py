import random

playing = True
game_on = False

# Use tuples because they are immutable
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

ranks = values.keys()


class Card:
    """
     Create a single card
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    """
    Create a new deck and deck functions: shuffle, deal
    """

    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def __str__(self):
        deck_contains = ''
        for card in self.all_cards:
            deck_contains += '\n' + card.__str__()
        return 'There are ' + str(
            len(self.all_cards)) + ' cards left in the deck!' + '\nThe deck contains: ' + deck_contains

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        single_card = self.all_cards.pop()
        return single_card


class Hand:
    """
    Create a hand class to be used for either player or dealer
    """

    def __init__(self):
        self.cards = []
        self.value = 0  # start with an empty hand
        self.aces = 0  # add an attribute to count the number of Aces in hand

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1



class Chips:
    """
    Create a Chip Bank
    """

    def __init__(self):
        while True:
            while True:
                try:
                    self.total = int(input('Please enter the number of chips you would like to purchase: '))
                    break
                except ValueError:
                    print('Sorry, a bet must be an integer!')

            if self.total <= 0:
                print('Sorry, you cannot purchase with negative money, madman! Please enter a positive integer: ')
                continue
            else:
                break

        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips!\nYour bet can't exceed ", chips.total)
            elif chips.bet <= 0:
                print("Good try! Placing a negative or null bet won't work here.")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x not in ['h', 's']:
            print("I didn't catch that. Please enter 'h' or 's' ")
            continue

        elif x[0].lower() == 'h':
            hit(deck, hand)  # hit() function defined above on deck in use for player
            break

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
            break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()


def push():
    print("Dealer and Player tie! No chips won or lost.")


def blackjack_play_game():
    global playing, game_on

    # Begin Game - Game Logic - Put it all together!

    # Greet the user

    print(
        'Welcome to BlackJack!'
        '\nThe goal is to get as close to possible to 21 without going over!'
        '\nDealer hits until he reaches 17.'
        '\nAces can count as 1 or 11.')

    main_loop = True
    while main_loop:

        # Set up the Player's chips outside while loop so that we can have multiple games and keep chip balance
        player_chips = 0

        try:
            player_chips = Chips()
        except ValueError:
            print('Please enter a valid integer')

        if player_chips.total > 0:
            game_on = True

        while game_on:

            # Create & shuffle the deck, deal two cards to each player
            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            player_hand.add_card(deck.deal())
            player_hand.add_card(deck.deal())

            dealer_hand = Hand()
            dealer_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

            if player_chips.total == 0:
                print('Sorry, you are all out of chips!')
                game_on = False
                break

            # Prompt the Player for their bet
            take_bet(player_chips)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            while playing:  # recall this variable from our hit_or_stand function

                # Prompt for Player to Hit or Stand
                hit_or_stand(deck, player_hand)

                # Show cards (but keep one dealer card hidden)
                show_some(player_hand, dealer_hand)

                # If player's hand exceeds 21, run player_busts() and break out of loop
                if player_hand.value > 21:
                    player_busts(player_chips)
                    break

                    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
            if player_hand.value <= 21:

                while dealer_hand.value < 17:
                    hit(deck, dealer_hand)

                    # Show all cards
                show_all(player_hand, dealer_hand)

                # Run different winning scenarios
                if dealer_hand.value > 21:
                    dealer_busts(player_chips)

                elif dealer_hand.value > player_hand.value:
                    dealer_wins(player_chips)

                elif dealer_hand.value < player_hand.value:
                    player_wins(player_chips)

                else:
                    push()

                    # Inform Player of their chips total 
            print("\nPlayer's chip balance: ", player_chips.total)

            # Ask to play again
            new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

            if new_game[0].lower() == 'y':
                playing = True
                continue
            else:
                print("Thanks for playing!")
                game_on = False
                main_loop = False
                break

