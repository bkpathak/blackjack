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

	def print_cards(self):
		print ("Hand: ",end="")
		for card in self.player_hand:
			print(card.get_rank(),"of",card.get_suit,", ",end="")