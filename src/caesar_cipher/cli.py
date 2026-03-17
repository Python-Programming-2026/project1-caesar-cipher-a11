import argparse

from caesar_cipher.cipher import encrypt_text, decrypt_text
from caesar_cipher.file_handler import encrypt_file, decrypt_file


def main():
    parser = argparse.ArgumentParser(
        prog="caesar",
        description="A command-line tool for Caesar cipher encryption and decryption."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands"
    )

    # -------- encrypt --------
    encrypt_parser = subparsers.add_parser(
        "encrypt",
        help="Encrypt text using Caesar cipher"
    )

    encrypt_parser.add_argument("text", type=str, help="Text to encrypt")
    encrypt_parser.add_argument("-s", "--shift", type=int, required=True, help="Shift value")

    # -------- decrypt --------
    decrypt_parser = subparsers.add_parser(
        "decrypt",
        help="Decrypt text using Caesar cipher"
    )

    decrypt_parser.add_argument("text", type=str, help="Text to decrypt")
    decrypt_parser.add_argument("-s", "--shift", type=int, required=True, help="Shift value")

    # -------- encrypt-file --------
    encrypt_file_parser = subparsers.add_parser(
        "encrypt-file",
        help="Encrypt a text file"
    )

    encrypt_file_parser.add_argument("input_file", type=str, help="Input file path")
    encrypt_file_parser.add_argument("output_file", type=str, help="Output file path")
    encrypt_file_parser.add_argument("-s", "--shift", type=int, required=True, help="Shift value")

    # -------- decrypt-file --------
    decrypt_file_parser = subparsers.add_parser(
        "decrypt-file",
        help="Decrypt a text file"
    )

    decrypt_file_parser.add_argument("input_file", type=str, help="Input file path")
    decrypt_file_parser.add_argument("output_file", type=str, help="Output file path")
    decrypt_file_parser.add_argument("-s", "--shift", type=int, required=True, help="Shift value")

    args = parser.parse_args()

    # -------- command routing --------
    try:
        if args.command == "encrypt":
            result = encrypt_text(args.text, args.shift)
            print(result)

        elif args.command == "decrypt":
            result = decrypt_text(args.text, args.shift)
            print(result)

        elif args.command == "encrypt-file":
            encrypt_file(args.input_file, args.output_file, args.shift)
            print(f"[OK] Encrypted file saved to: {args.output_file}")

        elif args.command == "decrypt-file":
            decrypt_file(args.input_file, args.output_file, args.shift)
            print(f"[OK] Decrypted file saved to: {args.output_file}")

        else:
            parser.print_help()

    except Exception as e:
        print(f"[ERROR] {e}")


if __name__ == "__main__":
    main()