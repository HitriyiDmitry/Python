my_translate = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate(english):
    return my_translate.get(english)

print(num_translate(input('Ввкдите прописью число от 0 до 10 на английском: ')))
