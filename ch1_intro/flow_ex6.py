# Write a function that takes a string as an argument and returns 
# an all-caps version of the string when the string is longer than 
# 10 characters. Otherwise, it should return the original string. 
# Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

words = input('text, please: ')

def caser(check_words):
    if len(check_words) > 10:
        check_words = check_words.upper()
    return check_words

new_words = caser(words)
print(f'new_words outside function: {new_words}')
print(f'words outside function: {words}')
