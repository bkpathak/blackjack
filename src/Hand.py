class Hand:
	'''
	Manages a card player has dealt so far, print out the cards in dealer and player in hands and
	determine the total value of cards in the hands.
	'''

	def __init__(self):
		self.player_hand = []

	def add_card(self,card):
		self.player_hand.append(card)
		return self.player_hand

	def get_value(self):
		value = 0
		for card in self.player_hand:
			rank = card.get_rank()
			if rank == "ACE" and value <= 10:
				value += 11
			else:	
				value += card.get_value(rank)
		return value

	def print_cards(self):
		print(','.join([card.get_rank()+" of "+card.get_suit() for card in self.player_hand]))

	def print_dealer_initial_hand(self):
		'''
		This function hide one of the player card initially.
		'''
		print(','.join([self.player_hand[0].get_rank()+" of "+self.player_hand[0].get_suit(),'[Hidden Card]']))
