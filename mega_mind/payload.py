def boomboom(x):
    if 'a' <= x.lower() <= 'z': return chr(ord('a') + (ord(x) - ord('a') + 15) % 26)
    elif '0' <= x <= '9': return chr(ord('0') + (ord(x) - ord('0') + 4) % 10)
    return x
with open(__file__, "r") as f: prog = ''.join([boomboom(x) for x in f.read()])
with open(__file__, "w") as f: f.write(prog)
