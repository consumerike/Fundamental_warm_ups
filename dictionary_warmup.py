#looping through all key-value pairs:
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(key)
    print(value)

#loop through all key-value pairs and print keys:
for key in user_0.keys():
    print(key)
#looping through the keys only is the default behavior of looping 
# through dictionaries thus this statement is equal to the one above
for key in user_0:
    print(key)

#using the keys method to determine if a key is present in a dictionary:

fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

if 'erin' not in fav_languages.keys():
    print('please take the quiz erin')

#sorted keys loop:
for name in sorted(fav_languages.keys()):
    print(name)

#loop through all values:
for languages in fav_languages.values():
    print(languages)