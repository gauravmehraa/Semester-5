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
    rows = [[] for _ in range(depth)]
    current = 0
    direction = 'S'
    for char in ciphertext:
        rows[current].append("*")
        if direction == 'S': current += 1
        if direction == 'N': current -= 1
        if current == depth-1 or current == 0:
            if direction == 'S': direction = 'N'
            else: direction = 'S'

    char = 0
    for rail in rows:
        for pos in range(len(rail)):
            rail[pos] = ciphertext[char]
            char += 1
    
    current = 0
    direction = 'S'
    for char in ciphertext:
        plaintext += rows[current][0]
        del rows[current][0]
        if direction == 'S': current += 1
        if direction == 'N': current -= 1
        if current == depth-1 or current == 0:
            if direction == 'S': direction = 'N'
            else: direction = 'S'
    
    return plaintext

text = input("Enter message: ")
depth = int(input("Enter depth: "))
e = encrypt(text, depth)
print(f"\nEncrypted message: {e}")
d = decrypt(e, depth)
print(f"Decrypted message: {d}")