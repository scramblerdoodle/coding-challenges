import asyncio
import random
from questions.question_1 import find_duplicates
from questions.question_2 import create_print_tasks
from questions.question_4 import check_brackets
from questions.question_5 import egg_drop
from questions.question_6 import zenos_paradox
from questions.question_7 import get_max_value


def test_question_1():
    assert find_duplicates([1, 1, 2, 3, 4, 4, 5, 2, 6, 5, 1]) == [1, 2, 4, 5]


def test_question_2():
    asyncio.run(create_print_tasks(["a", "b"]))


def test_question_4():
    assert check_brackets("{[]}")
    assert not check_brackets("{(])}")
    assert not check_brackets("{([)]}")
    assert not check_brackets("{()}[]]}{}()()((()){}{}{][][]}}{([")


def test_question_5():
    limit_floor = random.randint(1, 100)
    assert egg_drop(limit_floor)[0] == limit_floor - 1


def test_question_6():
    zenos_paradox(0.5, 64)


def test_question_7():
    carrot_types = [
        {"kg": 5, "price": 100},
        {"kg": 7, "price": 150},
        {"kg": 3, "price": 70},
    ]
    capacity = 36  # kg
    assert get_max_value(carrot_types, capacity) == 320
