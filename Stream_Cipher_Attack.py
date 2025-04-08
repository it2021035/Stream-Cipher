plainText1 = "I use the same IV because i am lazy"
plainText2 = "But now the can see the message"

IV = int("01001011", 2)

def stream_cipher(plainText1, plainText2, IV):
    cipherText1 = []
    cipherText2 = []

    bit_list1 = [format(num, '08b') for num in list(plainText1.encode('ascii'))]
    bit_list2 = [format(num, '08b') for num in list(plainText2.encode('ascii'))]

    for i in range(len(bit_list1)):
        xor_result = int(bit_list1[i], 2) ^ IV
        cipherText1.append(format(xor_result, '08b'))

    for i in range(len(bit_list2)):
        xor_result = int(bit_list2[i], 2) ^ IV
        cipherText2.append(format(xor_result, '08b'))

    return cipherText1, cipherText2

def stream_cipher_attack(cipherText1, cipherText2, knownPlainText):
    if len(cipherText1)>len(cipherText2):
        xor_result = [int(cipherText1[i], 2) ^ int(cipherText2[i], 2) for i in range(len(cipherText2))]
    else :
        xor_result = [int(cipherText1[i], 2) ^ int(cipherText2[i], 2) for i in range(len(cipherText1))]

    knownPlainText_bytes = [ord(c) for c in knownPlainText]
    recovered_bytes = [xor_result[i] ^ knownPlainText_bytes[i] for i in range(len(xor_result))]
    return ''.join(chr(b) for b in recovered_bytes)

# Encrypt
cipher1, cipher2 = stream_cipher(plainText1, plainText2, IV)

# Attack using known plainText1 to recover plainText2
recovered_plaintext2 = stream_cipher_attack(cipher1, cipher2, plainText1)

print("Recovered Plaintext 2:", recovered_plaintext2)
