plainText1 = "I use unsafe steam ciphers"
plainText2 = "Are you sure thow?"

IV = int("01001011", 2)

def stream_cipher (plainText1, plainText2, IV):
    cipherText1 = []
    cipherText2 = []

    bit_list1 = [format(num, '08b') for num in list(plainText1.encode('ascii'))]
    bit_list2 = [format(num, '08b') for num in list(plainText2.encode('ascii'))]


    for i in range(len(bit_list1)):
        xor_result = int(bit_list1[i], 2) ^ IV  # XOR in integer form
        cipherText1.append(format(xor_result, '08b'))  # Back to 8-bit binary

    for i in range(len(bit_list2)):
        xor_result = int(bit_list2[i], 2) ^ IV
        cipherText2.append(format(xor_result, '08b'))

    return cipherText1, cipherText2

#wokr in progress
def stream_cipher_attack(cipherText1, cipherText2, knownPlainText):
    # XOR the two cipher texts to get the XOR of the two plaintexts
    xor_result = [int(cipherText1[i], 2) ^ int(cipherText2[i], 2) for i in range(len(cipherText2))]

    xor_result.append(format(xor_result, '08b'))

    knownPlainText = [format(num, '08b') for num in list(knownPlainText.encode('ascii'))]

    # XOR the known plaintext with the xor_result to get the keystream
    keystream  = [int(xor_result[i], 2) ^ int(knownPlainText[i], 2) for i in range(len(knownPlainText))]


    return keystream


cipher1, cipher2 = stream_cipher(plainText1, plainText2, IV)

print(stream_cipher_attack(cipher1, cipher2, plainText1))
