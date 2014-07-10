import random
from Card import Card

# define global values and rank for cards
Suits = ('Spades', 'Hearts', 'Clubs' , 'Diamonds')
Ranks = ('ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
Rank_Values = {'ACE':1, '2':2, '3':3 ,'4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}


class Deck:
	'''
	This class implements the deck of playing cards, including member function for initializing,
	shuffling, and dealing from a deck.
	'''
	def __init__(self):
		'''
		Creates the standard deck of 52 cards
		'''
		self.cards = [Card(suit,rank) for suit in Suits for rank in Ranks] 
		random.shuffle(self.cards)


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
			return self.cards.pop(0)

		except IndexError as e:
			print("The deck is out of cards: {e}".format(e))


	def __str__(self):
		card_str = ""
		card_str = [card_str+str(c) for c in self.cards]
		return "".join(card_str)
