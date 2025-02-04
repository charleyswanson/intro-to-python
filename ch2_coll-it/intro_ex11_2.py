people_list = {
    'Name': 'Country',
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'Sanyu': 'Uganda',
    'Yoshitaka': 'Japan',
}

test_name = input('How about a name? ')

if test_name in people_list:
    print(f'{test_name}\'s country is {people_list[test_name]}')
else:
    print('I don\'t know that person.')