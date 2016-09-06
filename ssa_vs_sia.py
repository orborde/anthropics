import random

H="HEADS"
HEADSWORLD=range(1, 10+1)
T="TAILS"
TAILSWORLD=range(1, 1000+1)

WORLDS = {
    H : HEADSWORLD,
    T : TAILSWORLD
}

FIRST_TEN = set(range(1, 10+1))

def play(room_number):
    return guess, bet


def one_game():
    GODS_TOSS = random.choice([H, T])

    world = WORLDS[GODS_TOSS]
    room_number = random.choice(world)

    # We only care about the worlds in which we happen to be in the
    # first 10.
    if room_number not in FIRST_TEN:
        return None

    guess, bet = play(room_number)
    if bet == GODS_TOSS:
        return +bet
    else:
        return -bet


