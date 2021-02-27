
s = 'bbzzshdtaatuekdotmsfjfjjjturodlsacmg'

d = {}

def firstLetterrepeat(s):
    for letter in s:
        d[letter] = d.get(letter, 0) + 1
        if d[letter] > 1:
            return letter

print(firstLetterrepeat(s))

def firstLetterNotRepeat(s):

    d = {}

    for letter in s:
        d[letter] = d.get(letter, 0) + 1
    
    for letter in s:
        if d[letter] == 1:
            return letter
    return None
        
print(firstLetterNotRepeat(s))


n = 4378

def roundNumber(n):
    q = n // 10
    r = n % 10

    r = 10 if r >= 5 else 0
    
    res = 10 * q + r

    print(res)

roundNumber(n)



s = "welcome to geeksforgeeks"

def missingChars(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    s = s.lower()

    for letter in s:
        alphabet = alphabet.replace(letter, '')
    
    return alphabet

print(missingChars(s))


arr = [2, 73, 95, 59, 96, 2]

def isPalyndrome(arr):

    word = ''
    
    for num in arr:
        word += str(num)
    length = len(word)

    for i in range(length):
        print(word[i])
        print(word[length -1-i])
        if word[i] != word[length - 1 - i]:
            return False
    return True

print(isPalyndrome(arr))