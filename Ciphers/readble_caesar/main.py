from caesarcipher import Caesar_Cipher

cipher = Caesar_Cipher()

print(" Caesar cipher is a type of cryptography that allows you write a sentence or a text\n",
    "and using a specific number key, jump the number times of the key in alphabet by \n",
    "that way, encrypting your text\n\n")

choice = int(input("Type 1 if you want to encrypt a word| Type 2 if you want to decrypt| Type 3 if you want to break any cipher sentence:  "))


if choice == 1:
    word_to_encrypt = input("Type the sentence to encrypt to Caesar Cipher: ")
    encrypter_key = int(input("Type a key number to encrypt your word between 1 and 25: "))
    word_to_encrypt = word_to_encrypt.lower()
    cipher.encrypter(word_to_encrypt, encrypter_key)
