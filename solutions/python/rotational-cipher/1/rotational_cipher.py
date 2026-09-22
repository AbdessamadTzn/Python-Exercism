def rotate(text, key):
    cipher_output = ""
    for i in range(len(text)):
        letter = text[i]
        if letter.isalpha():
            if letter.isupper():
                in_alpha_range = ((ord(letter) - 65) + key) % 26
                to_ascii = chr(in_alpha_range + 65)
                cipher_output+=to_ascii
            else:
                in_alpha_range = ((ord(letter) - 97) + key) % 26
                to_ascii = chr(in_alpha_range + 97)
                cipher_output+=to_ascii                
                
        else:
            cipher_output+=letter
 
        
            

    return cipher_output
    
