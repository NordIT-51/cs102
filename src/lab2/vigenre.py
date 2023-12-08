def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    >>> encrypt_vigenere("Python3", "a") #Добавил тест на работу с числами и регистром
    'Python3'
    """
    ciphertext = ""
    keyword = keyword.upper()
    key = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[key]) - 65
            if char.isupper():
                ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
            key = (key + 1) % len(keyword)
        else:
            ciphertext += char
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    >>> encrypt_vigenere("Python3", "a") #Добавил ещё один тест на работу с числами и регистром
    'Python3'
    """
    plaintext = ""
    keyword = keyword.upper()
    key = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[key]) - 65
            if char.isupper():
                plaintext += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - shift - 97) % 26 + 97)
            key = (key + 1) % len(keyword)
        else:
            plaintext += char
    return plaintext