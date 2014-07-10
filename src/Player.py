class Player:
	'''
	This class will keep track of player name, betting funds,and the bet in the current game,add fund for blackjack and win and
	check wether player has blackjack or busted.
	'''
	def __init__(self):
		self.fund = 100          #player initial betting fund
		self.busted = False
		self.bet = 0
		self.blackjack = False

	def get_fund(self):
		return self.fund 

	def remaining_fund(self):
		self.fund -= self.bet

	def is_busted(self):
		return self.busted

	def add_fund(self):
		if self.blackjack:
			self.fund = 1.5 * self.bet
		else
			self.fund += self.bet

	def current_bet(self,bet):
		self.bet = bet

	def is_blackjack(self):
		return self.blackjack


	def __str__(self):
		return "Fund " + str(self.fund)