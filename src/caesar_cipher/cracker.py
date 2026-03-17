"""
Experimental module for Caesar cipher cracking.
Currently not exposed in CLI.
"""

from collections import Counter
from caesar_cipher.cipher import decrypt_text


ENGLISH_FREQ = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0,
    'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3,
    'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4,
    'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5,
    'V': 1.0, 'K': 0.8, 'J': 0.15, 'X': 0.15,
    'Q': 0.1, 'Z': 0.07
}


def score_text(text: str) -> float:
    """
    Score how likely a text is English based on letter frequency.
    Higher score = more likely English.
    """
    text = text.upper()

    # 统计字母
    counts = Counter(c for c in text if c.isalpha())

    total = sum(counts.values())
    if total == 0:
        return 0

    score = 0.0

    for letter, freq in ENGLISH_FREQ.items():
        observed = counts.get(letter, 0) / total * 100
        score += freq * observed

    return score


def crack_caesar(ciphertext: str):
    """
    Try all 26 shifts and return the best result.

    Returns:
    - best_shift
    - best_plaintext
    - best_score
    """
    best_shift = 0
    best_text = ""
    best_score = -1

    for shift in range(26):
        decrypted = decrypt_text(ciphertext, shift)
        score = score_text(decrypted)

        if score > best_score:
            best_score = score
            best_shift = shift
            best_text = decrypted

    return best_shift, best_text, best_score


def brute_force_all(ciphertext: str):
    """
    Return all possible decryptions (for debugging / learning).
    """
    results = []

    for shift in range(26):
        decrypted = decrypt_text(ciphertext, shift)
        results.append((shift, decrypted))

    return results