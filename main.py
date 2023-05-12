"""Main functions"""
import string

def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    PalavraF = string.casefold().replace(' ', '')
   
    for simbolo in string.punctuation
            PalavraF = PalavraF.replace(simbolo, "")
    
    PalavraInv = PalavraF[::-1]
    #print(f'palindromo formatado {PalavraF}')
    #print(f'palindromo invertido {PalavraInv}')
    
    if PalavraF == PalavraInv:
        return True
    else: 
        return False

if __name__ == "__main__":
    palin = input("Palíndromo teste: \n")
    is_palindrome(palin)
