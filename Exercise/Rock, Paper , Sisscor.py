import random
def game(Computer , your):
    if Computer == your:
        return None

    # Check for all possibilities when Computeruter chose s
    elif Computer == 'r':
        if your=='p':
            return True
        elif your=='s':
            return False
    
    # Check for all possibilities when Computeruter chose w
    elif Computer == 'p':
        if your=='r':
            return False
        elif your=='s':
            return True
    
    # Check for all possibilities when Computeruter chose g
    elif Computer == 's':
        if your=='p':
            return False
        elif your=='r':
            return True 
