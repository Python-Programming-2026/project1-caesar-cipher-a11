from caesar_cipher.cipher import encrypt_text, decrypt_text


def test_encrypt_basic():
    assert encrypt_text("abc", 3) == "def"


def test_decrypt_basic():
    assert decrypt_text("def", 3) == "abc"


def test_wrap_around():
    assert encrypt_text("xyz", 3) == "abc"


def test_case_preserved():
    assert encrypt_text("AbC", 3) == "DeF"


def test_non_alpha():
    assert encrypt_text("hello, world!", 3) == "khoor, zruog!"