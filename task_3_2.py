my_translate_adv = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate(english):
    if english[0].isupper():
        english = english.lower()
        return my_translate_adv.get(english).capitalize()
    else:
        return my_translate_adv.get(english)

print(num_translate(input('Ввкдите прописью число от 0 до 10 на английском: ')))