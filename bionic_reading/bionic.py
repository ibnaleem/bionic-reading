def convert_to_bionic(content: str) -> str:
    words = content.split()
    _string = ""

    for word in words:
        letter_count = len(word)
        freq = letter_count // 2
        _string += "".join(f"<b>{word[:freq]}</b>{word[freq:]} ")
    try:
        with open("bionic.md", "w+") as f:
            f.write(_string)
    except Exception as e:
        return str(e)

    return _string
