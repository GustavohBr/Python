#Password generator (currently with 9 digits)

import random
a = [str(chr(i)) for i in range(ord('a'), ord('z'))]
b = [str(chr(i)) for i in range(ord('A'), ord('Z'))]
c = [str(i) for i in range(0, 10)]
def generate():
    pw = []
    for i in range(3):
        pw.append(random.choice(a))
        pw.append(random.choice(b))
        pw.append(random.choice(c))
    random.shuffle(pw)
    pw = "".join(pw)
    return pw
print(generate())
