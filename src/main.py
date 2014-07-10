# main function to run the program

from BlackJack import BlackJack

if __name__ == '__main__':
	print("Welcome to BlackJack!")
	print("!!Rules!!")
	print("1.Options to player:Hit or Stand")
	print("2.Type Blackjack if your hand have Blackjack combination(21)!\n")
	round = 1
	next_round = 'yes'
	while next_round == 'yes':
		print("Round:",round)
		bj = BlackJack()
		bj.place_bet()
		bj.player_move()
		bj.dealer_move()
		bj.result()
		round += 1
		next_round = input("Play another round(yes/no)? ")
		print("\n")
	print("Goodbye !\n")


