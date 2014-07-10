class Player:
	'''
	This class will keep track of player name, betting funds,and the bet in the current game,add fund for blackjack and win and
	check wether player has blackjack or busted.
	'''
	fund = 100  # create static variable fund to play multiple round of game

	def __init__(self):
		self.busted = False
		self.bet = 0
		self.blackjack = False

	def get_fund(self):
		return Player.fund 

	def remaining_fund(self):
		Player.fund -= self.bet

	def is_busted(self):
		return self.busted

	def add_fund(self):
		if self.blackjack:
			Player.fund += 1.5 * self.bet
		else:
			Player.fund += self.bet

	def current_bet(self,bet):
		self.bet = bet

	def is_blackjack(self):
		return self.blackjack


	def __str__(self):
		return "Fund " + str(self.fund)