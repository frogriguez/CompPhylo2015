try:
    # ask the user for the filename, open it and read the DNA sequence
    input_file = raw_input('enter filename:\n')
    f = open(input_file)
    dna = f.read().rstrip("\n")

    # ask the user for the number of pieces and calculate the piece length
    pieces = int(raw_input('enter number of pieces:\n'))
    piece_length = len(dna) / pieces
    print('piece length is ' + str(piece_length))

# deal with exceptions that may be raised
except IOError as ex:
    print("Couldn't open the file: " + ex.strerror)
except ValueError as ex:
    print("Not a valid number: " + ex.args[0])
except ZeroDivisionError as ex:
    print("Number of pieces can't be zero")

else:
    # no exceptions, so it's safe to go ahead and print out the pieces
    for start in range(0, len(dna)-piece_length+1, piece_length):
        print(dna[start:start+piece_length])

