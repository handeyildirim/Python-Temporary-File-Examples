import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

with open('data.txt') as json_file:
    data = json.load(json_file)
    table_entries = ()
    for p in data['people']:
        table_entries = table_entries + (('name', p['name']),
                                         ('website', p['website']),
                                         ('from', p['from']),)
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
        print(table_entries)