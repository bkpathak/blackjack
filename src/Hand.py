class Hand:
	'''
	Manages a card player has dealt so far, print out the cards in dealer and player in hands and
	determine the total value of cards in the hands.
	'''

	def __init__(self):
		self.hand = []

	def add_card(self,card):
		self.hand.append(card)
		
		
	def get_value(self):
		value = 0
		is_ACE = False
		for card in self.hand:
			rank = card.get_rank()
			if rank == "ACE":
				is_ACE = True
			value += card.get_value(rank)
			#Make Ace value 11 if hand is soft i.e less then 12				
			if is_ACE:
				if value < 12:
					value += 10

		return value

	def is_busted(self):
		if self.get_value() > 21:
			return True
		else:
			return False

	def is_blackjack(self):
		if self.get_value() != 21:
			print("Please, count your card properly.It's not BlackJack.")
			return False
		else:
			return True


	def print_cards(self):
		print(','.join([card.get_rank()+" of "+card.get_suit() for card in self.hand]))

	def print_dealer_initial_hand(self):
		'''
		This function hide one of the player card initially.
		'''
		print(','.join([self.hand[0].get_rank()+" of "+self.hand[0].get_suit(),'[Hidden Card]']))
