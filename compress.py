import zlib
text = ''
with open('encrypt.txt') as f:
    contents = f.read()
    text= contents
b = bytes(text)
compressed = zlib.compress(b)

print(compressed)
print("size of original: " + str(len(b)))
print("size of compressed: " + str(len(compressed)))

