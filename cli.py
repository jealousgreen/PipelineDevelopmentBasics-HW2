import argparse
from simple_crypto import (
    caesar_encrypt,
    caesar_decrypt,
    xor_encrypt,
    xor_decrypt,
)


def main():
    parser = argparse.ArgumentParser(
        description="Simple crypto Caesar and XOR"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Caesar
    caesar_parser = subparsers.add_parser("caesar", help="Caesar cipher")
    caesar_parser.add_argument("mode", choices=["enc", "dec"], help="enc or dec")
    caesar_parser.add_argument("shift", type=int, help="shift value")
    caesar_parser.add_argument("text", help="text to process")

    # XOR
    xor_parser = subparsers.add_parser("xor", help="XOR cipher")
    xor_parser.add_argument("mode", choices=["enc", "dec"], help="enc or dec")
    xor_parser.add_argument("key", help="key string")
    xor_parser.add_argument("text", help="text (for enc) or hex bytes string (for dec)")

    args = parser.parse_args()

    if args.command == "caesar":
        if args.mode == "enc":
            print(caesar_encrypt(args.text, args.shift))
        else:
            print(caesar_decrypt(args.text, args.shift))

    elif args.command == "xor":
        if args.mode == "enc":
            cipher = xor_encrypt(args.text, args.key)
            # выводим в hex
            print(cipher.hex())
        else:
            cipher_bytes = bytes.fromhex(args.text)
            print(xor_decrypt(cipher_bytes, args.key))


if __name__ == "__main__":
    main()