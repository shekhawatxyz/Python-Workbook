import random

NUM_GAMES = 100000
better_to_switch = 0
print(f"Simulating {NUM_GAMES:,} games...")
for i in range(NUM_GAMES):
    car_door = random.randrange(1, 4)
    player_door = random.randrange(1, 4)
    reveal_door = random.randrange(1, 4)
    while reveal_door == player_door or reveal_door == car_door:
        reveal_door = random.randrange(1, 4)
    if player_door != car_door:
        better_to_switch = better_to_switch + 1
percent = better_to_switch / NUM_GAMES * 100
print(f"It was better to switch in {percent:.1f}% of games!")
