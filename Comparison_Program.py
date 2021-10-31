

with open(r'/home/pi/EEE3097S/HAT/Input.txt', "r") as e:
    Input = e.read().splitlines() #Creates the input file as an array
    

with open(r'/home/pi/EEE3097S/HAT/Output.txt', "r") as e:
    Output = e.read().splitlines() #Creates the outut file as an array

size = len(Input)

for i< size : #Loops throught the input and output data array checking of the values are the same
    if Input[i] == Output[i]:
        pass
    else :
        return print("Error Detected")
    i = i + 1

print("DONE")


