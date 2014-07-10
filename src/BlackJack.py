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
			print("Sorry,not enough fund to play. Start a new game.")
			input()
			sys.exit(0)

		print("You have {0:.2f}".format(self.player.get_fund())+" chips.")
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

		self.player.current_bet(bet)


	def player_move(self):
		self.player_hand.add_card(self.deck.deal_card())
		self.dealer_hand.add_card(self.deck.deal_card())
		self.player_hand.add_card(self.deck.deal_card())
		self.dealer_hand.add_card(self.deck.deal_card())
		print("\n")
		print("Player Hand: ",end="")
		self.player_hand.print_cards()
		print("Dealer Hand: ",end="")
		self.dealer_hand.print_dealer_initial_hand()

		print("\n\nPlayer's Turn:")
		print("Hand: ",end="")
		self.player_hand.print_cards()
		print("\n")
		player_input = input("Player's play:")

		while True:
			if player_input.lower() == 'hit':
				new_card = self.deck.deal_card()
				self.player_hand.add_card(new_card)
				print(new_card.get_rank()+" of " + new_card.get_suit())
				if self.player_hand.get_value() > 21:
					self.player.busted = True
					break
			
			elif player_input.lower() == 'blackjack':
				if self.player_hand.get_value() != 21:
					print("Please, count your card properly.It's not BlackJack.")

				else:
					self.player.blackjack = True
					break

			else:
				break
			
			print("Hand: ",end="")
			self.player_hand.print_cards()
			player_input = input("\nPlayer's play:")


	def dealer_move(self):
		if not self.player.is_busted():
			print("\nDealer's Turn:")
			while True:
				print("Hand :",end="")
				self.dealer_hand.print_cards()
				dealer_value = self.dealer_hand.get_value()
				
				if dealer_value < 17:
					print("\nDealer's Play: Hit")
					new_card = self.deck.deal_card()
					print(new_card.get_rank()+" of " + new_card.get_suit())
					self.dealer_hand.add_card(new_card)
				
				elif dealer_value >= 17 and dealer_value <= 21:
					print("Dealer's Play: Stand")
					break
				
				else:
					break

	def result(self):
		dealer_val = self.dealer_hand.get_value()
		player_val = self.player_hand.get_value()

		print("\n")
		if self.player.is_busted():
			print("Player's Hand: ",end="")
			self.player_hand.print_cards()
			print("Player Busted -- Dealer Wins!!!")
			self.player.remaining_fund()
		
		elif self.player.is_blackjack() and dealer_val != 21:
			print("Player's Hand: ",end="")
			self.player_hand.print_cards()
			print("!!BLACKJACK!!")
			self.player.add_fund()


		elif dealer_val > 21:
			print("Dealer Hand: ",end="")
			self.dealer_hand.print_cards()
			print("Dealer Busted -- Player Wins!!!")
			self.player.add_fund()

		elif player_val > dealer_val:
			print("Player's Hand: ",end="")
			self.player_hand.print_cards()
			print("Dealer's Hand: ",end="")
			self.dealer_hand.print_cards()
			print("Player Win!!!")
			self.player.add_fund()

		elif player_val < dealer_val:
			print("Player's Hand: ",end="")
			self.player_hand.print_cards()
			print("Dealer's Hand: ",end="")
			self.dealer_hand.print_cards()
			print("Dealer Win!!!")
			self.player.remaining_fund()

		elif player_val == dealer_val:
			print("Player's Hand: ",end="")
			self.player_hand.print_cards()
			print("Dealer's Hand: ",end="")
			self.dealer_hand.print_cards()
			print("Points Tie.PUSH")

		else:
			pass

		print("\n")
		print("Player current Status:")
		print("Player has {0:.2f} chips\n".format(self.player.get_fund()))




