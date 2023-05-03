from caesarcipher import Caesar_Cipher

cipher = Caesar_Cipher()

choice = int(input("Type 1 if you want to encrypt a word| Type 2 if you want to decrypt: "))

if choice == 1:
    word_to_encrypt = input("Type a word to encrypt to Caesar Cipher: ")
    encrypter_key = int(input("Type a key number to encrypt your word: "))
    cipher.encrypter(word_to_encrypt, encrypter_key)

elif(choice == 2):
    word_to_decrypt = input("Type the word that you want to decrypt: ")
    encrypter_key = int(input("Type the key to decrypt your cipher: "))
    cipher.decrypter(word_to_decrypt, encrypter_key)