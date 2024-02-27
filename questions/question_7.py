"""
----------------------------------------------------------------------------------------------------
QUESTION 6: 0-1 Knapsack Problem

Think that you have an unlimited number of carrots, but a limited number of carrot types.
Moreover, you have one bag that can hold a limited weight.
Each type of carrot has a weight and a price.

Write a function that takes carrot_types and capacity
and returns the maximum value the bag can hold.
----------------------------------------------------------------------------------------------------

Classic Knapsack problem, a notorious combinatorial NP problem. It's been quite a few years since
I've studied it.

The most well-known solution for the 0-1 Knapsack problem is by using dynamic programming, which
runs in pseudo-polynomial time.

The code was inspired in the approach suggested via pseudocode in the wiki page for the
Knapsack problem:
    https://en.wikipedia.org/wiki/Knapsack_problem
"""


def knapsack(capacity: int, weights: list, profits: list) -> int:
    """Calculates the maximum value a bag can hold in the 0-1 Knapsack problem."""

    # Sanity check for the input
    if len(weights) != len(profits):
        raise ValueError("Weights and profits must have same size")

    # Number of options to be inserted into the bag
    number_items = len(weights)

    # Table to find the solution
    table = [[0 for _ in range(capacity + 1)] for _ in range(number_items + 1)]

    # Conditions risen from the definition of the knapsack problem
    for i in range(1, number_items + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(
                    table[i - 1][j], table[i - 1][j - weights[i - 1]] + profits[i - 1]
                )

    # The value stored in the final position of the matrix is the maximum value the bag can hold
    return table[number_items][capacity]


def get_max_value(carrot_types: list[dict], capacity: int) -> int:
    """Gets the maximum value the bag can hold given a variety of carrot types and a bag capacity"""
    return knapsack(
        capacity,
        weights=[carrot["kg"] for carrot in carrot_types],
        profits=[carrot["price"] for carrot in carrot_types],
    )


if __name__ == "__main__":
    carrot_types = [
        {"kg": 5, "price": 100},
        {"kg": 7, "price": 150},
        {"kg": 3, "price": 70},
    ]
    capacity = 36
    print("0-1 Knapsack\n")
    print("Items:\n", carrot_types)
    print("Bag capacity:", capacity)
    print("Maximum value the bag can hold:", get_max_value(carrot_types, capacity))
