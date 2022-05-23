initial_words = ['разработка', 'администрирование', 'protocol', 'standard']

print(initial_words)

encoded_words = [word.encode('utf-8') for word in initial_words]

print(encoded_words)

decoded_words = [word.decode('utf-8') for word in encoded_words]

print(decoded_words)
