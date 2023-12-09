def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            if letter.isupper():
                new = chr((ord(letter) + shift - 65) % 26 + 65)
            else:
                new = chr((ord(letter) + shift - 97) % 26 + 97)
            ciphertext += new
        else:
            ciphertext += letter
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            if letter.isupper():
                new_letter = chr((ord(letter) - shift - 65) % 26 + 65)
            else:
                new_letter = chr((ord(letter) - shift - 97) % 26 + 97)
            plaintext += new_letter
        else:
            plaintext += letter
    return plaintext