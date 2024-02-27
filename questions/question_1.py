"""
----------------------------------------------------------------------------------------------------
QUESTION 1:
    Write a python function that finds the duplicate items in a list
----------------------------------------------------------------------------------------------------

This one's very simple, with a few different possible solutions.

The first one (find_duplicates_defaultdict) creates a dictionary for counting the occurrences, then
filters out any number which has only appeared once. 

The second one (find_duplicates_set) uses two hash maps to keep track of the found numbers and
the duplicates, returning the list of repeated numbers.
"""

from collections import defaultdict


def find_duplicates_defaultdict(nums: list) -> list:
    """Find duplicates in a list of items, using a defaultdict counter"""
    counter = defaultdict(int)
    for n in nums:
        counter[n] += 1

    return list(n for n, c in counter.items() if c > 1)


def find_duplicates_set(nums: list) -> list:
    """Find duplicates in a list of items, using sets"""
    found = set()
    duplicates = set()
    for n in nums:
        if n in found:
            duplicates.add(n)
        else:
            found.add(n)

    return list(duplicates)


find_duplicates = find_duplicates_defaultdict

if __name__ == "__main__":
    nums = input("Input list of numbers separated by spaces (e.g. 1 2 3 4 1)\n")
    nums = list(map(int, nums.split()))
    print(f"Duplicates in list: {find_duplicates(nums)}")
