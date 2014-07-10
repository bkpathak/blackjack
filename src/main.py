# main function to run the program

from BlackJack import BlackJack

if __name__ == '__main__':
	print("Welcome to BlackJack!")
	print("!!Rules!!")
	print("Options to player:Hit or Stand")
	print("Type Blackjack if your hand have Blackjack combination(21)!")
	round = 1
	next_round = 'yes'
	bj = BlackJack()
	while next_round == 'yes':
		print("Round:",round)
		bj.place_bet()
		bj.player_move()
		bj.dealer_move()
		bj.result()
		player_choice = input("Play another round(yes/no)? ")

	print("Goodbye !")


