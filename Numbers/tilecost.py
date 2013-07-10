# Find Cost of Tile to Cover W x H Floor
# Calculate the total cost of tile it would take
# to cover a floor plan of width and height,
# using a cost entered by the user.

if __name__ == '__main__':
    w = input('Enter width: ')
    h = input('Enter height: ')
    c = input('Cost: ')


    print c / (1.0 * w * h)
