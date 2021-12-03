import sys
f = open(sys.argv[1], "rb")
g = open(sys.argv[3], "w")
i = 0
parola = sys.argv[2]
for line in f:
    for byte in line:
        if (i == len(parola)):
            i = 0
        car = chr(byte ^ ord(parola[i]))
        g.write(car)
        i += 1
f.close()
g.close()