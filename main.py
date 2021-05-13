#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program uses a while loop to solve a factorial


def main():
    # this function uses a while loop to solve a factorial

    # this is to keep track of hw many times you go through the loop
    loop_counter = 0

    # input
    print("\n", end="")
    positive = input("Enter an integer to factor: ")

    # process & output
    try:
        positive_int = int(positive)
        final_number = 1
        print("\n", end="")
        while loop_counter < positive_int:
            loop_counter = loop_counter + 1

            final_number = final_number * loop_counter

        if positive_int < 0:
            print("You cannot enter a negative integer.")

        elif final_number == 0:
            print(" The factorial of 0 is 1.")

        else:
            print("The factorial of {0} is {1}."
                  .format(positive_int, final_number))

    except Exception:
        print("You have entered an invalid integer.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
