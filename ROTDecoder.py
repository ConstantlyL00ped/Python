import string

stringToDecode = input("Enter your encoded string: ").lower()
rot = input("Select how much moves along string should decoder takes during element swapping: ")

def decodeROT(encodedString, whatKindOfROT):
    alphabet = string.ascii_lowercase
    decodedString = ""
    for element in stringToDecode:
        if(element not in alphabet):
            decodedString += element
            continue
        controlelementIndex = alphabet.index(element) + whatKindOfROT
        while(controlelementIndex > len(alphabet) - 1):
            controlelementIndex = controlelementIndex - len(alphabet)
        decodedString += alphabet[controlelementIndex]
    return decodedString

