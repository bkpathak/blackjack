class Player:
	'''
	This class will keep track of player name, betting funds,and the bet in the current game.
	'''
	def __init__(self):
		self.fund = 100          #player initial betting fund
		self.busted = False

	def get_fund(self):
		return self.fund 

	def remaining_fund(self,bet):
		self.fund -= bet

	def is_busted(self):
		return self.busted

	def __str__(self):
		return "Fund " + str(self.fund)