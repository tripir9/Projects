# Tax Calculator
# Asks the user to enter a cost and either a country or state tax.
# It then returns the tax plus the total cost with tax.

if __name__ == '__main__':
    c = input('Enter cost: ')
    t = input('Enter tax(%): ')

    print c + (c * (1.0 * t / 100))
