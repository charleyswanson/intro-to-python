def greet(code):
    match code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'
        
def extract_region(locale):
    region = locale[3:5]
    return region

def extract_language(locale):
    language = locale[0:2]
    return language

def local_greet(locale):
    local_lang = extract_language(locale)
    local_region = extract_region(locale)

    match local_lang:
        case 'en':
            match local_region:
                case 'US':
                    return 'Hey!'
                case 'GB':
                    return 'Hello!'
                case 'AU':
                    return 'Howdy!'
        case _:
            return greet(local_lang)

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!
print(local_greet('sv_MA.UTF-8'))       # Hej!