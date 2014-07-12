blackjack
=========

This is a Text-based Blackjack game.The game is based on the description provided in the [wikipedia](http://en.wikipedia.org/wiki/Blackjack).The objective of the game is to beat the dealer, which  can be done in the following ways:
*Get 21 points on the player's first two cards (called a blackjack), without a dealer blackjack;
*Reach a final score higher than the dealer without exceeding 21; or
*Let the dealer draw additional cards until his or her hand exceeds 21.

It has implementation of four standard options for player after receiving two initial cards: __Hit,Double Down , Split, Stand__.The rules for each implementation is described below:

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

