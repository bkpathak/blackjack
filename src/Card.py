Rank_Values = {'ACE':1, '2':2, '3':3 ,'4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

class Card:
	'''
	This class manages the cards suits and ranks.
	'''
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def get_suit(self):
		return self.suit

	def get_rank(self):
		return self.rank

	def get_value(self,rank):
		return Rank_Values[rank]


	def __str__(self):
		return self.suit + self.rank
