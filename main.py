import asyncio
import random

from questions.question_1 import find_duplicates
from questions.question_2 import create_print_tasks
from questions.question_4 import check_brackets
from questions.question_5 import egg_drop
from questions.question_6 import zenos_paradox
from questions.question_7 import get_max_value


if __name__ == "__main__":
    # QUESTION 1
    print("QUESTION 1:")
    to_check_dups = [1, 1, 2, 3, 4, 4, 5, 2, 6, 5, 1]
    print(f"Duplicates of {str(to_check_dups)}:")
    print(find_duplicates(to_check_dups))
    print()

    # QUESTION 2
    print("QUESTION 2:")
    asyncio.run(create_print_tasks(["a", "b", "c"], print_timer=True))
    print()

    # QUESTION 4
    print("QUESTION 4:")
    to_check_brackets = ["{[]}", "{(])}", "{([)]}"]
    for case in to_check_brackets:
        print(f"Is '{case}' balanced?", end=" ")
        print(check_brackets(case))
    print()

    # QUESTION 5
    print("QUESTION 5:")
    limit_floor = random.randint(1, 100)
    print(f"Floor where the egg breaks: {limit_floor}")
    limit_egg_floor, egg_steps = egg_drop(limit_floor)
    print(f"Function result: {limit_egg_floor}")
    print(f"Number of steps: {egg_steps}")
    print()

    # QUESTION 6
    print("QUESTION 6:")
    print("Achilles and the Tortoise")
    zenos_paradox(0.5, 64)
    print()

    # QUESTION 7
    print("QUESTION 7:")
    carrot_types = [
        {"kg": 5, "price": 100},
        {"kg": 7, "price": 150},
        {"kg": 3, "price": 70},
    ]
    print(f"Carrot types: {carrot_types}")
    capacity = 36
    print(f"Bag capacity: {capacity}")

    print(f"Maximum value the bag can hold: {get_max_value(carrot_types, capacity)}")
