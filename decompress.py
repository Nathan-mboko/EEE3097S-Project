import zlib
text = ''

with open('encrypt.txt') as f:
    contents = f.read()
    text= contents
b = bytes(text)
compressed = zlib.compress(b)

decompressed = zlib.decompress(compressed)
print("size of original: " + str(len(b)))
print("size of decompresse-d: " + str(len(decompressed)))

with open('decompress.txt', 'w') as f:
    f.write(decompressed.decode('UTF-8'))

print(decompressed)
