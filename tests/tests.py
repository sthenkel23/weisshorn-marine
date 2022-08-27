import pytest

def random_fruit():
  return "apple"

def test_random_fruit_slow():
   sleep(3)
   assert random_fruit() in ["apple", "banana", "orange"]
