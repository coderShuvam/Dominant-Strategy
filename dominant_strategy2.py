import numpy as np

def find_dominant_strategy_row(payoff_matrix):
    """
    Finds the dominant strategy for the row player.
    Returns the index of the dominant strategy if it exists, otherwise None.
    """
    num_rows = payoff_matrix.shape[0]
    
    for i in range(num_rows):
        is_dominant = True
        for j in range(num_rows):
            if i != j:
                # Check if strategy i is better or equal to strategy j for all columns
                if not all(payoff_matrix[i, :] >= payoff_matrix[j, :]):
                    is_dominant = False
                    break
        if is_dominant:
            return i 
    
    return None  

def find_dominant_strategy_column(payoff_matrix):
    """
    Finds the dominant strategy for the column player.
    Returns the index of the dominant strategy if it exists, otherwise None.
    """
    num_cols = payoff_matrix.shape[1]
    
    for i in range(num_cols):
        is_dominant = True
        for j in range(num_cols):
            if i != j:
                if not all(payoff_matrix[:, i] <= payoff_matrix[:, j]):
                    is_dominant = False
                    break
        if is_dominant:
            return i
    
    return None 

# Example Usage
if __name__ == "__main__":
    # payoff_matrix = np.array([
    #     [4, 3],
    #     [2, 1]
    # ])
#     payoff_matrix = np.array([
#     [3, 1],
#     [2, 4]
# ])
    payoff_matrix = np.array([
    [3, 1],
    [2, 4]
])



    # Find dominant strategies for the row and column players
    dominant_row = find_dominant_strategy_row(payoff_matrix)
    dominant_col = find_dominant_strategy_column(payoff_matrix)

    # Print results
    if dominant_row is not None:
        print(f"Row Player's Dominant Strategy: Row {dominant_row}")
    else:
        print("Row Player has no dominant strategy.")

    if dominant_col is not None:
        print(f"Column Player's Dominant Strategy: Column {dominant_col}")
    else:
        print("Column Player has no dominant strategy.")
