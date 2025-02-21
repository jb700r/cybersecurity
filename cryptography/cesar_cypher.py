alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def cesar_cypher(text, shift, encrypt=True):
    text = text.lower()
    result = ''
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            if encrypt:
                result += alphabet[(index + shift) % len(alphabet)]
            else:
                result += alphabet[(index - shift) % len(alphabet)]
        else:
            result += char
    return result

def main():
    text = input('Enter text to encrypt: ')

    try:
        shift = int(input('Enter shift: '))
    except ValueError:
        print('Invalid shift value')
        return
    
    encrypted = cesar_cypher(text, shift)
    print(encrypted)
    decrypted = cesar_cypher(encrypted, shift, encrypt=False)
    print(decrypted)

if __name__ == '__main__':
    main()