from pathlib import Path


CHUNK_SIZE = 4096  # 一次转换4KB，可调


def build_translation_table(shift: int) -> dict:
    """
    为优化较大文本性能，使用 str.maketrans 构建字母映射表。
    通过字符串切片和字典实现的字符映射。
    """
    shift = shift % 26

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    shifted_lower = lower[shift:] + lower[:shift]
    shifted_upper = upper[shift:] + upper[:shift]

    return str.maketrans(lower + upper, shifted_lower + shifted_upper)


def process_file(input_path: str, output_path: str, shift: int, mode: str):
    """
    分块读写（对较大文件）
    变量:
    - input_path: path to input file
    - output_path: path to output file
    - shift: Caesar shift value
    - mode: "encrypt" or "decrypt"
    使用raise返回错误
    """
    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if input_path.suffix.lower() != ".txt":
        raise ValueError("Input file must be a .txt file")
    
    if output_path.suffix.lower() != ".txt":
        raise ValueError("Output file must be a .txt file")

    if mode not in ("encrypt", "decrypt"):
        raise ValueError("mode must be 'encrypt' or 'decrypt'")
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if mode == "decrypt":
        shift = -shift

    table = build_translation_table(shift)

    with input_path.open("r", encoding="utf-8") as f_in, \
         output_path.open("w", encoding="utf-8") as f_out:

        for chunk in iter(lambda: f_in.read(CHUNK_SIZE), ""):
            f_out.write(chunk.translate(table))


def encrypt_file(input_path: str, output_path: str, shift: int):
    """
    加密封装
    """
    process_file(input_path, output_path, shift, mode="encrypt")


def decrypt_file(input_path: str, output_path: str, shift: int):
    """
    解密封装
    """
    process_file(input_path, output_path, shift, mode="decrypt")