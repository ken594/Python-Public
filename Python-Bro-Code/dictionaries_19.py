### Section 19: Dictionary = A changeable, unordered collection of unique key:value pairs
#               Fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

## update
# capitals.update({'Germany': 'Berlin'})
# capitals.update({'USA': 'Las Vegas'})

## pop
capitals.pop('China')

## clear
capitals.clear()

# print(capitals['Russia'])
# print(capitals['Germany'])
# print(capitals.get('Germany'))

## print only the keys
# print(capitals.keys())

## print only the values
# print(capitals.values())

## print the entier dict
# print(capitals.items())

for key,value in capitals.items():
    print(key, value)