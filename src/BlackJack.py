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
	
	def play(self):
		try:
			bet = int(input("How much does to bet?"))
			if bet < 1:
				bet = int(input())
		self.player.remaining_fund(bet)

	
		if self.player.get_fund() > 1:
			print("Sorry,not enough fund to play. Start a new game")
			input()
			sys.exit(0)

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























