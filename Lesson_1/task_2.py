words = ['class', 'function', 'method']


def encode_with_eval(arg: str) -> None:
    converted = eval('b\'%s\'' % arg)
    print(
        f'Type of argument is {type(converted)}. Length is {len(converted)}.'
        f'\nValue is: {converted}\n'
    )


for word in words:
    encode_with_eval(word)
