def interpolation(text, dictionary):
    for key in dictionary:
        text_name = '{' + key + '}'
        text = text.replace(text_name, dictionary[key])
    return text


test_cases = [
    (('Hello, I am {name}', {'name': 'Kenny'}), 'Hello, I am Kenny'),
    (("Hello! My name is {name}, I am {age} years old. I am a {kind}.", {'name': 'Bob', 'age': '2', 'kind': 'flower'}), 'Hello! My name is Bob, I am 2 years old. I am a flower.')
]

for test_case in test_cases:
    input_args, expected_result = test_case
    real_result = interpolation(*input_args)
    print(f'Testing {input_args}: {real_result == expected_result}')
