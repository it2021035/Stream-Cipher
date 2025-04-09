plainText1 = "53"
plainText2 = "74"

IV = int("01001011", 2)

def stream_cipher(plainText1, plainText2, IV):
    cipherText1 = []
    cipherText2 = []

    bit_list1 = [format(num, '08b') for num in list(int(char) for char in plainText1)]
    bit_list2 = [format(num, '08b') for num in list(int(char) for char in plainText2)]

    for i in range(len(bit_list1)):
        xor_result = int(bit_list1[i], 2) ^ IV
        cipherText1.append(format(xor_result, '08b'))

    for i in range(len(bit_list2)):
        xor_result = int(bit_list2[i], 2) ^ IV
        cipherText2.append(format(xor_result, '08b'))

    return cipherText1, cipherText2

def stream_cipher_attack(cipherText1, cipherText2):
    if len(cipherText1)>len(cipherText2):
        xor_result = [int(cipherText1[i], 2) ^ int(cipherText2[i], 2) for i in range(len(cipherText2))]
    else :
        xor_result = [int(cipherText1[i], 2) ^ int(cipherText2[i], 2) for i in range(len(cipherText1))]

    predictions = []

    for xor_val in xor_result:
        possible_pairs = []
        for d1 in range(10):  # '0' έως '9'
            ascii_d1 = ord(str(d1))
            for d2 in range(10):
                ascii_d2 = ord(str(d2))
                if ascii_d1 ^ ascii_d2 == xor_val:
                    pair = tuple(sorted((d1, d2)))  # βάζει το μικρότερο πρώτο
                    if pair not in possible_pairs:
                        possible_pairs.append(pair)
        predictions.append(possible_pairs)

    for i, pairs in enumerate(predictions):
        p1_candidates = sorted(set(pair[0] for pair in pairs))
        p2_candidates = sorted(set(pair[1] for pair in pairs))
        print(f"Digit {i+1}: p1 = {p1_candidates}, p2 = {p2_candidates}")


    return predictions

# Encrypt
cipher1, cipher2 = stream_cipher(plainText1, plainText2, IV)

print( stream_cipher_attack(cipher1,cipher2))
