import yaml

UTF_SYMBOLS = 'ἄ⇄◍∑∰'

DATA = {
    'first': [f'some string {i ** 2}' for i in range(6)],
    'second': 814,
    'third': {f'key_{i}': value for i, value in enumerate(UTF_SYMBOLS)}
}

with open('data/file.yaml', 'w', encoding='utf-8') as target:
    yaml.dump(DATA, target, allow_unicode=True, default_flow_style=False)

with open('data/file.yaml', 'r', encoding='utf-8') as source:
    data_loaded = yaml.load(source, Loader=yaml.FullLoader)

print('Dictionaries is%s equal.' % ('' if DATA == data_loaded else ' not'))
