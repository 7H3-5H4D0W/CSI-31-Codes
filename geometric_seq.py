# Here is the introduction.
# File: geometric_seq.py
# A program to compute the nth term of geometric sequence.

def main():
    print("This program calculates the nth term of a geometric sequence.")
    term = float(input("Enter the starting term: "))
    ratio = float(input("Enter the common ratio: "))
    nth = eval(input("Enter the nth term: "))
    for i in range(nth):
        print(term)
        term = term * ratio

    print("The", nth, "term of this geometric sequence is", term)

main()
