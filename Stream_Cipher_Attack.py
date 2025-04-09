def ascii_digit_pairs_for_xor(xor_val):
    unique_pairs = set()
    for d1 in range(10):
        ascii_d1 = ord(str(d1))
        for d2 in range(10):
            ascii_d2 = ord(str(d2))
            if ascii_d1 ^ ascii_d2 == xor_val:
                pair = tuple(sorted((d1, d2)))
                unique_pairs.add(pair)
    return list(unique_pairs)

def analyze_three_ciphertexts(c1, c2, c3):
    min_len = min(len(c1), len(c2), len(c3))
    
    xor12 = [int(c1[i], 2) ^ int(c2[i], 2) for i in range(min_len)]
    xor13 = [int(c1[i], 2) ^ int(c3[i], 2) for i in range(min_len)]
    xor23 = [int(c2[i], 2) ^ int(c3[i], 2) for i in range(min_len)]

    print("Predictions per digit position:\n")

    for i in range(min_len):
        pairs12 = ascii_digit_pairs_for_xor(xor12[i])
        pairs13 = ascii_digit_pairs_for_xor(xor13[i])
        pairs23 = ascii_digit_pairs_for_xor(xor23[i])

        # Gather candidate digits
        p1 = sorted(set(a for a, b in pairs12) & set(a for a, b in pairs13))
        p2 = sorted(set(b for a, b in pairs12) & set(a for a, b in pairs23))
        p3 = sorted(set(b for a, b in pairs13) & set(b for a, b in pairs23))

        print(f"Digit {i+1}:")
        print(f"  p1 ∈ {p1}")
        print(f"  p2 ∈ {p2}")
        print(f"  p3 ∈ {p3}")
        print("")

def stream_cipher(plainText, IV):
    return [format(ord(ch) ^ IV, '08b') for ch in plainText]


p1 = "123234"
p2 = "43"
p3 = "789345"

IV = int("10110101", 2)

c1 = stream_cipher(p1, IV)
c2 = stream_cipher(p2, IV)
c3 = stream_cipher(p3, IV)

analyze_three_ciphertexts(c1, c2, c3)