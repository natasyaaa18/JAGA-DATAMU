alphabet = 'abcdefghijklmnopqrstuvwxyz'

def ganti(text):
    text = text.lower()
    
    result = ''
    
    for char in text:
        if char.isalpha():
            result += alphabet[(alphabet.index(char) + 13) % 26]
        else:
            result += char
    return result


n = input()
print(ganti(n))