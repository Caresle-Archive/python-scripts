# Encoder only

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F',
    'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z'
]


def main():
    shift = int(input("Shift value: "))
    text = input("Message to code: ")
    text_letter = []
    text_enco = ""
    for t in text.upper():
        for idx, a in enumerate(alphabet):
            if t == a:
                if idx + shift >= len(alphabet):
                    r = abs(idx + shift - len(alphabet))
                    text_letter.append(r)
                else:
                    text_letter.append(idx + shift)
    for t in text_letter:
        for idx, a in enumerate(alphabet):
            if t == idx:
                text_enco += a
    print(text_enco)


if __name__ == '__main__':
    main()
