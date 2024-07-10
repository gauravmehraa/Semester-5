def encrypt(plaintext, depth):
    ciphertext = ''
    rows = [[] for _ in range(depth)]
    current = 0
    direction = 'S'
    for char in plaintext:
        rows[current].append(char)
        if direction == 'S': current += 1
        if direction == 'N': current -= 1
        if current == depth-1 or current == 0:
            if direction == 'S': direction = 'N'
            else: direction = 'S'
    for row in rows:
        for char in row: ciphertext += char
    return ciphertext

def decrypt(ciphertext, depth):
    plaintext = ''
    return plaintext

text = input("Enter message: ")
depth = int(input("Enter depth: "))
e = encrypt(text, depth)
print(f"\nEncrypted message: {e}")
d = decrypt(e, depth)
print(f"Decrypted message: {d}")