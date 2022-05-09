# Definitions
i = 0
player1 = None
player2 = None
game_is_on = True
pos = {
    "A": "a",
    "B": "b",
    "C": "c",
    "D": "d",
    "E": "e",
    "F": "f",
    "G": "g",
    "H": "h",
    "I": "i",
}


def check(A, B, C, D, E, F, G, H, I):
    # Checks if there's a winner or if it's a draw
    if A == B and B == C:
        return False
    elif D == E and E == F:
        return False
    elif G == H and H == I:
        return False
    elif A == D and D == G:
        return False
    elif B == E and E == H:
        return False
    elif C == F and F == I:
        return False
    elif A == E and E == I:
        return False
    elif C == E and E == G:
        return False
    elif A != "a" and B != "b" and C != "c" and D != "d" and E != "e" and F != "f" and G != "g" and H != "h" and I != "i":
        return None
    else:
        return True

# Checks if player 1 chooses to start with X or O
player1_chooses = input("Player 1, choose either X or O: ").capitalize()
if player1_chooses == "X":
    player1 = "X"
    player2 = "O"
    print("Player 1 is X and Player 2 is O")
elif player1_chooses == "O":
    player1 = "O"
    player2 = "X"
    print("Player 1 is O and Player 2 is X")
else:
    print("Invalid Answer. Please Try Again.")
    game_is_on = False

bg = f"""
    {pos["A"]} | {pos["B"]} | {pos["C"]}
    -----------
    {pos["D"]} | {pos["E"]} | {pos["F"]}
    -----------
    {pos["G"]} | {pos["H"]} | {pos["I"]}
"""
print(bg)

# A loop that works as long as the game is ongoing
# I used "i" to switch between player 1 and player 2
while game_is_on:
    if i % 2 == 0:
        player = player1
    else:
        player = player2
    p = input(f"Player {player} choose a letter: ").lower()
    if p == "a":
        pos["A"] = player
    elif p == "b":
        pos["B"] = player
    elif p == "c":
        pos["C"] = player
    elif p == "d":
        pos["D"] = player
    elif p == "e":
        pos["E"] = player
    elif p == "f":
        pos["F"] = player
    elif p == "g":
        pos["G"] = player
    elif p == "h":
        pos["H"] = player
    elif p == "i":
        pos["I"] = player
    else:
        print("Invalid. Try again.")
        i += 1

    bg = f"""
    {pos["A"]} | {pos["B"]} | {pos["C"]}
    -----------
    {pos["D"]} | {pos["E"]} | {pos["F"]}
    -----------
    {pos["G"]} | {pos["H"]} | {pos["I"]}
    """
    print(bg)
    game_is_on = check(pos["A"], pos["B"], pos["C"], pos["D"], pos["E"], pos["F"], pos["G"], pos["H"], pos["I"])
    if game_is_on == False:
        print(f"Player {player} won the game!")
    elif game_is_on == None:
        print("It's a draw")
    i += 1
