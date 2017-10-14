# A function that checks if a string is a palindrome

def is_palindrome(string)
    if type(string) != str:
        return False
    string = string.upper().replace(' ','')
    reversed_string = string[::-1]
    if reversed_string == string:
        return True
    return False

print(is_palindrome("A Toyota's a Toyota"))
