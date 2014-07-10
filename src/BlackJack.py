import random
import sys

from Player import Player
from Deck import Deck
from Hand import Hand

class BlackJack:
	'''
	Creates and manages the game.Check for the condition of the game whether player wins, loss or busted.
	'''
	def __init__(self):
		self.deck = Deck()
		self.player = Player()
		self.player_hand = Hand()
		self.dealer_hand = Hand()
	
	
	def place_bet(self):
		if self.player.get_fund() < 1:
			print("Sorry,not enough fund to play. Start a new game")
			input()
			sys.exit(0)

		print("You have "+str(self.player.get_fund())+" chips.")
		bet = int(input("Place your bet: "))
		
		while True:
			try:
				if bet < 1:
					bet = int(input("Bet must be at least 1 chip.Try Again!!! "))
				elif self.player.get_fund() < bet:
					bet = int(input("Not enough chips.Try Again!!! "))
				else:
					break
		
			except ValueError:
				bet = int(input("Doesn't looks like valid bet.Try Again!!!"))

		self.player.remaining_fund(bet)


	def play(self):
		self.player_hand.add_card(self.deck.deal_card())
		self.dealer_hand.add_card(self.deck.deal_card())
		self.player_hand.add_card(self.deck.deal_card())
		self.dealer_hand.add_card(self.deck.deal_card())

		print("Player Hand: ",end="")
		self.player_hand.print_cards()
		print("Dealer Hand: ",end="")
		self.dealer_hand.print_dealer_initial_hand()

		print("\n\nPlayer's Turn:")
		print("Hand: ",end="")
		self.player_hand.print_cards()

		player_input = input("Player's play(Hit/Stand):")
		if player_input.lower() == 'hit':
			busted = False
			while not busted:
				new_card = self.deck.deal_card()
				self.player_hand.add_card(new_card)
				print("\n")
				print(new_card.get_suit()+" of " + new_card.get_rank())
				player_value = self.player_hand.get_value()
					if player_value <= 21:
						print("Hand: ",end="")
						self.player_hand.print_cards()
					else:
						print("Hand: ",end="")
						self.player_hand.print_cards()
						print("BUSTED!!")
						busted = True
				
				else:
					while 
						print("Dealer's Turn:")
						print("Hand :",end="")
						self.dealer_hand.print_cards()
						dealer_value = self.dealer_hand.get_value()
						if dealer_value <= 17:
							print("Dealer's Play: Hit")
							self.dealer_hand.add_card(self.deck.deal_card())

						elif dealer_value >= 17 and dealer_value <= 21:
							print("Dealer's Play: Stand")

						else:
							print("Hand :",end="")
							self.dealer_hand.print_cards()
							print("Dealer Busted")
							busted = True




		else:
			print("Sorry,not enough fund to play. Start a new game")
			input()
			sys.exit(0)


	def hit(self):
		new_card = self.deck.deal_card()
		self.player_hand.add_card(new_card)
		print("\n")
		print(new_card.get_rank()+" of " + new_card.get_suit())
		return self.player_hand.get_value()




b = BlackJack()
b.play()























