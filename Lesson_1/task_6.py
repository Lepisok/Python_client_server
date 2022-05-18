from chardet import detect

with open('test_file.txt', 'rb') as source:
    data = source.read()

detected = detect(data)
print(f"File encoding by default: {detected['encoding']} "
      f"with probability {detected['confidence'] * 100:.1f}%")

with open('test_file.txt', 'r', encoding='utf-8', errors='replace') as source:
    forced_utf_8 = source.read()

print(forced_utf_8)
