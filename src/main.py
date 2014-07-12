# main function to run the program

from BlackJack import BlackJack

if __name__ == '__main__':
	print("*****Welcome to BlackJack!*****")
	print("*****!!Rules!!*****")
	print("1.Options to player:Hit, Stand, Double and Split")
	print("2.Type Blackjack if your hand have Blackjack combination(21)!")
	print("3.Other rules of game is based on the description on wikipedia.")
	print("4.Detail rules used in game is described in Readme file.\n")
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
		try:
			next_round = input("Play another round(yes/no)? ").lower()
			if next_round not in ['yes','no']:
				next_round = input("Please type yes/no!!!")
		except ValueError:
			print("Not valid option.Game Quiting!!!")


		print("\n")
	print("Goodbye !\n")


