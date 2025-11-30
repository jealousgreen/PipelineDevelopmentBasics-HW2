from itertools import cycle


def xor_bytes(data: bytes, key: bytes) -> bytes:
    """XOR-шифрование по байтам с повторяющимся ключом."""
    if not key:
        raise ValueError("Key must not be empty")

    return bytes(b ^ k for b, k in zip(data, cycle(key)))


def xor_encrypt(text: str, key: str, encoding: str = "utf-8") -> bytes:
    """Шифруем строку в байты."""
    return xor_bytes(text.encode(encoding), key.encode(encoding))


def xor_decrypt(cipher: bytes, key: str, encoding: str = "utf-8") -> str:
    """Расшифровываем байты обратно в строку."""
    plaintext_bytes = xor_bytes(cipher, key.encode(encoding))
    return plaintext_bytes.decode(encoding)