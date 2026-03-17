from pathlib import Path


CHUNK_SIZE = 4096  # 4KB，可调


def build_translation_table(shift: int) -> dict:
    """
    Build translation table for Caesar cipher using str.maketrans.
    Supports both lowercase and uppercase letters.
    """
    shift = shift % 26

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    shifted_lower = lower[shift:] + lower[:shift]
    shifted_upper = upper[shift:] + upper[:shift]

    return str.maketrans(lower + upper, shifted_lower + shifted_upper)


def process_file(input_path: str, output_path: str, shift: int, mode: str):
    """
    Core file processing function.

    Parameters:
    - input_path: path to input file
    - output_path: path to output file
    - shift: Caesar shift value
    - mode: "encrypt" or "decrypt"
    """
    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if mode not in ("encrypt", "decrypt"):
        raise ValueError("mode must be 'encrypt' or 'decrypt'")

    if mode == "decrypt":
        shift = -shift

    table = build_translation_table(shift)

    with input_path.open("r", encoding="utf-8") as f_in, \
         output_path.open("w", encoding="utf-8") as f_out:

        for chunk in iter(lambda: f_in.read(CHUNK_SIZE), ""):
            f_out.write(chunk.translate(table))


def encrypt_file(input_path: str, output_path: str, shift: int):
    """
    Encrypt a file using Caesar cipher.
    """
    process_file(input_path, output_path, shift, mode="encrypt")


def decrypt_file(input_path: str, output_path: str, shift: int):
    """
    Decrypt a file using Caesar cipher.
    """
    process_file(input_path, output_path, shift, mode="decrypt")