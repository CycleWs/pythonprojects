class Caesar_Cipher():
    
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    def encrypter(self,word,key):
        letters = self.alphabet
        
        encrypted_word = ''
        for word_letters in word:
            x = word_letters
            
            if x in letters:
                num = letters.find(word_letters)
                num += key
                rest = num
                
                if num > 25:
                    #if the letter is "higher" than Z, restart the alphabet from letter A
                    rest -= 25
                    num = -1
                    num += rest
                
                if num < 0:
                    num += len(letters)
                    
                encrypted_word += letters[num]
                
            else:
                encrypted_word += word_letters
                
        print("Your word in Caesar Cipher is: " + encrypted_word)
    
    def decrypter(self,word,key):
        letters = self.alphabet
        
        decrypted_word = ''
        for word_letters in word:
            x = word_letters
            
            if x in letters:
                num = letters.find(word_letters)
                num -= key
                
                if num > 25:
                    num = 0
                
                decrypted_word += letters[num]
            else:
                decrypted_word += word_letters
                
        print("The original word of the Caesar Cipher is: "+decrypted_word)
        