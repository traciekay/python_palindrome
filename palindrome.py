# A function that checks if a string is a palindrome

def is_palindrome(string):
    if type(string) != str:
        return False
    string = string.upper().replace(' ','')
    string_1=''

    #list comprehension

    for char in string:
        if char.isalnum():
            string_1 += char
    reversed_string = string_1[::-1]
    if reversed_string == string_1:
        return True
    return False

print(is_palindrome("A Toyota's a Toyota"))
