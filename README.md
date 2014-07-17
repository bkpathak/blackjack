BlackJack
=========

This is a Text-based Blackjack game.The game is based on the description provided in the [wikipedia](http://en.wikipedia.org/wiki/Blackjack).The objective of the game is to beat the dealer, which  can be done in the following ways:
* Get 21 points on the player's first two cards (called a blackjack), without a dealer blackjack;
* Reach a final score higher than the dealer without exceeding 21; or
* Let the dealer draw additional cards until his or her hand exceeds 21.

The game is implemented with standard 1 deck of cards.It has implementation of four standard options for player after receiving two initial cards: __Hit,Double Down , Split, Stand__.The rules for each implementation is described below:

* __Hit__: Take another card from dealer
* __Double Down__: After receiving initial two card, player can increase the bet by up to the initial betting amount placed.
* __Split__:If the player receive card with same rank initially, the player can split the card into two hand and must placed bet equal to original bet.The blackjack after split is considered as non-blackjack 21.Also double cannot be played after placed playing split.
* __Stand__:Player takes no more cards and dealer draws the card.

Following rules are implemented for the dealer in the game.

* Dealer hits until his cards total 17 or more points.
* Dealer also hits on __*soft 17*__(i.e, when the dealer initial 2 card value is 17, eg. e.g., an initial ace and six).
* Dealer never split and double down.

The player is paid according to the standard method.Player get paid __3:2__ for __BlackJack__ and __1:1__ for other win.Following rules are implemented for different scenario of the game:

* A blackjack beats any hand that is not a blackjack, even one with a value of 21.
* In the case of a tied score, known as "push" or "standoff", bets are normally returned without adjustment; however, a blackjack beats any hand that is not a blackjack, even one with a value of 21.
* An outcome of blackjack vs. blackjack results in a push.

# Running the game

Download the folder and run the main.py file containing inside the the src directory.The game is built using Pyhton 3.4.0 [GCC 4.8.2] on Ubuntu 14.04.

``` python3 main.py ```

# Sample output of program

### Sample output 1

```
*****Welcome to BlackJack!*****
*****!!Rules!!*****
1.Options to player:Hit, Stand, Double and Split
2.Other rules of game is based on the description on wikipedia.
3.Detail rules used in game is described in Readme file.

Round: 1
You have 100.00 chips.
Place your bet: 10


Player Hand: 2 of Diamonds,5 of Clubs
Dealer Hand: 8 of Spades,[Hidden Card]


Player's Turn:
Hand: 2 of Diamonds,5 of Clubs
Player's play:hit
9 of Diamonds
Hand: 2 of Diamonds,5 of Clubs,9 of Diamonds
Player's play:hit
3 of Clubs
Hand: 2 of Diamonds,5 of Clubs,9 of Diamonds,3 of Clubs
Player's play:stand

Dealer's Turn:
Hand :8 of Spades,4 of Spades

Dealer's Play: Hit
5 of Diamonds
Hand :8 of Spades,4 of Spades,5 of Diamonds
Dealer's Play: Stand


Player's Hand: 2 of Diamonds,5 of Clubs,9 of Diamonds,3 of Clubs
Dealer's Hand: 8 of Spades,4 of Spades,5 of Diamonds
Player Win!!!


Player current Status:
Player has 110.00 chips

Play another round(yes/no)? 
```

### Sample output 2 (Split case) 

```
*****Welcome to BlackJack!*****
*****!!Rules!!*****
1.Options to player:Hit, Stand, Double and Split
2.Other rules of game is based on the description on wikipedia.
3.Detail rules used in game is described in Readme file.

Round: 1
You have 100.00 chips.
Place your bet: 10


Player Hand: 8 of Diamonds,8 of Spades
Dealer Hand: 3 of Hearts,[Hidden Card]


Player's Turn:
Hand: 8 of Diamonds,8 of Spades
Player's play:split
Player's split on 8
Play Hand 1
Hand: 8 of Diamonds,10 of Hearts
Player's play:hit
2 of Diamonds
Hand: 8 of Diamonds,10 of Hearts,2 of Diamonds
Player's play:stand
Play Hand 2
Hand: 8 of Spades,9 of Diamonds
Player's play:hit
ACE of Hearts
Hand: 8 of Spades,9 of Diamonds,ACE of Hearts
Player's play:hit  
8 of Hearts

Dealer's Turn:
Hand :3 of Hearts,J of Clubs

Dealer's Play: Hit
10 of Clubs
Hand :3 of Hearts,J of Clubs,10 of Clubs


Player's Hand 1: 
Dealer Hand: 3 of Hearts,J of Clubs,10 of Clubs
Dealer Busted -- Player Wins!!!


Player's Hand 2: 
Player's Hand: 8 of Spades,9 of Diamonds,ACE of Hearts,8 of Hearts
Player Busted -- Dealer Wins!!!
Player current Status:
Player has 100.00 chips

Play another round(yes/no)? 
```
### Sample Output 3 (Double case)
```
*****Welcome to BlackJack!*****
*****!!Rules!!*****
1.Options to player:Hit, Stand, Double and Split
2.Type Blackjack if your hand have Blackjack combination(21)!
3.Other rules of game is based on the description on wikipedia.
4.Detail rules used in game is described in Readme file.

Round: 1
You have 100.00 chips.
Place your bet: 10


Player Hand: 7 of Clubs,10 of Diamonds
Dealer Hand: 4 of Diamonds,[Hidden Card]


Player's Turn:
Hand: 7 of Clubs,10 of Diamonds
Player's play:double
Enter the double bet amount: 10
ACE of Diamonds

Dealer's Turn:
Hand :4 of Diamonds,9 of Clubs

Dealer's Play: Hit
10 of Clubs
Hand :4 of Diamonds,9 of Clubs,10 of Clubs


Dealer Hand: 4 of Diamonds,9 of Clubs,10 of Clubs
Dealer Busted -- Player Wins!!!


Player current Status:
Player has 120.00 chips

Play another round(yes/no)?
```
### Sample output 4(Player BlackJack)
```
*****Welcome to BlackJack!*****
*****!!Rules!!*****
1.Options to player:Hit, Stand, Double and Split
2.Other rules of game is based on the description on wikipedia.
3.Detail rules used in game is described in Readme file.

Round: 1
You have 100.00 chips.
Place your bet: 10


Player Hand: K of Clubs,ACE of Clubs
Dealer Hand: 4 of Spades,[Hidden Card]

Dealer's Turn:
Hand :4 of Spades,ACE of Spades

Dealer's Play: Hit
3 of Hearts
Hand :4 of Spades,ACE of Spades,3 of Hearts
Dealer's Play: Stand


Player's Hand: K of Clubs,ACE of Clubs
!!BLACKJACK!!
Dealer's Hand: 4 of Spades,ACE of Spades,3 of Hearts


Player current Status:
Player has 115.00 chips

Play another round(yes/no)? 
```
