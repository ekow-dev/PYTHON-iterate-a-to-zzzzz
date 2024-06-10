letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
dec1 = -1
dec2 = -1
dec3 = -1
dec4 = -1
dec5 = -1
while dec1 != 25:
    dec1 += 1
    print(letters[dec1])
dec1 = -1
while dec1 != 25:
    dec1 += 1
    while dec2 != 25:
        dec2 += 1
        print(letters[dec1]+letters[dec2])
    dec2 = -1
dec1 = -1
while dec1 != 25:
    dec1 += 1
    while dec2 != 25:
        dec2 += 1
        while dec3 != 25:
            dec3 += 1
            print(letters[dec1]+letters[dec2]+letters[dec3])
        dec3 = -1
    dec2 = -1
dec1 = -1
while dec1 != 25:
    dec1 += 1
    while dec2 != 25:
        dec2 += 1
        while dec3 != 25:
            dec3 += 1
            while dec4 != 25:
                dec4 += 1
                print(letters[dec1]+letters[dec2]+letters[dec3]+letters[dec4])
            dec4 = -1
        dec3 = -1
    dec2 = -1
dec1 = -1
while dec1 != 25:
    dec1 += 1
    while dec2 != 25:
        dec2 += 1
        while dec3 != 25:
            dec3 += 1
            while dec4 != 25:
                dec4 += 1
                while dec5 != 25:
                    dec5 += 1
                    print(letters[dec1]+letters[dec2]+letters[dec3]+letters[dec4]+letters[dec5])
                dec5 = -1
            dec4 = -1
        dec3 = -1
    dec2 = -1
