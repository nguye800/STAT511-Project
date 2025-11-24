import random

# part 1a
# samples = 100
# total = 0
# for i in range(samples):
#     roll1 = random.randint(1,6)
#     roll2 = random.randint(1,6)
#     if roll1+roll2 == 12 or abs(roll1-roll2) == 4:
#         total += 1

# print("sample probabilities")
# print("probability of getting a total of 12 or absolute difference of 4: ", total / samples)
# print("True probability: ", 5 / 36)

# part 1b
# samples = 100
# total = 0
# for i in range(samples):
#     roll1 = random.randint(1,6)
#     roll2 = random.randint(1,6)
#     if roll1 == 6 or roll2 == 6 or abs(roll1-roll2) == 4:
#         total += 1

# print("sample probabilities")
# print("probability of getting a 6 or absolute difference of 4: ", total / samples)
# print("True probability: ", 13 / 36)

# part 2a
# samples = 100
# total = 0
# for i in range(samples):
#     card1 = random.randint(1,13)
#     card2 = random.randint(1,13)
#     card3 = random.randint(1,13)
#     if card1 <= 10 and card2 <= 10 and card3 <= 10:
#         total += 1

# print("probability that all 3 cards aren't faces: ", total / samples)
# print("True probability: ", (10/13)**3)

# part 2b
# samples = 100
# total = 0
# for i in range(samples):
#     drawcards = set()
#     card1 = random.randint(1,13)
#     drawcards.add(card1)

#     card2 = random.randint(1,13)
#     while card2 in drawcards:
#         card2 = random.randint(1,13)
#     drawcards.add(card2)

#     card3 = random.randint(1,13)
#     while card3 in drawcards:
#         card3 = random.randint(1,13)

#     if card1 <= 10 and card2 <= 10 and card3 <= 10:
#         total += 1

# print("probability that all 3 cards aren't faces (without replacement): ", total / samples)
# print("True probability: ", (10/13)*(9/12)*(8/11))

# part 2c
# samples = 100
# total = 0
# red = [0]*26
# black = [1]*26
# cards = red + black
# for i in range(samples):
#     card1 = random.randint(0, len(cards)-1)
#     card2 = random.randint(0, len(cards)-1)
#     card3 = random.randint(0, len(cards)-1)

#     if cards[card1] == 0 and cards[card2] == 0 and cards[card3] == 0:
#         total += 1    

# print("probability that all 3 cards are red: ", total / samples)
# print("True probability: ", (26/52)**3)

# part 3a
samples = 100
total = 0 # heads 0, tails 1
for i in range(samples):
    flip = random.randint(0,1)
    if flip == 0:
        total += 1
print("probability of heads: ", total / samples)
print("true probability: ", 0.5)

# 3b
samples = 100
total = 0 # heads 0, tails 1
for i in range(samples):
    flip1 = random.randint(0,1)
    flip2 = random.randint(0,1)
    if flip1 == 0 or flip2 == 0:
        total += 1
print("probability of at least one heads: ", total / samples)
print("true probability: ", 0.75)