# translator for 1337 5P3@|<
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "A":
            translation = translation + "@"
        elif letter in "B":
            translation = translation + "8"
        elif letter in "C":
            translation = translation + "<"
        elif letter in "E":
            translation = translation + "3"
        elif letter in "F":
            translation = translation + "|="
        elif letter in "G":
            translation = translation + "9"
        elif letter in "H":
            translation = translation + "|-|"
        elif letter in "I":
            translation = translation + "1"
        elif letter in "K":
            translation = translation + "|<"
        elif letter in "L":
            translation = translation + "1"
        elif letter in "M":
            translation = translation + "/\/\\"
        elif letter in "N":
            translation = translation + "|\|"
        elif letter in "O":
            translation = translation + "0"
        elif letter in "R":
            translation = translation + "4"
        elif letter in "S":
            translation = translation + "5"
        elif letter in "T":
            translation = translation + "7"
        elif letter in "U":
            translation = translation + "(_)"
        elif letter in "V":
            translation = translation + "\/"
        elif letter in "W":
            translation = translation + "\/\/"
        elif letter in "X":
            translation = translation + "*"
        elif letter in "Z":
            translation = translation + "2"
        else:
            translation = translation + letter
    return translation


print(translate(raw_input("Enter words:").upper()))