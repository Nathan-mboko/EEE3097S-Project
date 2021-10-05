from xorCryptPy import xorCrypt

text_list = []
encrypt = ""
decrypt = ""
with open(r'/home/pi/EEE3097S/2018-09-19-04_22_21_VN100.csv', "r") as my_input_file:
    for line in my_input_file:
        line = line.split(",", 2)
        text_list.append(" ".join(line))

with open('table.txt', "w") as my_output_file:
    my_output_file.write("#1\n")
    my_output_file.write("double({},{})\n".format(len(text_list), 2))
    for line in text_list:
        my_output_file.write("  " + line)
    print('File Successfully written.')

with open('table.txt') as f:
    contents = f.read()
    encrypt = xorCrypt(contents)
    print(encrypt)

with open('encrypt.txt', 'w') as f:
    f.write(encrypt)

