import os, re

for _,_,files in os.walk('.'):
    for file in files:
        print(file)
        with open(file, encoding='utf-8') as f:
            text = f.read()

        text = re.sub('Список словарных статей', 'Список словарных статей', text)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)
