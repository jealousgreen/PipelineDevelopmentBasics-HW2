import pytest
from simple_crypto.xor_cipher import xor_encrypt, xor_decrypt


def test_xor_encrypt_decrypt_roundtrip():
    text = "attack at dawn"
    key = "secret-key"
    cipher = xor_encrypt(text, key)
    assert isinstance(cipher, bytes)

    decrypted = xor_decrypt(cipher, key)
    assert decrypted == text


def test_xor_empty_key_raises():
    from simple_crypto.xor_cipher import xor_bytes
    with pytest.raises(ValueError):
        xor_bytes(b"data", b"")
