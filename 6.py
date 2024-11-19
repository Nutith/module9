def all_variants(text):
    for i in range(1, len(text)+1):
        for j in range(len(text)):
            if j + i > len(text):
                continue

            yield text[j:j+i]


a = all_variants("abc")
for i in a:
    print(i)
