def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

# edit the text below to see how this works
text = 'cats'
bits = string2bits(text)

for x in bits:
    print(x)

string2bits("cats")
