# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:51:51 2020

@author: Caleb
"""

import random

deck = {
        # 2s
        "2 of Clubs" : 2,
        "2 of Hearts" : 2,
        "2 of Diamonds" : 2,
        "2 of Spades" : 2,
        # 3s
        "3 of Clubs" : 3,
        "3 of Hearts" : 3,
        "3 of Diamonds" : 3,
        "3 of Spades" : 3,
        # 4s
        "4 of Clubs" : 4,
        "4 of Hearts" : 4,
        "4 of Diamonds" : 4,
        "4 of Spades" : 4,
        # 5s
        "5 of Clubs" : 5,
        "5 of Hearts" : 5,
        "5 of Diamonds" : 5,
        "5 of Spades" : 5,
        # 6s
        "6 of Clubs" : 6,
        "6 of Hearts" : 6,
        "6 of Diamonds" : 6,
        "6 of Spades" : 6,
        # 7s
        "7 of Clubs" : 7,
        "7 of Hearts" : 7,
        "7 of Diamonds" : 7,
        "7 of Spades" : 7,
        # 8s
        "8 of Clubs" : 8,
        "8 of Hearts" : 8,
        "8 of Diamonds" : 8,
        "8 of Spades" : 8,
        # 9s
        "9 of Clubs" : 9,
        "9 of Hearts" : 9,
        "9 of Diamonds" : 9,
        "9 of Spades" : 9,
        # 10s
        "10 of Clubs" : 10,
        "10 of Hearts" : 10,
        "10 of Diamonds" : 10,
        "10 of Spades" : 10,
        # Jacks
        "Jack of Clubs" : 10,
        "Jack of Hearts" : 10,
        "Jack of Diamonds" : 10,
        "Jack of Spades" : 10,
        # Queens
        "Queen of Clubs" : 10,
        "Queen of Hearts" : 10,
        "Queen of Diamonds" : 10,
        "Queen of Spades" : 10,
        # Kings
        "Kings of Clubs" : 10,
        "Kings of Hearts" : 10,
        "Kings of Diamonds" : 10,
        "Kings of Spades" : 10,
        # Aces
        "Ace of Clubs" : 11,
        "Ace of Hearts" : 11,
        "Ace of Diamonds" : 11,
        "Ace of Spades" : 11,
        }
deck_list = [
    #2s
    "2 of Clubs",
    "2 of Hearts",
    "2 of Diamonds", 
    "2 of Spades", 
    #3s
    "3 of Clubs", 
    "3 of Hearts", 
    "3 of Diamonds", 
    "3 of Spades", 
    # 4s
    "4 of Clubs" 
    "4 of Hearts" 
    "4 of Diamonds"
    "4 of Spades" 
    # 5s
    "5 of Clubs",
    "5 of Hearts",
    "5 of Diamonds", 
    "5 of Spades" ,
    # 6s
    "6 of Clubs",
    "6 of Hearts",
    "6 of Diamonds",
    "6 of Spades",
    # 7s
    "7 of Clubs",
    "7 of Hearts",
    "7 of Diamonds",
    "7 of Spades",
    # 8s
    "8 of Clubs",
    "8 of Hearts",
    "8 of Diamonds",
    "8 of Spades",
    # 9s
    "9 of Clubs",
    "9 of Hearts",
    "9 of Diamonds",
    "9 of Spades",
    # 10s
    "10 of Clubs",
    "10 of Hearts",
    "10 of Diamonds",
    "10 of Spades",
    # Jacks
    "Jack of Clubs",
    "Jack of Hearts",
    "Jack of Diamonds",
    "Jack of Spades",
    # Queens
    "Queen of Clubs",
    "Queen of Hearts",
    "Queen of Diamonds",
    "Queen of Spades",
    # Kings
    "Kings of Clubs",
    "Kings of Hearts",
    "Kings of Diamonds",
    "Kings of Spades",
    # Aces
    "Ace of Clubs",
    "Ace of Hearts",
    "Ace of Diamonds",
    "Ace of Spades",
    ]

def deal_first_cards(num_players, deck_list):
    player_hands = []
    for i in range(num_players):
        player_hand = []
        for y in range(2):
            drawn_card = random.choice(deck_list)
            player_hand.append(drawn_card)
            deck_list.remove(drawn_card)
        player_hands.append(player_hand)
    return player_hands
def display_hand(hand):
    hand_string = ""
    for item in hand:
        if item != hand[-1]:
            hand_string += item + ", "
        if item == hand[-1]:
            hand_string += "and " + item
    return hand_string
def calculate_hand(hand, deck):
    hand_score = 0
    for item in hand:
        hand_score += deck[item]
    return hand_score

    
num_players = int(input("How many people are playing (2-4)? "))
print ("")
#True means "Hit Me", False indicates "Bust" or "Pass"
player_statues = []
for x in range(num_players):
    player_statues.append(True)
#Deal the First Cards
player_hands = deal_first_cards(num_players, deck_list)
#Playing the Game 
for i in range(1):
    tracker = 0
    for z in range(num_players):
        hand = player_hands[tracker]
        hand_string = display_hand(hand)
        hand_score = calculate_hand(hand, deck)
        print ("Player " + str(tracker + 1) + "'s turn: ")
        print ("This is your hand: \n" + hand_string)
        print ("This hand is worth " + str(hand_score) +" points. ")
        print ("")
        tracker += 1