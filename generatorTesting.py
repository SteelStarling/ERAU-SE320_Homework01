#!/usr/bin/env python3

"""Generator testing for SE320 - Software Construction, containing generators for the Fibbonaci Sequence and Recaman's Sequence
Author: Taylor Hancock
Date:   01/24/2025
Class:  SE320 - Software Construction
Assignment: Assignment 01 - Generator Functions
"""

from itertools import count

def fibbonaci(n = 0):
    """Generates each value in the Fibbonaci Sequence (OEIS A000045).
    
    Formal Definition:
        a_0 = 0,
        a_1 = 1,
        a_n = a_(n-1) + a_(n-2).
    
    Optional Arguments:
        n (int): The number of inputs to output or zero for infinite (default: 0)
    """
    last_two = [0, 1] # define to first two numbers, will be replaced each time

    # for loop (since we need to know how many loops)
    for i in count(0):
        # break out of loop once n is reached (if n describes an end point)
        if n != 0 and i >= n:
            break
        
        # first two outputs hardcoded
        if i == 0:
            yield last_two[0]
        elif i == 1:
            yield last_two[1]
        else:
            # calculate next number
            next_number = sum(last_two)

            yield next_number

            # update list
            last_two[0] = last_two[1]
            last_two[1] = next_number

def recaman(n = 0):
    """Generates each value in Recaman's Sequence (OEIS A005132).
    
    Formal Definition:
        a_0 = 0,
        a_n = a_(n-1) - n, if a_n > 0 and not already in sequence,
        otherwise a_n = a_(n-1) + n.
    
    Optional Arguments:
        n (int): The number of inputs to output or zero for infinite (default: 0)
    """
    a_prev = 0
    recaman_set = set()

    # for loop (since we need to know how many loops)
    for i in count(0):
        # break out of loop once n is reached (if n describes an end point)
        if n != 0 and i >= n:
            break

        # add previous item to set
        recaman_set.add(a_prev)

        yield a_prev

        # get a_prev - (i + 1) -> due to counting from zero
        a_n = a_prev - (i + 1)

        # if a_n <= 0 or in set, a_n = a_prev + (i + 1)
        if a_n <= 0 or a_n in recaman_set:
            a_n = a_prev + (i + 1)
        
        # update a_prev
        a_prev = a_n


if __name__ == "__main__":
    print("========== FIBBONACI ==========")
    
    print("Infinite Fibbonaci:")
    infinite_fibbonaci = fibbonaci()
    for i in range(50):
        print(f"{i + 1}.  {next(infinite_fibbonaci)}")
    
    print("\nFinite Fibbonaci:")
    short_fibbonaci = fibbonaci(5)
    for i, fib in enumerate(short_fibbonaci):
        print(f"{i + 1}.  {fib}")

    print("\n\n")
    print("=========== RECAMAN ===========")

    print("Infinite Recaman:")
    infinite_recaman = recaman()
    for i in range(50):
        print(f"{i + 1}.  {next(infinite_recaman)}")
    
    print("\nFinite Recaman:")
    short_recaman = recaman(5)
    for i, rec in enumerate(short_recaman):
        print(f"{i + 1}.  {rec}")