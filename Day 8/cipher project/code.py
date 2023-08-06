alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n")) 


def encrypt(text,shift):
    encrypted_text =''
    for i in text:
        idx = alphabet.index(i) 
        x = 26 - idx 
        if x <= shift:
            encrypted_text += alphabet[shift - x] 
        else:
            encrypted_text += alphabet[idx +shift]
    print(encrypted_text)

def decrypt(text,shift):
    decrypted_text =''
    for i in text:
        idx = alphabet.index(i) - shift
        decrypted_text += alphabet[idx]
    print(decrypted_text)

if direction == 'encode':
    encrypt(text,shift)
elif direction == 'decode':
    decrypt(text,shift)

