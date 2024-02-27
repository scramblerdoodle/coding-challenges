"""
----------------------------------------------------------------------------------------------------
QUESTION 5: Dropping two eggs from a 100-story building

A building has 100 floors. One of the floors is the highest floor an egg can be dropped from without
breaking. If an egg is dropped from above that floor, it will break. If it is dropped from that
floor or below, it will be completely undamaged, and you can drop the egg again.

Given two eggs, find the highest floor an egg can be dropped from without breaking, 
with as few drops as possible in the worst-case scenario.

----------------------------------------------------------------------------------------------------
The first naïve idea was, of course, a linear check: test floor 1, then 2, etc...
It's guaranteed to find the solution but it takes N tries, where N is the number of floors.

The second one was a sort of binary search, but it wouldn't make any sense: if the floor where
the egg breaks is 49, then we'd check floor 50, the egg would break and we'd have to test up to
floor 49. So this algorithm would take N/2 - 1 tries at worst case.

So the approach I ended up taking was to skip a certain number of floors `SKIP_FLOORS` at every
iteration. The egg is thrown every K floors, until it breaks at floor N.
Once it does, the check becomes linear from the penultimate floor thrown up until N.

I tested a few numbers for the number of floors to be skipped, and the range from 8 through 13
always seemed to result 19 steps for worst case.

So I chose 10 since it's a a nicer number to explain the worst case:

    Assume the floor in which the egg breaks is the 100th floor
    Thus, in the algorithm, we'll check every 10 floors up to 100,
    i.e. floors 10, 20, 30, ..., up to 100,
    resulting in 10 throws.

    From which, we need to check from the last unbroken position plus 1 (91), up to, at most,
    the position where it broke minus one (99).
    
    Thus, throw it from 91, 92, 93, ..., up to 99.
    Resulting in 9 throws.

    Since it didn't break when thrown from floor 99 but it broke from floor 100,
    the last floor where it can be thrown from is the 99th floor, in 19 throws.
"""

# Number of floors to be skipped at every iteration
SKIP_FLOORS = 10


# Worst-case Complexity: floor 100; #steps = 10 + 9 = 19
def egg_drop(limit: int, current: int = 0, n_steps: int = 0) -> tuple[int, int]:

    # Breaks the first egg if current+10 exceeds (or is equal to) the limit
    if current + SKIP_FLOORS >= limit:

        # Attempts linearly floor-by-floor if the first egg breaks,
        # up to the position where the egg broke - 1
        while current < limit:
            n_steps += 1
            current += 1

        limit_floor = current - 1

    else:
        limit_floor, n_steps = egg_drop(limit, current + SKIP_FLOORS, n_steps + 1)

    return limit_floor, n_steps


if __name__ == "__main__":
    limit_floor = int(input("Input floor where the egg would break: "))
    if limit_floor < 1:
        raise ValueError("Invalid input, egg can only break after floor 0")

    result_egg_floor, n_steps = egg_drop(limit_floor)
    print(f"Limit floor: {result_egg_floor}")
    print(f"Number of steps: {n_steps}")

    # # Very naïve way to check complexity, can be used to check for other values of SKIP_FLOORS
    # floors = range(1, 101)
    # results = [r for r in map(egg_drop, floors)]
    # max_steps = 0
    # max_floor = 0
    # for r, s in results:
    #     if s >= max_steps:
    #         max_steps = s
    #         max_floor = r + 1

    # print(max_floor, max_steps)
