alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
def encrypt_decrypt(direction, text, shift):
    end_text = ""
    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift
            new_letter = alphabets[new_position]
            end_text += new_letter
        else:
            end_text += char
    print(f"The {direction}d message is:\n{end_text}")


print("Message Encryption - Decryption\n")

start_game = True

while start_game:
    direction = input("Type encode to encrypt message, Type decode to decrypt message:\n")

    text = input("Type your message:\n").lower()

    shift = int(input("Enter the shift number:\n"))
    shift = shift % 26
    encrypt_decrypt(direction, text, shift)

    replay = input('Do you want to continue again : Type "Yes" to continue , Type "No" to end game.\n').lower()
    if replay == "no":
        start_game = False
        print("Goodbye")

