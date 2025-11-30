def caesar_encrypt(text: str, shift: int) -> str:
    """Шифр Цезаря для латинского алфавита, регистр сохраняем."""
    result = []

    for ch in text:
        if 'a' <= ch <= 'z':
            base = ord('a')
            offset = (ord(ch) - base + shift) % 26
            result.append(chr(base + offset))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            offset = (ord(ch) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            # не буквы не трогаем
            result.append(ch)

    return "".join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    """Дешифрование Цезаря — просто сдвиг в обратную сторону."""
    return caesar_encrypt(text, -shift)