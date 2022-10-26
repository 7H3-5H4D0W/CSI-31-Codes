# File: fahrenheit_to_celsius.py
# This program converts Farenheit temperature to Celsius.

def main():
    fahrenheit = float(input("What is the Fahrenheit temperature? "))
    celsius = (5 * (fahrenheit - 32) / 9)
    print("\nThe temperature is", round(celsius, 4), "degrees Celsius.")

main()
