import random

# Game data
supply_piles = {
    "Copper": {"cost": 0, "stack": 46, "type": "treasure"},
    "Estate": {"cost": 2, "stack": 8, "type": "victory"},
    "Province": {"cost": 8, "stack": 8, "type": "victory"},
}

kingdom_cards = ["Village", "Smithy"]

# Player data structure
class Player:
    def __init__(self):
        self.deck = ["Copper", "Copper", "Estate", "Estate", "Estate"]  # Initial deck
        self.hand = []
        self.discard = []
        self.actions = 1
        self.buys = 1
        self.coins = 0


# Core game functions
def initialize_supply():
    # Set up supply piles
    for pile in supply_piles.values():
        pile["start_stack"] = pile["stack"]

    # Add kingdom card piles
    for kingdom_card in kingdom_cards:
        new_pile(kingdom_card)


def new_pile(card):
    supply_piles[card] = {"cost": 5, "stack": 10, "type": "action"}


def current_player():
    # For simplicity, let's assume there are only two players
    return random.choice([player1, player2])


def shuffle(deck):
    random.shuffle(deck)


def draw_card(player):
    if len(player.deck) == 0:
        shuffle(player.discard)
        player.deck = player.discard
        player.discard = []

    player.hand.append(player.deck.pop())


def play_actions(player):
    # For simplicity, let's just play the first action card in hand if available
    action_cards = [card for card in player.hand if supply_piles[card]["type"] == "action"]

    if action_cards:
        print(f"Available action cards: {', '.join(action_cards)}")
        card_to_play = input("Choose an action card to play: ")

        if card_to_play in action_cards:
            play_action(player, card_to_play)
        else:
            print("Invalid choice. Try again.")
            play_actions(player)


def play_action(player, card):
    if card == "Village":
        draw_card(player)
        player.actions += 2


def buy_cards(player):
    affordable_cards = [card for card in supply_piles if supply_piles[card]["cost"] <= player.coins]

    if affordable_cards and player.buys > 0:
        print(f"Available cards to buy: {', '.join(affordable_cards)}")
        card_to_buy = input("Choose a card to buy: ")

        if card_to_buy in affordable_cards:
            buy_card(player, card_to_buy)
        else:
            print("Invalid choice. Try again.")
            buy_cards(player)


def buy_card(player, card):
    if supply_piles[card]["stack"] > 0:
        player.discard.append(card)
        supply_piles[card]["stack"] -= 1
        player.coins -= supply_piles[card]["cost"]
        player.buys -= 1
        print(f"Bought {card}!")
    else:
        print("Sorry, that pile is empty. Try again.")


def cleanup(player):
    # Move hand and played cards to discard, draw new hand
    player.discard.extend(player.hand)
    player.hand = []
    draw_card(player)
    player.actions = 1
    player.buys = 1
    player.coins = 0


# Main game loop
player1 = Player()
player2 = Player()

initialize_supply()

game_end = False
turns = 0

while not game_end:
    player = current_player()

    print(f"\n--- Player {player} Turn ---")

    # Play full turn
    player.actions = 1
    player.buys = 1
    player.coins = 0

    draw_card(player)  # Draw initial hand

    # Actions phase
    print("\n--- Actions Phase ---")
    play_actions(player)

    # Buy phase
    print("\n--- Buy Phase ---")
    buy_cards(player)

    # Cleanup phase
    print("\n--- Cleanup Phase ---")
    cleanup(player)

    # Check end game conditions
    if supply_piles["Province"]["stack"] == 0 or turns >= 20:
        game_end = True

    turns += 1

# Tally scores
score_player1 = len([card for card in player1.deck + player1.hand + player1.discard if card == "Estate"])
score_player2 = len([card for card in player2.deck + player2.hand + player2.discard if card == "Estate"])

print("\nGame over!")
print("Player 1 score:", score_player1)
print("Player 2 score:", score_player2)
