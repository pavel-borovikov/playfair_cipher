#         Polybius Playfair Cipher

keyword = 'ADALOVELACE'
message = 'LVFPPNMQDOORAYJVKHPGPBTPKHNZFOAY'

# Grid details
valid_characters = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'
grid_size = 5


# The letter 'j' also stands for the letter 'i' that is missing in order for the valid_characters to contain 25 letters.
# group_size is linked with the amount of letters in the valid_characters. 5 ** 2 = 25


def decipher(keyword, message):
    # Preparing the grid
    grid_values = []
    grid = []

    for letter in keyword:
        if letter in valid_characters:
            if letter not in grid_values:
                grid_values.append(letter)
        else:
            return print(f"Error! '{letter}' in the keyword is not a valid character.")

    for letter in valid_characters:
        if letter not in grid_values:
            grid_values.append(letter)

    for i in range(grid_size):  # Creating the amount of rows
        grid.append([])

    for i in range(len(grid_values)):
        row = i // grid_size
        grid[row].append(grid_values[i])

    # Grouping and deciphering characters
    group = []
    coordinates = []
    deciphered_message = []
    for i in range(len(message)):
        # Finding the grid coordinates of the grouped letters
        try:
            if len(group) < 2:
                if message[i] in valid_characters:
                    group.append(message[i])
                else:
                    return print(f"Error! '{message[i]}' in the message is not a valid character.")

        finally:
            if len(group) == 2:
                for letter in group:
                    for row in range(len(grid)):
                        if letter in grid[row]:
                            x = grid[row].index(letter)
                            y = row
                            coordinates.append([x, y])

                # Decoding the characters
                # Same x
                if coordinates[0][0] == coordinates[1][0]:
                    letter1 = grid[coordinates[0][1] - 1][coordinates[0][0]]
                    letter2 = grid[coordinates[1][1] - 1][coordinates[1][0]]
                    deciphered_message.append(letter1)
                    deciphered_message.append(letter2)

                # Same y
                elif coordinates[0][1] == coordinates[1][1]:
                    letter1 = grid[coordinates[0][1]][coordinates[0][0] - 1]
                    letter2 = grid[coordinates[1][1]][coordinates[1][0] - 1]
                    deciphered_message.append(letter1)
                    deciphered_message.append(letter2)

                # Both different
                else:
                    letter1 = grid[coordinates[0][1]][coordinates[1][0]]
                    letter2 = grid[coordinates[1][1]][coordinates[0][0]]
                    deciphered_message.append(letter1)
                    deciphered_message.append(letter2)

                group = []
                coordinates = []

    print(deciphered_message)


decipher(keyword, message)
