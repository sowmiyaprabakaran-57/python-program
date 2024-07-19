def caesar_cipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

text = input("Enter a message: ")
shift = int(input("Enter the shift value: "))
encrypted_text = caesar_cipher(text, shift)
print(f"The encrypted message is: {encrypted_text}")
