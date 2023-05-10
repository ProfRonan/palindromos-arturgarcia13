"""Main functions"""


def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    statusFormat = False
    pont = [".", ",", "!", "?"]
    PalavraF = string.casefold().replace(' ', '')
    while statusFormat == False:
        for i in PalavraF:
            for v in pont:
                if i == v:
                    PalavraF = PalavraF.replace(v, "")
        statusFormat = True
    
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
