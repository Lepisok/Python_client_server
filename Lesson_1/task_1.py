list_1 = ['разработка', 'сокет', 'декоратор']
list_2 = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
]


def check_string(arg: str) -> None:
    print(
        f'Type: {type(arg)}. Length: {len(arg)}.'
        f'\nValue: {arg}\n'
    )


for element in list_1:
    check_string(element)

for element in list_2:
    check_string(element)
