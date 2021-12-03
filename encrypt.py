import sys
f = open(sys.argv[2], "r")
g = open(sys.argv[3], "wb")
i = 0
parola = sys.argv[1]
for line in f:
    for character in line:
        if(i == len(parola)):
            i = 0
        car = bytes(chr(ord(character) ^ ord(parola[i])), "utf-8")
        g.write(car)
        i += 1
f.close()
g.close()