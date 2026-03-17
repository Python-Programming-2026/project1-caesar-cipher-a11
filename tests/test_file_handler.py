import os
from caesar_cipher.file_handler import encrypt_file, decrypt_file


def test_file_encrypt_decrypt(tmp_path):
    input_file = tmp_path / "input.txt"
    encrypted_file = tmp_path / "encrypted.txt"
    decrypted_file = tmp_path / "decrypted.txt"

    # 写入测试内容
    input_file.write_text("hello world")

    # 加密
    encrypt_file(str(input_file), str(encrypted_file), 3)

    # 解密
    decrypt_file(str(encrypted_file), str(decrypted_file), 3)

    result = decrypted_file.read_text()

    assert result == "hello world"