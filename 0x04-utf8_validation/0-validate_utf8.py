#!/usr/bin/python3
"""module: function validUTF8(data)"""


def get_prefix(binary_string):
    """A function to count the number of 1's
    at the start of a binary string
    """
    count = 0
    for char in binary_string:
        if char == '0':
            break
        count += 1

    return count


def validUTF8(data):
    """A function to check the validity of data
    that is supposedly  UTF-8 encoded
    - Return: True if data is a valid UTF-8 encoding, else return False
    - A character in UTF-8 can be 1 to 4 bytes long
    - The data set can contain multiple characters
    - The data will be represented by a list of integers
    - Each integer represents 1 byte of data, therefore you only need to
      handle the 8 least significant bits of each integer

      - format of UTF.
      1 byte - 0*******
      2 bytes - [ 11******, 10****** ]
      3 bytes - 111***** 10****** 10****** 10*****
      4 bytes - 1111**** 10****** 10****** 10****** 10******

      - strategy
      the count of ones in the start has to be correspondent to the count
      of bytes starting with 1 after that.
      - capture count
      - loop over the next items in the list and skip items equal to count.
    """
    count = 0

    for byte in data:
        binary_rep = bin(byte)[2:].zfill(8)

        if count == 0:
            count = get_prefix(binary_rep)

            if count == 0:
                continue

            if count == 1 or count > 4:
                return False
        else:
            if not binary_rep.startswith('10'):
                return False

        count -= 1

    return count == 0
