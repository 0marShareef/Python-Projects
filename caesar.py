def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(',
               '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_',
               '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

    def encrypt(text1, shift1):
        coded_text = ""
        for i in text1:
            if i == " ":
                coded_text += " "
            elif i in symbols:
                coded_text += i
            else:
                letter_index = alphabet.index(i)
                shift_index = letter_index + shift1
                coded_text += alphabet[shift_index]
        print(f"The encoded text is: {coded_text}")

    def decrypt(text2, shift2):
        decoded_text = ""
        for i in text2:
            if i == " ":
                decoded_text += " "
            elif i in symbols:
                decoded_text += i
            else:
                letter_index = alphabet.index(i)
                shift_index = letter_index - shift2
                decoded_text += alphabet[shift_index]
        print(f"The decoded text is: {decoded_text}")

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'quit' to stop:\n")
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    elif direction == "quit":
        quit()
    else:
        print("Please enter a valid command.")
        main()


main()
