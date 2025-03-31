import numpy as np
import random
import sys


def find_pure_nash_equilibria(payoff_matrix_1, payoff_matrix_2, positive_only=False):
    """
    Find all pure Nash Equilibria in a 2-player normal-form game.

    Args:
        payoff_matrix_1: A matrix with player 1's payoffs
        payoff_matrix_2: A matrix with player 2's payoffs

    Returns:
        A list of tuples with the Nash Equilibria coordinates (i, j)
    """
    num_strategies_1 = len(payoff_matrix_1)
    num_strategies_2 = len(payoff_matrix_1[0])

    nash_equilibria = []

    # Check each strategy profile (i, j)
    for i in range(num_strategies_1):
        for j in range(num_strategies_2):
            # Check if this is a Nash Equilibrium

            # Is this the best response for player 1 given player 2's strategy j?
            best_response_1 = True
            for i_alt in range(num_strategies_1):
                if payoff_matrix_1[i_alt][j] > payoff_matrix_1[i][j]:
                    best_response_1 = False
                    break

            # Is this the best response for player 2 given player 1's strategy i?
            best_response_2 = True
            for j_alt in range(num_strategies_2):
                if payoff_matrix_2[i][j_alt] > payoff_matrix_2[i][j]:
                    best_response_2 = False
                    break

            # If both conditions are met, it's a Nash Equilibrium
            if best_response_1 and best_response_2:
                nash_equilibria.append((i, j))

    return nash_equilibria


def get_integer_input(prompt):
    """Get an integer input from the user with validation."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a integer.")


def get_yes_no_input(prompt):
    """Get a yes/no input from the user."""
    while True:
        response = input(prompt).lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please answer 'yes' or 'no'.")


def main():
    # Get user inputs
    print("Nash Equilibrium Finder for 2-Player Normal Form Games")
    print("----------------------------------------------------")
    print()

    num_strategies_1 = get_integer_input("Enter number of strategies for player 1: ", positive_only=True)
    num_strategies_2 = get_integer_input("Enter number of strategies for player 2: ", positive_only=True)

    # Initialize payoff matrices
    payoff_matrix_1 = [[0 for _ in range(num_strategies_2)] for _ in range(num_strategies_1)]
    payoff_matrix_2 = [[0 for _ in range(num_strategies_2)] for _ in range(num_strategies_1)]

    # Determine if payoffs should be entered manually or generated randomly
    generate_random = get_yes_no_input("Generate random payoffs? (yes/no): ")

    if generate_random:
        # Generate random payoffs
        for i in range(num_strategies_1):
            for j in range(num_strategies_2):
                payoff_matrix_1[i][j] = random.randint(-10, 10)
                payoff_matrix_2[i][j] = random.randint(-10, 10)
    else:
        # Get payoffs manually
        print("\nEnter payoffs for each strategy profile (i, j):")
        for i in range(num_strategies_1):
            for j in range(num_strategies_2):
                print(f"\nStrategy profile: Player 1 uses strategy {i + 1}, Player 2 uses strategy {j + 1}")
                payoff_matrix_1[i][j] = get_integer_input(f"Payoff for Player 1: ")
                payoff_matrix_2[i][j] = get_integer_input(f"Payoff for Player 2: ")

    # Display the game
    print("\nGame Payoff Matrices:")
    print("Player 1's payoffs:")
    for row in payoff_matrix_1:
        print(row)

    print("\nPlayer 2's payoffs:")
    for row in payoff_matrix_2:
        print(row)

    # Find Nash Equilibria
    nash_equilibria = find_pure_nash_equilibria(payoff_matrix_1, payoff_matrix_2)

    # Display results
    print("\nResults:")
    if not nash_equilibria:
        print("No pure Nash Equilibria found.")
    else:
        print(f"Found {len(nash_equilibria)} pure Nash Equilibria:")
        for i, eq in enumerate(nash_equilibria, 1):
            # Convert to 1-indexed for display
            print(f"Equilibrium {i}: Player 1 plays strategy {eq[0] + 1}, Player 2 plays strategy {eq[1] + 1}")
            print(
                f"    Payoffs: Player 1 = {payoff_matrix_1[eq[0]][eq[1]]}, Player 2 = {payoff_matrix_2[eq[0]][eq[1]]}")

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()