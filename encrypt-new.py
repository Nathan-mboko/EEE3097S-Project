from xorCryptPy import xorCrypt

encrypt = ""
decrypt = ""

with open(r'/home/pi/EEE3097S/HAT/Output.txt', "r") as e:
    contents = e.read()
    encrypt = xorCrypt(contents)


with open('en.txt', 'w') as f:
    f.write(encrypt)

print("DONE")


