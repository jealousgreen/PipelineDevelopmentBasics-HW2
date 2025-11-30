import pytest
from simple_crypto.caesar import caesar_encrypt, caesar_decrypt


@pytest.mark.parametrize("text, shift, expected", [
    ("abc", 1, "bcd"),
    ("xyz", 3, "abc"),
    ("Hello, World!", 5, "Mjqqt, Btwqi!"),
])
def test_caesar_encrypt(text, shift, expected):
    assert caesar_encrypt(text, shift) == expected


@pytest.mark.parametrize("text, shift", [
    ("abc", 1),
    ("Hello, World!", 13),
    ("Python3.11", 25),
])
def test_caesar_encrypt_decrypt_inverse(text, shift):
    encrypted = caesar_encrypt(text, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    assert decrypted == text
