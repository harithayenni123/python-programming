# Day 8 - Caesar Cipher

from art import logo

print(logo)

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

def caesar(text, shift, direction):
    cipher_text = ""

    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            cipher_text += alphabet[new_position % 26]
        else:
            cipher_text += char

    print(f"The {direction}d text is: {cipher_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(text=text, shift=shift, direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye 👋")
