raw = r'this\t\n and that'

print(raw)

multi = '''It was the best of times.
It was the worst of times.'''

print(multi)

# % operator
text = (
        "%d little pigs come out, "
        "or I'll %s, and I'll %s, "
        "and I'll blow your %s down."
        % (3, 'huff', 'puff', 'house'))
print(text)
