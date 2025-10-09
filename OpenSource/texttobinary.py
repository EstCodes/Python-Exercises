word = input("Enter a word or Message to convert: ")
print("Binary of the word is: ")
res = ''.join(format(ord(i), '08b') for i in word)

print("Binary code: ", res)
print("Binary code length: ", len(res))
print("Binary code type: ", type(res))
print("Binary code size: ", res.__sizeof__())
print("Binary code memory address: ", id(res))