import random
#print("♠♣♢♡")

talia=[]

figury=["A","K","Q","W"]

kolor = ["♠", "♣", "♢", "♡"]

wartosci = {"9": 0, "10": 10, "J": 2, "Q": 3, "K": 4, "A": 11}

wygrana = 1000

num_players=2

for f in figury[1:]:
    for k in kolor:
        talia.append(f + k)

for i in range(1,10):
    for k in kolor:
        talia.append(str(i) + k)
def Tasowanie(talia):
    random.shuffle(talia)

def Rozdanie(talia, num_players):
    hands = [[] for i in range(num_players)]
    for i in range(3):
        for j in range(num_players):
            card = talia.pop()
            hands[j].append(card)
    return hands

# Funkcja do obliczania punktów za daną rękę
def calculate_score(hand):
    score = 0
    for card in hand:
        value = card[:-1]
        score += wartosci[value]
    return score

# Funkcja do sprawdzania, czy dana ręka zawiera podaną kombinację
def has_combination(hand, combination):
    for card in combination:
        if card not in hand:
            return False
    return True

# Funkcja do wyświetlania ręki
def display_hand(hand):
    hand_str = ""
    for card in hand:
        hand_str += card + " "
    return hand_str

# Tasujemy talie i rozdajemy karty
Tasowanie(talia)
hands = Rozdanie(talia, 2)

# Początkowe punkty graczy
scores = [0, 0]

# Wartość pierwszej licytacji
bid = 100

# Gracz, który wygrał licytację
bid_winner = None

# Licytujemy
while bid_winner == None:
    print("Gracz 1, Twój aktualny budżet to:", scores[0])
    print("Gracz 2, Twój aktualny budżet to:", scores[1])
    print("Aktualna licytacja to:", bid)
    bid1 = int(input("Gracz 1, podaj swoją ofertę: "))
    bid2 = int(input("Gracz 2, podaj swoją ofertę: "))
    if bid1 > bid:
        bid = bid1
        bid_winner = 0
    elif bid2 > bid:
        bid = bid2
        bid_winner = 1
    elif bid1 == bid2:
        print("Licytacja zakończona remisem. Powtórz licytację.")

print("Licytacja wygrana przez gracza", bid_winner+1, "za", bid, "punktów.")
points[bid_winner] += bid // 2

for i in range(num_players):
    if i != bid_winner:
        points[i] -= 100
for i in range(num_players):
    if points[i] >= 1000:
        print("Gracz", i+1, "wygrał z wynikiem", points[i], "punktów!")
        game_over = True
        break

if not game_over:
    print("Aktualne wyniki:")
for i in range(num_players):
    print("Gracz", i+1, "ma", points[i], "punktów.")
for i in range(0,10):
    print(talia[i])






















"""
for i in range(1,4):
    j = figury[i] + "♠"
    talia.append(j)

for i in range(1,10):
    j = str(i)
    z = j + "♠"
    talia.append(z)
for i in range(1,10):
    j = str(i)
    z = j + "♣"
    talia.append(z)
for i in range(1,10):
    j = str(i)
    z = j + "♢"
    talia.append(z)
for i in range(1,10):
    j = str(i)
    z = j + "♡"
    talia.append(z)
"""