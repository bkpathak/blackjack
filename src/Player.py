class Player:
	'''
	This class will keep track of player name, betting funds,and the bet in the current game.
	'''
	def __init__(self, name):
		self.player_name = name
		self.fund = 100          #player initial betting fund

	def get_current_fund(self,bet):
		return self.fund 

	def remaining_fund(self,bet):
		self.fund -= bet

	def __str__(self):
		return "Name "+self.player_name + ":Fund " + str(self.fund)