import random

# define global values and rank for cards
Suits = ("Spades", "Hearts", "Clubs" , "Diamonds")
Ranks = ("ACE", "TWO", "THREE" ,"FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING")
Rank_Values = {"ACE":1, "TWO":2, "THREE":3 ,"FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9, "TEN":10, "JACK":10, "QUEEN":10, "KING":10}

class BlackJack:
	'''
	Creates and manages the game.Also creates the required classes for the game.
	'''


class Card:
	'''
	This class manages the cards suits and ranks.
	'''
	def __init__(self,suit,rank):
		if (suit in Suits) and (rank in Ranks):
			self.suit = suit
			self.rank = rank
		else:
			self.suit = None
			self.rank = None

	def get_suit(self):
		return self.suit

	def get_rank(self):
		return self.rank

	def __str__(self):
		return self.suit + self.rank



class Deck:
	'''
	This class implements the deck of playing cards, including member function for initializing,
	shuffling, and dealing from a deck.
	'''
	def __init__(self):
		'''
		Creates the standard deck of 52 cards
		'''
		self.cards = [Card(rank,suit) for suit in Suits for rank in Ranks] 


	def card_shuffle(self):
		'''
		Shuffle the cards in the deck.
		'''
		random.shuffle(self.cards)


	def deal_card(self):
		'''
		Return the card from top of the deck.
		'''
		try:
			return self.card.pop(0)

		except IndexError as e:
			print("The deck is out of cards: {e}".format(e))


	def __str__(self):
		card_str = ""
		card_str = [card_str+str(c) for c in self.cards]
		return "".join(card_str)



class Player:
	'''
	This class will keep track of player name, betting funds,and the bet in the current game.
	'''
	def __init__(self, name):
		self.player_name = name
		self.fund = 100          #player initial betting fund

	def get_current_fund(self,bet):
		return self.fund 

	def remaining_fund(self,bet):
		self.fund -= bet

	def __str__(self):
		return "Name "+self.player_name + ":Fund " + str(self.fund)



class Hand:
	'''
	Manages a card player has dealt so far, print out the cards in dealer and player in hands and
	determine the total value of cards in the hands.
	'''

	def __init__(self):
		self.player_hand = []

	def hand_card(self,card):
		self.player_hand.append(card)
		return self.player_hand

	def get_value(self):
		value = 0
		for card in self.player_hand:
			rank = card.get_rank()
			value += Rank_Value[rank]
		return value


h1=Hand()
print(h1.get_value())