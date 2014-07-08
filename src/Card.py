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

	def get_value(self,rank):
		return Rank_Values[rank]


	def __str__(self):
		return self.suit + self.rank