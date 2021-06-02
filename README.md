## Python tasks

This is a mini-collection of python tasks.

## _Task 0_
Become familiar with the concept of a 'class' and the principles of object-oriented programming.

Launch: `python3 0_class.py`

## _Task 1_
The program should display numbers from 1 to 100. Also:

- If the number is a multiple of three then the program should display the word «Fizz»
- If the number is a multiple of five then the program should display the word «Buzz»
- If the number is a multiple of fifteen then the program should display the word «FizzBuzz»

Launch: `python3 1_fizzbuzz.py`

## _Task 2_
The program should read the entered five-digit number. After that, each digit must be displayed on a new line.

For example: 
> The number is 10890
> 
> 1 digit is 1   
> 2 digit is 0   
> 3 digit is 8   
> 4 digit is 9   
> 5 digit is 0

Launch: `python3 2_decomposition.py`

## _Task 3_
Implement the Selection sort algorithm and arrange the numbers in ascending order.

For example:
>Input: [0, 3, 24, 2, 3, 7]  
>Output: [0. 2. 3. 3. 7. 24]

Launch: `python3 3_selection_sort.py`
## _Task 4_
The program should replace tab character with four spaces and back. The input is a file.

Launch: `python3 4_tab.py`

## _Task 5_
The program should interpolation some patterns in the string. It is necessary to replace the appearance of the patterns with their meaning from the dictionary. 

For example:
>String = 'Hello! My name is {name}. I am {age} years old'   
>Data = ['name': 'Bob', 'age': '2']   
> Output = 'Hello! My name is Bob. I am 2 years old'

Launch: `python3 5_interpol.py`

## _Task 6_
The program should delete the column containing the preset digit in the matrix.

For example:
>Input_array = [[1,2,5], [6,7,9]]  
> Preset_digit = 2  
>Output_array = [[1,5], [6,9]]

Launch: `python3 6_matrix.py`

## _Task 7_
The program should find maximum value in some object.

For example:
>max([1, 2, 3], 6, a=12, b=18)
> 
> 18 

Launch: `python3 7_max.py`

## _Task 8_
Implementation of internal function 'enumerate'.

Launch: `python3 8_enumeration.py`

## _Task 9_
Continue working with a 'class' - objects. The program should have class 'Man', which display 'I'm not ready yet' and class 'Pupil', which display the same thing with a pause of 3-6 seconds.

Launch: `python3 9_class_2.py`

## _Task 10_
We need to write a class 'WrapStrToFile' that will have one computed property called 'content'. When trying to read the content property, the file must be opened inside the property code using the 'filepath' attribute. If the file does not exist, then the text 'File does not exist yet' should be returned. When assigning a value to the "content" property, the file must be open for writing, and the content must be written. When removing the "content" attribute, the file must also be removed.

For example:
>wstf = WrapStrToFile()
> 
> print(wstf.content)    # Output: File doesn't exist
> 
>wstf.content = 'test str'
> 
>print(wstf.content)     # Output: test_str
> 
>wstf.content = 'text 2'
> 
>print(wstf.content)     # Output: text 2
> 
>del wstf.content # after this file does not exist

Launch: `python3 10_WrapStrToFile.py`

## _Task 11_ 
We need to write a context manager that measures and displays the execution time of the code inside it.

Launch: `python3 11_context_manager.py`

## _Task 12_
The function receives the input sequence of numbers "source" and the multiplier "m". At the output of the function, a new sequence is expected based on "source" where each term has been multiplied by "m". If source was not specified then the sequence [1,2,3] is taken.

_There are several ways in the file to solve this tasks: with and without generators._

Launch: `python3 12_generators.py`

## _Task 13_
Examining the documentation for the 'Itertools' library to find functions that will give you
correct answers to the next questions:
- The function must accept three arrays ([1, 2, 3], [4, 5], [6, 7]) and return
only one array ([1, 2, 3, 4, 5, 6, 7])
- The function takes an array (['hello', 'i', 'write', 'cool', 'code']) and returns
an array of elements with a length of at least five (['hello', 'write'])  
- The function outputs to the string 'password' all possible combinations of the form
([('p', 'a', 's', 's'), ('p', 'a', 's', 'w'), ('p', 'a', 's', 'o'), ...)  

Launch: `python3 13_itertools.py`