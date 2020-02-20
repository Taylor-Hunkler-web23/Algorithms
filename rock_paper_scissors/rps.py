#!/usr/bin/python

import sys

plays = ["rock", "paper", "scissors"]
def rock_paper_scissors(n):

  # combos = []

    if n == 0:
        return [] 
    if n == 1:
        return plays


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')