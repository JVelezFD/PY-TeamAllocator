import random

print("Welcome to Team Allocator!")

players = [
    "Martin","Craig","Sue",
    "Claire", "Dave", "Alice",
    "Lucianna", "Harry", "Jack",
    "Rose", "Lexi", "Maria",
    "Thomas", "James", "William",
    "Ada", "Grace", "Jean",
    "Marissa", "Alan",
];

random.shuffle(players);

# Creating First Team
team1 = players[:len(players)//2];

# Selecting Team 1 captain

print("Team 1 captain: " + random.choice(team1));

print("Team 1:")
for player in team1:
    print(player);
    
    