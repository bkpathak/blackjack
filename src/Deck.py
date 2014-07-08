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