#Applied Cryptography
#Column Transposition
#Budrescu Sorin-Andrei - CSML II - 2023

import numpy as np

def adjustSize(message,key,char):
    #used in decryption, adding * symbols so that len(string) % len(key) == 0
    result = message
    if len(result) % len(key) == 0:
        return result

    while len(result) % len(key) != 0:
        result+=char
    return result

def stringToArray(string):
    listOfChars = list()
    for character in string:
        if character == ' ':
            continue
        listOfChars.append(character)
    return listOfChars

def arrayToString(string):
    result = ''
    for char in string:
        result+=char
    return result

def alphabeticalOrder(string):
    mappings = list()
    i = 0
    sortedString = sorted(string)
    for character in sortedString:
        mappings.append([i,character])
        i+=1

    #Return sorted word back to original word, keeping the same indices
    mappingsOrdered = list()
    for character in string:
        for element in mappings:
            if element[1] == character:
                mappingsOrdered.append(element)

    result = list()
    for element in mappingsOrdered:
        result.append(element[0])

    return result

def encrypt(message,key):
    #Convert to uppercase from start so we don't mess up sorting of characters
    message = message.upper()
    key = key.upper()

    #Hacky way to make sure every string can be encrypted, as len(message) needs to be divisible by len(key)
    message = adjustSize(message, key, '.')

    chararray = stringToArray(message) #convert string to character array
    columns = len(key) #key dictates the number of columns

    gridtext = [chararray[i:i + columns] for i in range(0, len(chararray), columns)] #split array after every [columns] characters
    lastgroup =  gridtext[len(gridtext)-1] # last group of the split array

    while(len(lastgroup)<columns):
        gridtext[len(gridtext) - 1].append('*') #add * so that we fill the matrix

    gridtext = np.transpose(gridtext)
    permutation = alphabeticalOrder(key) #determine the alphabetical order of the key string

    print('Text to encrypt: '+message)
    print('Plaintext arranged into the grid:')
    print(gridtext)

    print('Key: '+key)
    print('Permutation: '+str(permutation))

    orderedGroups = list()

    for i in range(columns):
        orderedGroups.append([gridtext[i],permutation[i]])

    sortedGroups = sorted(orderedGroups, key=lambda t: t[1])

    result = ''
    for tuple in sortedGroups:
        result += arrayToString(tuple[0])

    result = result.replace('*','')

    print('Encrypted Result: '+result.replace('.',''))
    return result

def decrypt(message,key):
    #convert key to upper to avoid any issues
    key = key.upper()

    #message =  adjustSize(message,key,'*')
    print('Text to decrypt: ' +message.replace('.',''))
    groupSize = int(len(message)/len(key))
    print('Group size: ' +str(groupSize))

    chararray = stringToArray(message)  # convert string to character array

    gridtext = [chararray[i:i + groupSize] for i in range(0, len(chararray), groupSize)]
    gridtext = np.transpose(gridtext)

    print('Crypted text arranged into a grid')
    print(gridtext)

    permutation = alphabeticalOrder(key)
    print('Key: '+key)
    print('Key Permutation:' + str(permutation))

    result = ''

    for i in range(groupSize):
        for index in permutation:
            result += gridtext[i][index]

    print('Decrypted Result: '+result.replace('.',''))
    return result


#Main
if __name__ == '__main__':
    message = 'a very secret and important message'
    key = 'cipher'
    message = message.replace(' ','')

    encrypted = encrypt(message,key)
    print('\n----------------\n')
    decrypted = decrypt(encrypted,key)