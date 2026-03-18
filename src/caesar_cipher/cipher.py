def normalize_shift(shift: int) -> int:
    """
    将偏移量规范化到 [0, 25] 范围内。
    利用 % 取模运算符实现数值的周期性循环。
    """
    return shift % 26


def shift_char(char: str, shift: int) -> str:
    """
    对单个字符进行位移。
    使用if 选择结构、ord/chr 内置函数。
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
    使用凯撒密码加密完整文本。
    使用for 循环遍历，join 字符串拼接。
    """
    return "".join(shift_char(c, shift) for c in text)


def decrypt_text(text: str, shift: int) -> str:
    """
    解密与加密相同
    """
    return encrypt_text(text, -shift)