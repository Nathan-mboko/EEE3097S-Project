from xorCryptPy import xorCrypt

decrypt = ""

with open('decompress.txt') as f:
    contents = f.read()
    decrypt = xorCrypt(contents)
    print(decrypt)

with open('decrypt.txt', 'w') as f:
    f.write(decrypt)


