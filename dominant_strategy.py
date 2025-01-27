# Payoff matrix for Player 1
payoff_matrix = {
    "X": {"A": 3, "B": 2},
    "Y": {"A": 4, "B": 1}
}

def find_dominant_strategy(payoff_matrix):
    strategies = list(payoff_matrix.keys())
    dominant_strategy = None

    for strategy in strategies:
        is_dominant = True
        for other_strategy in strategies:
            if strategy != other_strategy:
                for opponent_move in payoff_matrix[strategy]:
                    if payoff_matrix[strategy][opponent_move] < payoff_matrix[other_strategy][opponent_move]:
                        is_dominant = False
                        break
            if not is_dominant:
                break

        if is_dominant:
            dominant_strategy = strategy
            break

    return dominant_strategy

dominant = find_dominant_strategy(payoff_matrix)
if dominant:
    print(f"The dominant strategy for Player 1 is: {dominant}")
else:
    print("No dominant strategy exists for Player 1.")
