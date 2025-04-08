plainText1 = "12345"
plainText2 = "33253"

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

def stream_cipher_attack(cipherText1, cipherText2):
    if len(cipherText1)>len(cipherText2):
        xor_result = [int(cipherText1[i], 2) ^ int(cipherText2[i], 2) for i in range(len(cipherText2))]
    else :
        xor_result = [int(cipherText1[i], 2) ^ int(cipherText2[i], 2) for i in range(len(cipherText1))]

    charset="0123456789"
    prediction=[]
    
    while prediction != xor_result:
        print()

    return prediction

# Encrypt
cipher1, cipher2 = stream_cipher(plainText1, plainText2, IV)

print( stream_cipher_attack(cipher1,cipher2))
