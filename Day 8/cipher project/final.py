alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols = ['#','@','!','$','*','^','%','(',')',':',';',' ','"',"'"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n")) 

if shift < 27 :
    def encrypt(text,shift):
        encrypted_text =''
        
        for i in text:
            if i in alphabet:
                idx = alphabet.index(i)
                encrypted_text += alphabet[idx+shift]
            elif i in symbols:
                encrypted_text += i
        print(encrypted_text)

    def decrypt(text,shift):
        decrypted_text =''
        for i in text: 
            if i in alphabet:
                idx = alphabet.index(i) 
                decrypted_text += alphabet[idx-shift]
            elif i in symbols:
                decrypted_text += i
        print(decrypted_text)

    if direction == 'encode':
        encrypt(text,shift)
    elif direction == 'decode':
        decrypt(text,shift)

    while True:
        inp = input("Type 'yes' if you want to go again. Otherwise 'No',").lower()
        if inp == 'yes':
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n")) 
            if direction == 'encode':
                encrypt(text,shift)
            elif direction == 'decode':
                decrypt(text,shift)
        else:
            print('Good Bye')
            break


else:
    print('Shift is bigger than alphates total number')