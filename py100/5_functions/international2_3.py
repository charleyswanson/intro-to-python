# Building on your solutions from the previous exercises, write a function local_greet that takes a locale as input, and returns a greeting. The locale lets us greet people from different countries appropriately, even when they share a common language, for example:

def local_greet(locale):
    
    def extract_language(locale):
        global language
        language = locale[0:2]
        return language

    extract_language(locale)

    def extract_region(locale):
        global region
        region = locale[3:5]
        return region
    
    extract_region(locale)

    match language:
        case 'en':
            match region:
                case 'US':
                    return 'Hi!'
                case 'GB':
                    return 'Hello!'
                case 'AU':
                    return 'Howdy!'
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

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!