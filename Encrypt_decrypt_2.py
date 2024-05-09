alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type encode to encrypt message, Type decode to decrypt message:\n")

text = input("Type your message:\n").lower()

shift = int(input("Enter the shift number:\n"))


def encrypt_decrypt(direction, text, shift):
    cipher_text =""
    if direction == "encode":
        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encrypted message is:\n{cipher_text}")

    elif direction == "decode":
        plain_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position - shift
            new_letter = alphabet[new_position]
            plain_text += new_letter
        print(f"The decrypted message is:\n{plain_text}")


encrypt_decrypt(direction, text, shift)


