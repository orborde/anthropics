# TODO: This only allows the agent to make bets at 1:1 odds. That
# might not be the best way to set this up.
#
# TODO: Did I accidentally encode SIA right into this simulation? If
# so, how would we model SSA?

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

# Function that implements some proposed betting strategy (i.e. the
# agent).
def play(room_number):
    return guess, bet


# Run one round of the game and return the betting outcome.
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


