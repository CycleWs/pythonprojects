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
                    rest -= 26
                    num = 0
                    num += rest
                
                if num < 0:
                    num += len(letters)
                    
                encrypted_word += letters[num]
                
            else:
                encrypted_word += word_letters
                
        print("Your sentence with Caesar Cipher is: " + encrypted_word)
    
    def decrypter(self,word,key):
        letters = self.alphabet
        
        combinations_sentence = ''
        for word_letters in word:
            x = word_letters
            
            if x in letters:
                num = letters.find(word_letters)
                num -= key
                
                if num > 25:
                    num = 0
                
                combinations_sentence += letters[num]
            else:
                combinations_sentence += word_letters
                
        print("The original sentence of the Caesar Cipher is: "+combinations_sentence)
    
    def Break_Cipher(self,word):
        keys = 0
        while(keys < 26):
            keys += 1
            letters = self.alphabet
            
            combinations_sentence = ''
            for word_letters in word:
                x = word_letters
                
                if x in letters:
                    num = letters.find(word_letters)
                    num -= keys
                    
                    if num > 25:
                        num = 0
                    
                    combinations_sentence += letters[num]
                else:
                    combinations_sentence += word_letters
                    
            print("Key #:",keys," sentence: ",combinations_sentence)

