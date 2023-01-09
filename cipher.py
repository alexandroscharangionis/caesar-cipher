from art import logo

# Alphabet is doubled so if we try to shift letters towards the end of the alphabet, new_index variable works and doesn't trigger "list out of range" error
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(text, shift_amount, operation):
    output_text = ''
    # Multiply by -1 so new_index is calculated negatively if operation is 'decode'
    if operation == 'decode':
        shift_amount *= -1
    for char in text:
        if char in alphabet:
            current_index = alphabet.index(char)
            new_index = current_index + shift_amount
            output_text += alphabet[new_index]
        else:
            output_text += char
    print(
        f"The {'encrypted' if operation == 'encode' else 'decrypted'} text is '{output_text}'")


print(logo)

while True:
    operation = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Using modulo operand on shift ensured that program doesn't break if user inputs a number that's too big:
    shift = shift % 26

    if operation != 'decode' and operation != 'encode':
        print('Input not recognized')
    else:
        caesar_cipher(text, shift, operation)
        if input('Type "yes" if you want to go again, or type anything else to quit.\n').lower() == 'yes':
            continue
        else:
            print('Goodbye')
            break
