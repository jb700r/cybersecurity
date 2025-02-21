alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
spelling_alphabet = [
    'Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliett', 
    'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 
    'Uniform', 'Victor', 'Whiskey', 'X-ray', 'Yankee', 'Zulu'
]


def main():
    user_message = input('Enter a message to convert to the spelling alphabet: ')
    result = ''

    for char in user_message:
        if char.isalpha():
            result += spelling_alphabet[alphabet.index(char.lower())] + ' '
        elif char == ' ':
            result += '(space) '
        elif char.isdigit():
            result += f'{char}'

    print(result)
   

if __name__ == '__main__':
    main()