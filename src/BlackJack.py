import sys

from Player import Player
from Deck import Deck
from Hand import Hand

class BlackJack:
	'''
	Creates and manages the game.Check for the condition of the game whether player wins, loss or busted.
	'''
	def __init__(self):
		self.moves = ["hit","stand","double","split"]
		self.deck = Deck()
		self.player = Player()
		self.player_hand = []
		self.player_hand.append(Hand()) 
		self.dealer_hand = Hand()
	
	
	def place_bet(self):
		if self.player.get_fund() < 1:
			print("Sorry,not enough fund to play. Start a new game.")
			input()
			sys.exit(0)

		print("You have {0:.2f}".format(self.player.get_fund())+" chips.")
		
		while True:
			try:
				bet = int(input("Place your bet: "))
				if bet < 1:
					bet = int(input("Bet must be at least 1 chip.Try Again!!! "))
				elif self.player.get_fund() < bet:
					bet = int(input("Not enough chips.Try Again!!! "))
				else:
					break
		
			except ValueError:
				print("Doesn't looks like valid bet.Try Again!!!")

		self.player.current_bet(bet)

	
	def play_hit(self,current_hand, hand_index = 0):
				new_card = self.deck.deal_card()
				current_hand.add_card(new_card)
				print(new_card.get_rank()+" of " + new_card.get_suit())
				
				if current_hand.get_value() > 21:
					self.player.busted[hand_index] = True

	
	def play_double(self):
		if len(self.player_hand[0].hand) == 2 and not self.player.is_split(): 		#Allowed only in initial hands
			try:
				double_bet = int(input("Enter the double bet amount: "))
			except ValueError:
				double_bet = int(input("Please enter the valid integer positive number: "))

			if double_bet <= self.player.current_fund() and double_bet <= self.player.bet[0]:
				self.player.current_bet(double_bet)
				new_card = self.deck.deal_card()
				self.player_hand[0].add_card(new_card)
				print(new_card.get_rank()+" of " + new_card.get_suit())
				
				if self.player_hand[0].get_value() > 21:
					self.player.busted[0] = True
				elif self.player_hand[0].get_value == 21:
					self.player.blackjack = True
				else:
					pass
	

			else:
				print("You should have enough chips and the double cannot be more then 100% of original bet.Try Again!!")
				
		else:
			print("You can only Double Down initially when not playing split.Try other move!!")

	
	def play_split(self):
		hand_cards = self.player_hand[0].get_hand()
		
		if len(hand_cards) == 2 and hand_cards[0].get_rank() == hand_cards[1].get_rank():
			if self.player.get_bet() <= self.player.current_fund():
				self.player.split = True
				self.player_hand.append(Hand())  # create new hand to store split hand
				print("Player's split on " + str(hand_cards[0].get_rank()))
				remove_card = self.player_hand[0].remove_card()
				self.player.current_bet(self.player.get_bet())
				self.player_hand[1].add_card(remove_card)
				for i in range(0,2):
					print("Play Hand",i)
					self.player_hand[i].add_card(self.deck.deal_card())
					while True:
						print("Hand: ",end="")
						self.player_hand[i].print_cards()	
						player_input = input("Player's play:").lower()
						if player_input not in ["hit","stand"]:
							print("Only Hit and Stand is valid after splitting.")
							player_input = input("Enter your play :").lower()
						elif player_input == "stand":
							break
						else:
							pass

						self.play_hit(self.player_hand[i],i)
						
						if self.player.is_busted(i):
							break


				
			else:
				print("\nNot enough fund to split.Try other move!!!")
				
		else:
			print("\nSplitting is only allowed on initial hand when cards rank are equal.")
	

	def player_move(self):

		self.player_hand[0].add_card(self.deck.deal_card())
		self.dealer_hand.add_card(self.deck.deal_card())
		self.player_hand[0].add_card(self.deck.deal_card())
		self.dealer_hand.add_card(self.deck.deal_card())
		print("\n")
		print("Player Hand: ",end="")
		self.player_hand[0].print_cards()
		print("Dealer Hand: ",end="")
		self.dealer_hand.print_dealer_initial_hand()

		if self.player_hand[0].get_value() == 21:
			self.player.blackjack = True
			return

		print("\n\nPlayer's Turn:")
		
		while True:
			print("Hand: ",end="")
			self.player_hand[0].print_cards()			
			player_input = input("Player's play:").lower()
			if player_input not in self.moves:
				print("Enter valid moves: "+",".join(self.moves))

			if player_input == 'hit':
				self.play_hit(self.player_hand[0])
				if self.player.is_busted():
					break


			elif player_input == 'double':   # Double is not allowed after split
				self.play_double()
			
			elif player_input == 'split':
				if not self.player.is_split():      # Split is not allowed in the split hand itself.
					self.play_split()
					break
							
				else:
					print("\nSplitting is only allowed on initial hand when cards are equal.!!!")
			
			else:
				break

			
			


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

				# Dealer Hits on soft 17
				elif len(self.dealer_hand.hand) == 2 and dealer_value == 17:
					print("\nDealer's Play: Hit on Soft 17")
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
		player_val = []
		player_val.append(self.player_hand[0].get_value())
		dealer_blackjack = False
		if len(self.dealer_hand.hand) == 2 and dealer_val == 21:
			dealer_blackjack = True

		for i in range(0,2):
			print("\n")
			if i == 0 and self.player.is_split():
				print("Player's Hand 1: ")
			elif i == 1 and not self.player.is_split():
				break

			elif i == 1 and self.player.is_split():
				print("Player's Hand 2: ")
				player_val.append(self.player_hand[i].get_value())

			else:
				pass


			if self.player.is_busted(i):
				print("Player's Hand: ",end="")
				self.player_hand[i].print_cards()
				print("Player Busted -- Dealer Wins!!!")
				self.player.remaining_fund()
		
			elif self.player.is_blackjack() and not dealer_blackjack:
				print("Player's Hand: ",end="")
				self.player_hand[i].print_cards()
				print("!!BLACKJACK!!")
				print("Dealer's Hand: ",end="")
				self.dealer_hand.print_cards()
				if dealer_val > 21:
					print("Dealer Busted!!")

				self.player.add_fund()


			elif dealer_val > 21:
				print("Dealer Hand: ",end="")
				self.dealer_hand.print_cards()
				print("Dealer Busted -- Player Wins!!!")
				self.player.add_fund()

			elif player_val[i] > dealer_val:
				print("Player's Hand: ",end="")
				self.player_hand[i].print_cards()
				print("Dealer's Hand: ",end="")
				self.dealer_hand.print_cards()
				print("Player Win!!!")
				self.player.add_fund()

			
			elif player_val[i] == dealer_val and not dealer_blackjack :
				print("Player's Hand: ",end="")
				self.player_hand[i].print_cards()
				print("Dealer's Hand: ",end="")
				self.dealer_hand.print_cards()
				print("Points Tie.PUSH")

			else:
				print("Player's Hand: ",end="")
				self.player_hand[i].print_cards()
				print("Dealer's Hand: ",end="")
				self.dealer_hand.print_cards()
				print("Dealer Win!!!",end="")
				if dealer_blackjack:
					print("Dealer's BLACKJACK")
				self.player.remaining_fund()

		print("Player current Status:")
		print("Player has {0:.2f} chips\n".format(self.player.get_fund()))
