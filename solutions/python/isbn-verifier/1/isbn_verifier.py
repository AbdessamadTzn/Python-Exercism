import re 
def is_valid(isbn):

    reg_expression = r'^\d-?\d{3}-?\d{5}-?[\dX]$'
    
    if not re.match(reg_expression, isbn):
        return False

    isbn_ = isbn.replace("-", "")

    counter = 10
    res = 0
    for x in isbn_ :
        if x=='X':
            c = 10*counter
        else:
           c = int(x)*counter
            
        res += c
        counter -=1
        
    return res % 11 == 0
            
            
