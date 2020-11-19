import random
import sys
class Create_deck:
    def __init__(self, suits, ranks):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = suit + "-" + rank
                self.deck.append(card)

    def shuffle_deck(self):
        random.shuffle(self.deck)
        return self.deck

    def split_and_deal_cards(self):
        self.cards_dealt = {}
        player1_cards = []
        player2_cards = []

        for i, j in enumerate(self.deck):
            if i % 2 == 0:
                player1_cards.append(j)
            else:
                player2_cards.append(j)

        self.cards_dealt["player1_cards"] = player1_cards
        self.cards_dealt["player2_cards"] = player2_cards
        return self.cards_dealt

class Player():
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

class Hand(Player):
    def add_cards(self, add_this_cards):
        self.cards.append(add_this_cards)

    def remove_cards(self):
        return self.cards.pop(0)

    def won_the_war(self, player1war, player2war):
        for _ in range(len(player1war)):
            self.cards.append(player1war.pop(0))
            self.cards.append(player2war.pop(0))
    
def at_war(war, player1war, player2war, count, double_war):
    print("count of war: ",count)
    print(double_war)
    while war:
        if len(player_1.cards) >= 4:
            for _ in range(0, 4):
                player1war.append(player_1.remove_cards())

        else:
            print(f"As {player_1.name} doesn't have enough Cards to deploy for war!!")
            winner = player_2.name
            print(f"{winner} Wins the WAR!! All cards go to {winner}.\n")
            war = False
            sys.exit(f"Winner is {winner}")

        if len(player_2.cards) >= 4:
            for _ in range(0, 4):
                player2war.append(player_2.remove_cards())

        else:
            print(f"As {player_2.name} doesn't have enough Cards to deploy for war!!")
            winner = player_1.name
            print(f"{winner} Wins the WAR!! All cards go to {winner}.\n")
            war = False
            sys.exit(f"Winner is {winner}")

        print(f"{player_1.name}:  {player1war}")
        print(f"{player_2.name}:  {player2war}\n")

        print(f"{player_1.name}'s card: {player1war[-1]}")
        print(f"{player_2.name}'s card: {player2war[-1]}\n")

        if ranks.index(player1war[-1].split("-")[1]) > ranks.index(player2war[-1].split("-")[1]):
            war = False
            winner = player_1.name
            print(f"{winner} Wins the WAR!! All cards go to {winner}.\n")
            player_1.won_the_war(player1war, player2war)

        elif ranks.index(player1war[-1].split("-")[1]) == ranks.index(player2war[-1].split("-")[1]):
            print("\nIt's a war Again!!\n")
            count = count+1
            double_war = double_war+1
            war = True
            continue

        else:
            war = False
            winner = player_2.name
            print(f"{winner} Wins the WAR!! All cards go to {winner}.\n")
            player_2.won_the_war(player1war, player2war)

    return winner

suits = ["H", "D", "S", "C"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

player1Name = input("Enter the Name of player 1: ")
player2Name = input("Enter the Name of player 2: ")
game = Create_deck(suits, ranks)

print(f"Player 1: {player1Name}")
print(f"And")
print(f"Player 2: {player2Name}")
game.shuffle_deck()

cont = input("Shall We begin ? (Y/N)")

if cont[0].lower() == "y":
    player_1 = Hand(player1Name, game.split_and_deal_cards()["player1_cards"])
    player_2 = Hand(player2Name, game.split_and_deal_cards()["player2_cards"])

print(f"{player_1.name}'s cards: {player_1.cards}")
print(f"{player_2.name}'s cards: {player_2.cards}")

war = False
double_war = 0
winner = None
count = 0
total_rounds_played = 0
while len(player_1.cards) > 0 and len(player_2.cards) > 0:
    total_rounds_played = total_rounds_played + 1
    print(f"{player_1.name} curruntly has {len(player_1.cards)} card(s)")
    print(f"{player_2.name} currently has {len(player_2.cards)} card(s)\n")

    player1_card = player_1.remove_cards()
    player2_card = player_2.remove_cards()

    print(f"{player_1.name}'s card: ", player1_card)
    print(f"{player_2.name}'s card: ", player2_card)

    if ranks.index(player1_card.split("-")[1]) > ranks.index(player2_card.split("-")[1]):
        print(f"{player_1.name} wins the round!!\n")
        war = False
        winner = player_1.name
        player_1.add_cards(player1_card)
        player_1.add_cards(player2_card)

    elif ranks.index(player1_card.split("-")[1]) == ranks.index(player2_card.split("-")[1]):
        count = count+1
        print("\nIt's a war!!\n")
        war = True
        player1war = [player1_card]
        player2war = [player2_card]
        winner = at_war(war, player1war,player2war, count, double_war)

    else:
        print(f"{player_2.name} wins the round!!\n")
        war = False
        winner = player_2.name
        player_2.add_cards(player1_card)
        player_2.add_cards(player2_card)

    # cont = input("Do You wish to Continue? (Y/N)")
    # if cont[0].lower() == 'y':
    #     continue
    # else:
    #     break
    
print(f"Total count of war: {count}")
print(f"Double war hapened: {double_war}")
print(f"total_rounds_played: {total_rounds_played}")
print(f"And the winner is {winner} !!")
