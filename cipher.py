# Alphabet is doubled so if we try to shift letters towards the end of the alphabet, new_index variable works and doesn't trigger "list out of range" error
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift_amount):
    encrypted_text = ''
    for letter in text:
        original_index = alphabet.index(letter)
        new_index = original_index + shift_amount
        new_letter = alphabet[new_index]
        encrypted_text += new_letter
    print(f"The encrypted text is '{encrypted_text}'")


def decrypt(encrypted_text, shift_amount):
    decrypted_text = ''
    for letter in encrypted_text:
        current_index = alphabet.index(letter)
        original_index = current_index - shift_amount
        new_letter = alphabet[original_index]
        decrypted_text += new_letter
    print(f"The decrypted text is '{decrypted_text}'")


while True:
    operation = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if operation == 'encode':
        encrypt(text, shift)
        break
    elif operation == 'decode':
        decrypt(text, shift)
        break
    else:
        print('Input not recognized')
