import random

# Karty
CARD_RANKS = ["As", "Król", "Dama", "Walet", "10", "9", "8", "7"]
CARD_SUITS = ["Pik", "Kier", "Trefl", "Karo"]

# Tworzenie talii
deck = []
for suit in CARD_SUITS:
    for rank in CARD_RANKS:
        card = rank + " " + suit
        deck.append(card)

# Losowanie rozdania
random.shuffle(deck)
hand1 = deck[:10]
hand2 = deck[10:20]
hand3 = deck[20:30]
hand4 = deck[30:40]
trump_card = deck[40]

# Wybór koloru atutowego
trump_suit = trump_card.split()[1]
print("Kolor atutowy to:", trump_suit)

# Licytacja
bid_winner = 0
bid = 0
for i in range(4):
    current_bid = int(input("Gracz " + str(i+1) + ", podaj swoją licytację: "))
    if current_bid > bid:
        bid = current_bid
        bid_winner = i

print("Licytacja wygrana przez gracza", bid_winner+1, "za", bid, "punktów.")

# Gracz, który wygrał licytację
current_player = bid_winner

# Wist
tricks_won = [0, 0, 0, 0]
for i in range(10):
    # Wyświetlenie wistu
    print("Gracz", current_player+1, "wybiera kartę.")

    # Wybór karty
    card = input("Podaj kartę (format: wartość kolor): ")
    while card not in hand1 and card not in hand2 and card not in hand3 and card not in hand4:
        print("Nie masz tej karty. Spróbuj ponownie.")
        card = input("Podaj kartę (format: wartość kolor): ")

    # Usunięcie karty z ręki gracza
    if card in hand1:
        hand1.remove(card)
    elif card in hand2:
        hand2.remove(card)
    elif card in hand3:
        hand3.remove(card)
    elif card in hand4:
        hand4.remove(card)

    # Dodanie punktów za wygrany wist
    current_trick_points = 0
    current_trick_points += CARD_RANKS.index(card.split()[0]) + 1
    if card.split()[1] == trump_suit:
        current_trick_points += 10
    tricks_won[current_player] += current_trick_points

    # Przejście do następnego gracza
    current_player = (current_player + 1) % 4

# Podsumowanie wyników
print("Gra zakończona!")
print("Wyniki:")
for i in range(4):
    print("Gracz", i+1, "wygrał", tricks_won[i], "punktów.")
