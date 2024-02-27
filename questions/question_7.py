# 0-1 Knapsack Problem


def knapsack_recursive(
    capacity: int, weights: list[int], profits: list[int], number_items: int
):

    # Base Case
    if number_items == 0 or capacity == 0:
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if weights[number_items - 1] > capacity:
        return knapsack_recursive(capacity, weights, profits, number_items - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            profits[number_items - 1]
            + knapsack_recursive(
                capacity - weights[number_items - 1], weights, profits, number_items - 1
            ),
            knapsack_recursive(capacity, weights, profits, number_items - 1),
        )


def knapsack_dynamic(capacity: int, weights: list, profits: list):
    if len(weights) != len(profits):
        raise ValueError("Weights and profits must have same size")

    amount_options = len(weights)

    knapsack_table = [
        [0 for _ in range(capacity + 1)] for _ in range(amount_options + 1)
    ]

    for i in range(amount_options + 1):
        for j in range(capacity + 1):

            if i == 0 or j == 0:
                knapsack_table[i][j] = 0

            elif weights[i - 1] <= j:
                knapsack_table[i][j] = max(
                    profits[i - 1] + knapsack_table[i - 1][j - weights[i - 1]],
                    knapsack_table[i - 1][j],
                )

            else:
                knapsack_table[i][j] = knapsack_table[i - 1][j]

    return knapsack_table[amount_options][capacity]


def get_max_value(carrot_types: list[dict], capacity: int) -> int:
    return knapsack_dynamic(
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
    print(get_max_value(carrot_types, capacity))
