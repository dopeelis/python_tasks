some_text = "Hello! My name is {name}, I am {age} years old. I am a {kind}."
data = {'name': 'Bob', 'age': '2', 'kind': 'flower'}


def interpolation(text, dictionary):
    for key in dictionary:
        text_name = '{' + key + '}'
        if text_name in text:
            text = text.replace(text_name, dictionary[key])
    print(text)


interpolation(some_text, data)
