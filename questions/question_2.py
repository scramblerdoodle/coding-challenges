"""
----------------------------------------------------------------------------------------------------
QUESTION 2:
    Write an async python function that writes every item in any given 
    array with 1, 2, 4, 8, etc., seconds apart.

    Example:  
    for ["a", "b", "c", "d"], 
        "a" is printed in 1 sec, 
        "b" is printed in 2 seconds, 
        "c" is printed in 4 seconds, etc.
----------------------------------------------------------------------------------------------------

This one's a simple matter of creating an async function with an await sleep timer in powers of 2,
depending on the number of items in the input list.

"""

import asyncio


async def delayed_print(value: str, timer: int, print_timer: bool = False) -> None:
    """Prints `value` after `timer` seconds"""
    await asyncio.sleep(timer)

    if not print_timer:
        print(value)
    else:
        print(f"{value} (Elapsed time: {timer}s)")


async def create_print_tasks(input_list: list, print_timer: bool = False) -> None:
    """Creates the async tasks to print with a delay"""
    tasks = [
        asyncio.create_task(delayed_print(input_list[i], 2**i, print_timer))
        for i in range(len(input_list))
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    input_list = input("Array to be printed, separated by spaces: ")
    input_list = input_list.split()
    print(f"Printing input list:")
    asyncio.run(create_print_tasks(input_list, False))
