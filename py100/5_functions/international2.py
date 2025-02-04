# Building on your solutions from the previous exercises, write a function local_greet that takes a locale as input, and returns a greeting. The locale lets us greet people from different countries appropriately, even when they share a common language, for example:

# When implementing local_greet, make sure you re-use your extract_language, extract_region, and greet functions from the previous exercises.

def local_greet(locale):
    language = locale[0:2]
    region = locale[3:5]
    match language:
        case 'en':
            match region:
                case 'US':
                    return 'Hey!'
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