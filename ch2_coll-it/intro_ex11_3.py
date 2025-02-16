# You need to write some Python code to determine the country name associated with one of the listed names. Your code should include the data structure(s) you need and at least one test case to ensure the code works.

# Alice	USA
# Francois	Canada
# Inti	Peru
# Monika	Germany
# Sanyu	Uganda
# Yoshitaka	Japan

people = {'Alice': 'USA', 
          'Francois': 'Canada', 
          'Inti': 'Peru',
          'Monika': 'Germany',
          'Sanyu': 'Uganda',
          'Yoshitaka': 'Japan',
}   

test_name = input('How about a name? ')
print(f'{test_name} is from {people[test_name]}')