class Player:
	'''
	This class will keep track of player name, betting funds,and the bet in the current game,add fund for blackjack and win and
	check wether player has blackjack or busted.
	'''
	fund = 100  # create static variable fund to play multiple round of game

	def __init__(self):
		self.busted = [False,False]   # To handle each split case separately
		self.bet = []
		self.blackjack = False
		self.split = False

	def get_fund(self):
		'''
		Fund at the end of each round.
		'''
		return Player.fund 
	
	def get_bet(self):
		return sum(self.bet)


	def remaining_fund(self):
		if self.split:
			Player.fund -= self.bet[0]
		else:
			Player.fund -= sum(self.bet)

	def current_fund(self):
		'''
		Fund to play for current round.
		'''
		return Player.fund - sum(self.bet)

	def is_busted(self,index = 0):
		if index == 0:
			return self.busted[index]
		else:
			return self.busted[index]

	def is_split(self):
		return self.split

	def add_fund(self):
		if self.blackjack:
			Player.fund += 1.5 * sum(self.bet)
		
		elif self.split:
			Player.fund += self.bet[0]

		else:
			Player.fund += sum(self.bet)

	def current_bet(self,bet):
		self.bet.append(bet)

	def is_blackjack(self):
		return self.blackjack


	def __str__(self):
		return "Fund " + str(self.fund)