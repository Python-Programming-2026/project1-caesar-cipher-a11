def normalize_shift(shift: int) -> int:
    """
    Normalize shift value to range [0, 25].
    """
    return shift % 26


def shift_char(char: str, shift: int) -> str:
    """
    Shift a single character by shift positions.
    Only letters are shifted; other characters remain unchanged.
    """
    if not char.isalpha():
        return char

    shift = normalize_shift(shift)

    if char.isupper():
        base = ord('A')
    else:
        base = ord('a')

    return chr((ord(char) - base + shift) % 26 + base)


def encrypt_text(text: str, shift: int) -> str:
    """
    Encrypt text using Caesar cipher.
    """
    return "".join(shift_char(c, shift) for c in text)


def decrypt_text(text: str, shift: int) -> str:
    """
    Decrypt text using Caesar cipher.
    """
    return encrypt_text(text, -shift)