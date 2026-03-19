class Caesar_Cipher():
    
    def __init__(self):
        self.alphabet_without_vowel = 'bcdfghjklmnpqrstvwxyzш'
        self.alphabet_vowels = 'aeiouёыюя'
    
    def encrypter(self,word,key):
        consoants = self.alphabet_without_vowel 
        vowels = self.alphabet_vowels
        key_to_vowels = 0
        if key > vowels.__len__():
            key_to_vowels = vowels.__len__() - 1
            
        encrypted_word = ''
        for word_letters in word:
            x = word_letters
            
            if x in consoants:
                num = consoants.find(word_letters)
                num += key
                rest = num
                
                if num > consoants.__len__():
                    #if the letter is "higher" than Z, restart the alphabet_without_vowel  from letter A
                    rest -= consoants.__len__() + 1
                    num = 0
                    num += rest
                
                if num < 0:
                    num += len(consoants)
                    
                encrypted_word += consoants[num]
                
            elif x in vowels:
                
                key_to_vowels = vowels.find(word_letters)
                key_to_vowels += key
                rest = key_to_vowels
                
                if key_to_vowels > vowels.__len__():
                    rest -= vowels.__len__() + 1
                    key_to_vowels = 0
                    key_to_vowels += rest
                
                if key_to_vowels < 0:
                    key_to_vowels += len(vowels)
                    
                encrypted_word += vowels[key_to_vowels]        
            else:
                encrypted_word += word_letters
                
        print("Your sentence with Caesar Cipher is: " + encrypted_word)
    
    def decrypter(self,word,key):
        letters = self.alphabet_without_vowel 
        
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
            letters = self.alphabet_without_vowel 
            
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

