"""
----------------------------------------------------------------------------------------------------
QUESTION 6: Zeno's Paradox of Achilles and the Tortoise

Write the code that animates "Zeno's Paradox of Achilles and the Tortoise" on the terminal.
We would like to see the paradox demonstrated.

----------------------------------------------------------------------------------------------------
Zeno's Paradox of Achilles and the Tortoise is one of Zeno's motion paradoxes, consisting of
a race between Achilles and a Tortoise, where the Tortoise has a head start in relation to Achilles
in Zeno's paradox, the idea is that no matter how faster Achilles moves,
the Tortoise will always be ahead since it also moves during that time.

In the following example, consider A to be Achilles and T the Tortoise.

In this step, Achilles is on position 0 and the Tortoise is on position 32.
|A-------------------------------T-------------------------------|

Now, in the time that Achilles took to reach position 32, the Tortoise moved to position 48.
|--------------------------------A---------------T---------------|

Again, in the time Achilles took to reach position 48, the Tortoise moved to position 56.
|------------------------------------------------A-------T-------|

So on and so forth, until eventually A almost reaches T:
|--------------------------------------------------------------AT|


In the simulation, however, we use whole numbers, which fails to grasp the
infinitesimal nature of the paradox (eventually in the simulation both would occupy the same
position, but Zeno argues that even if they are 0.5 cm apart, in the time for Achilles to reach
the Tortoise it'd have moved another 0.1 cm or so, and keep approaching infinitely closer but never
reaching).
Here I've tried to "fake" this by making them both move 1 position at a time when they're adjacent,
but the idea is as explained above.

Anyway, explanation aside, the code itself is relatively straightforward.

This one uses sys.stdout.write to overwrite stdout with the different states of the animation.
The animation uses by default the position of the Tortoise as the midway in the track,
and the Tortoise speed as a quarter of the track size.
This is arbitrary, just to make the animation look nice for exponents of two (4, 8, 16, 32, etc).

The __main__ portion of the code also has a simple user interface with some options to change
the animation speed or the track size.
"""

# Zeno's Paradox of Achilles and the Tortoise
import time
import sys

# Symbols
ACHILLES = "A"
TORTOISE = "T"

# Default options
DEFAULT_ANIMATION_SPEED = 0.5
DEFAULT_TOTAL_DISTANCE = 64


def zenos_paradox(animation_speed: float, track_size: int) -> None:
    """Animates Zeno's Paradox of Achilles and the Tortoise"""

    # Track setup
    BASE_TRACK = "-" * track_size

    # Tortoise setup
    tortoise_speed = track_size // 4
    TORTOISE_STARTING_POINT = track_size // 2

    # Initial position setup
    tortoise_pos = TORTOISE_STARTING_POINT
    achilles_pos = 0

    # Loop until the end of the track
    while tortoise_pos < track_size:

        # Build the string containing the track with A and T
        track = (
            BASE_TRACK[:achilles_pos]
            + ACHILLES
            + BASE_TRACK[achilles_pos + 1 : tortoise_pos]
            + TORTOISE
            + BASE_TRACK[: track_size - tortoise_pos - 1]
        )

        # sys.stdout to overwrite the string and animate the simulation
        sys.stdout.write("\r" + "|" + track + "|")
        sys.stdout.flush()
        time.sleep(animation_speed)

        # Put Achilles on the Tortoise position,
        # and make the Tortoise move
        achilles_pos = tortoise_pos
        tortoise_pos += tortoise_speed

        # Halve the tortoise speed
        if tortoise_speed > 1:
            tortoise_speed //= 2

    # Final print just to add a line break to the animation
    print()


if __name__ == "__main__":
    option = ""
    animation_speed = DEFAULT_ANIMATION_SPEED
    track_size = DEFAULT_TOTAL_DISTANCE

    print("\nZeno's Paradox of Achilles and the Tortoise")
    while option != "r":
        option = input(
            """
    Choose an option:
            r: Run the animation
            s: Choose new animation speed (default 0.5 seconds)
            t: Choose track size (default 64)
            q: Quit
    > """
        )
        if option == "s":
            animation_speed = float(input("Animation speed (in seconds): "))
        elif option == "t":
            track_size = int(input("Track size: "))
        elif option == "r":
            break
        elif option == "q":
            exit()
        else:
            print("ERROR! Invalid option.")

    zenos_paradox(animation_speed, track_size)
