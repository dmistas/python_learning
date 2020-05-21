# def digits_recursive(n, digits=[]):
#     temp = digits_recursive(n // 10, [n % 10] + digits) if n else digits or [0]
#     return temp
#
# print(digits_recursive(123456))


# def sum_digits(s):
#     return sum(map(int, s))
# s = input()
# middle = len(s) // 2  # середина
# if middle == 0 or sum_digits(s[:middle]) == sum_digits(s[-middle:]):
#     print('Счастливый')
# else:
#     print('Обычный')


# arr = [1,2,3,4,5,6,7,8,9]
# print(arr[::2])

# def checkio(number: int) -> int:
#     arr = []
#     for i in str(number):
#         if int(i):
#             arr.append(int(i))
#         else: continue
#     mul = 1
#     for j in arr:
#         mul = mul * j
#
#     return mul
#
#
# if __name__ == '__main__':
#     print('Example:')
#     print(checkio(123405))
#     print(checkio(123405555))
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(123405) == 120
#     assert checkio(999) == 729
#     assert checkio(1000) == 1
#     assert checkio(1111) == 1
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
#
#
# def find_message(text: str) -> str:
#     """Find a secret message"""
#     str = ''
#     punct = (':;!?,.- ')
#     for s in text:
#         if s == s.upper() and punct.find(s) == -1:
#             str = str + s
#
#
#     return str
#
#
# if __name__ == '__main__':
#     print('Example:')
#     print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
#
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
#     assert find_message("hello world!") == "", "Nothing"
#     assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
#
#
# # punct = ('  ! ? , . - ')
# # s = '!'
# # print(punct.find(s))
#
#
# def find_message(text: str) -> str:
#     """Find a secret message"""
#     i = 0
#     message = ""
#     while i < len(text):
#         x = text[i]
#         if x.isupper():
#             message += x
#         i += 1
#     return message
#
#
# if __name__ == '__main__':
#     print('Example:')
#     print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
#
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
#     assert find_message("hello world!") == "", "Nothing"
#     assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# Your optional code here
# You can import some modules or create additional functions


# def checkio(number: int) -> str:
#     # Your code here
#     # It's main function. Don't remove this function
#     # It's using for auto-testing and must return a result for check.
#     string = str(number)
#
#     if number % 3 == 0 and number % 5 == 0:
#         string = 'Fizz Buzz'
#     elif number % 5 == 0:
#         string = 'Buzz'
#     elif number % 3 == 0:
#         string = 'Fizz'
#
#     # replace this for solution
#     return string
#
#
# # Some hints:
# # Convert a number in the string with str(n)
#
# # These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     print('Example:')
#     print(checkio(15))
#
#     assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
#     assert checkio(6) == "Fizz", "6 is divisible by 3"
#     assert checkio(5) == "Buzz", "5 is divisible by 5"
#     assert checkio(7) == "7", "7 is not divisible by 3 or 5"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# def checkio(array):
#     """
#         sums even-indexes elements and multiply at the last
#     """
#     if not array:
#         return 0
#     i=0
#     sum = 0
#     new_arr =[]
#     for i, score in enumerate(array):
#         if i % 2 == 0:
#             new_arr.append(score)
#     for j in new_arr:
#         sum = sum + j
#     # mul = array[-1]
#     mul = sum * array[-1]
#     return mul
# # These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     print('Example:')
#     print(checkio([0, 1, 2, 3, 4, 5]))
#
#     assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
#     assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
#     assert checkio([6]) == 36, "(6)*6=36"
#     assert checkio([]) == 0, "An empty array = 0"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
# arr = []
# for i in range(10):
#     arr.append(i)
# print(arr[::2])


# def checkio(array):
#     return sum(array[::2]) * sum(array[-1:])
#
#
# # These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     print('Example:')
#     print(checkio([0, 1, 2, 3, 4, 5]))
#
# assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
#     assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
#     assert checkio([6]) == 36, "(6)*6=36"
#     assert checkio([]) == 0, "An empty array = 0"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# def best_stock(a):
#     # your code here
#     print(dir(a))
#     ret = max(a, key=a.get) #  это вообще легально?! что за key = a.get
#     return ret
# def best_stock(a):
#     # your code here
#     for k, v in a.items():
#         if v == max(a.values()):
#             return k
#
# if __name__ == '__main__':
#     print("Example:")
#     print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
#     assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
#     print("Coding complete? Click 'Check' to earn cool rewards!")


# def correct_sentence(text: str) -> str:
#     """
#         returns a corrected sentence which starts with a capital letter
#         and ends with a dot.
#     """
#     text = text[0].upper() + text [1:]
#     if text[-1] != '.':
#         text = text + '.'
#
#     return text
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(correct_sentence("greetings, friends"))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert correct_sentence("greetings, friends") == "Greetings, friends."
#     assert correct_sentence("Greetings, friends") == "Greetings, friends."
#     assert correct_sentence("Greetings, friends.") == "Greetings, friends."
#     assert correct_sentence("hi") == "Hi."
#     assert correct_sentence("welcome to New York") == "Welcome to New York."
#
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def left_join(phrases):
#     """
#         Join strings and replace "right" to "left"
#     """
#     str = ''
#     for i, word in enumerate(phrases, start=1):
#         word2 = word.replace('right', 'left')
#         str = str + word2
#         if i != len(phrases):
#             str = str + ','
#
#     return str
#
# def left_join(phrases):
#     str = ','.join(phrases).replace('right','left')
#     return str
#
# if __name__ == '__main__':
#     print('Example:')
#     print(left_join(("left", "right", "left", "stop")))

# def second_index(text: str, symbol: str) -> [int, None]:
#     """
#         returns the second index of a symbol in a given text
#     """
#     # if text.count(symbol)>=2:
#     #     count = text.find(symbol)
#     #     count2 = text.find(symbol, int(count+1))
#     #     return count2
#     if text.count(symbol)>=2:
#         return text.find(symbol, int(text.find(symbol)+1))
#     else:
#         return None
#
#
# if __name__ == '__main__':
#     print('Example:')
#     print(second_index("find the river", "e"))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert second_index("sims", "s") == 3, "First"
#     assert second_index("find the river", "e") == 12, "Second"
#     assert second_index("hi", " ") is None, "Third"
#     assert second_index("hi mayor", " ") is None, "Fourth"
#     assert second_index("hi mr Mayor", " ") == 5, "Fifth"
#     print('You are awesome! All tests are done! Go Check it!')
#
# sorted
# def checkio(numbers_array: tuple) -> list:
#     numbers_array = list(numbers_array)
#     numbers_array.sort(key=abs)
#     return numbers_array
#
# # def checkio(numbers_array: tuple) -> list:
# #     return sorted(numbers_array, key = abs)
#
#
# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     print('Example:')
#     print(list(checkio((-20, -5, 10, 15))))
#
#     def check_it(array):
#         if not isinstance(array, (list, tuple)):
#             raise TypeError("The result should be a list or tuple.")
#         return list(array)
#
#     assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
#     assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
#     assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# def checkio(*args):
#     arr = list(args)
#     if arr:
#         arr.sort()
#         return (round(arr[-1]-arr[0], 3))
#     else:
#         return 0
# print(checkio(1, 2, 3))


# def first_word(text: str) -> str:
#     """
#         returns the first word in a given text.
#     """
#     if text.find(' ') != -1:
#         return text[0:text.find(' ')]
#     else:
#         return text
#    # return text.split()[0]
#
# if __name__ == '__main__':
#     print("Example:")
#     print(first_word("Hello world"))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert first_word("Hello world") == "Hello"
#     assert first_word("a word") == "a"
#     assert first_word("hi") == "hi"
#     print("Coding complete? Click 'Check' to earn cool rewards!")


# def first_word(text: str) -> str:
#     """returns the first word in a given text."""
#     str = ''
#     punct = (':;!?,.- ')
#     for s in text:
#         if punct.find(s) == -1:
#             str = str + s
#         else:
#             str = str + ' '
#     return str.split()[0]
# def first_word(text: str) -> str:
#     """returns the first word in a given text."""
#     str = ''
#     text = text.replace('.',' ')
#     text = text.replace(',',' ')
#     return text.split()[0]

# def checkio(words: str) -> bool:
#     i = 0
#     for w in words.split():
#         if w.isalpha():
#             i += 1
#             if i == 3:
#                 return True
#         else:
#             i = 0
#     return False

# def checkio(words: str) -> bool:
#     bool_arr = [a.isalpha() for a in words.split()]
#     trois_true = [all([bool_arr[i], bool_arr[i+1], bool_arr[i+2]]) for i in range(len(bool_arr)-2)]
#     return any(trois_true)
#
#
#
# # These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     print('Example:')
#     print(checkio("Hello World hello"))
#
#     assert checkio("Hello World hello") == True, "Hello"
#     assert checkio("He is 123 man") == False, "123 man"
#     assert checkio("1 2 3 4") == False, "Digits"
#     assert checkio("bla bla bla bla") == True, "Bla Bla"
#     assert checkio("Hi") == False, "Hi"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# from operator import itemgetter
# def bigger_price(limit: int, data: list) -> list:
#     """
#         TOP most expensive goods
#     """
#     data.sort(key=itemgetter('price'), reverse=True)
#     del data[limit:]
#     return data
#
# if __name__ == '__main__':
#     from pprint import pprint
#     print('Example:')
#     pprint(bigger_price(2, [
#         {"name": "bread", "price": 100},
#         {"name": "wine", "price": 138},
#         {"name": "meat", "price": 15},
#         {"name": "water", "price": 1}
#     ]))

# def popular_words(text: str, words: list) -> dict:
#     list_text = text.lower().split()
#     result = {}
#     for templates in words:
#         i = 0
#         for word in list_text:
#             if templates == word:
#                 i +=1
#         result.update({templates:i})
#     return result
#
# if __name__ == '__main__':
#     print("Example:")
#     print(popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']))

# def between_markers(text: str, begin: str, end: str) -> str:
#     """
#         returns substring between two given markers
#     """
#     new_string = ''
#     j=0
#     for i, symbol in enumerate (text):
#         if symbol == begin:
#             j=i
#         if symbol == end:
#             new_string += text[j+1:i]
#
#     return new_string
#
# if __name__ == '__main__':
#     print('Example:')
#     print(between_markers('What is >apple<', '>', '<'))
#
#     # These "asserts" are used for self-checking and not for testing
#     assert between_markers('What is >apple<', '>', '<') == "apple"
#     assert between_markers('What is [apple]', '[', ']') == "apple"
#     assert between_markers('What is ><', '>', '<') == ""
#     assert between_markers('>apple<', '>', '<') == "apple"
#     print('Wow, you are doing pretty good. Time to check it!')

# def between_markers(text: str, begin: str, end: str) -> str:
#     """
#         returns substring between two given markers
#     """
#     if text.find(begin) == -1:
#         i = 0
#     else:
#         i = text.find(begin)+len(begin)
#     if text.find(end) == -1:
#         j = len(text)
#     else:
#         j = text.find(end)
#     return text[i:j]
#
#
# if __name__ == '__main__':
#     print('Example:')
#     print(between_markers('No [b]hi', '[b]', '[/b]'))

# from operator import itemgetter
# def checkio(text: str) -> str:
#     new_text = ''
#     result = []
#     for symbol in text:
#         if symbol.isalpha():
#             new_text += symbol
#     new_text = new_text.lower()
#     # print(new_text)
#     s = set(new_text)
#     for element in s:
#         i = 0
#         for symbol in new_text:
#             if symbol == element:
#                 i += 1
#         result.append([element, i])
#     result.sort(key=lambda elem: elem[0])
#     # print(result)
#     result.sort(key=itemgetter(1), reverse=True)
#     # print(result)
#     return result[0][0]
# def checkio(text: str) -> str: # охренеть, весь мой код можно было сделать 1 строкой?!!!!
#     text = text.lower()
#     return max(sorted(filter(str.isalpha, text)), key=text.count)
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(checkio("One"))

# from typing import List, Any
#
#
# def all_the_same(elements: List[Any]) -> bool:
#     # set converts the list into a set (mathematical entity). The length of set is 1 if the list has identical elements and 0 if the list is empty
#     return len(set(elements)) <= 1
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(all_the_same([1, 1, 1]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert all_the_same([1, 1, 1]) == True
#     assert all_the_same([0.1, 0.1, 1]) == False
#     assert all_the_same(['a', 'a', 'a']) == True
#     assert all_the_same([]) == True
#     assert all_the_same([1]) == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# import re
# def checkio(data: str) -> bool:
#     if re.search('\d', data) and len(data) >= 10 and re.search('[a-z]', data) and re.search('[A-Z]', data):
#         return True
#     else:
#         return False

# def checkio(data: str) -> bool:
#     """Checks password string and returns True or False based on whether
#     or not it meets the following characteristics of a secure password:
#     It is at least 10 characters in length, contains at least one upper
#     and one lower case letter A-Z, at least one number, and no special
#     characters."""
#
#     m = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{10,}$')
#     if m.match(data) is not None:
#         return True
#     else:
#         return False

# def time_converter_my(time):
#     arr = time.split(':')
#     if int(arr[0]) == 00:
#         return '12:'+arr[1]+' a.m.'
#     elif int(arr[0]) == 12:
#         return '12:' + arr[1] + ' p.m.'
#     elif int(arr[0])<12:
#         arr[0]  = str(int(arr[0]))
#         return ':'.join(arr) + ' a.m.'
#     else:
#         if int(arr[0])>=13:
#             arr[0] = str(int(arr[0])%12)
#         return ':'.join(arr) + ' p.m.'
#
# def time_converter(time):
#     hours,min=map(int,time.split(':'))
#     ans=f"{hours%12 if hours%12!=0 else '12'}:{min:02} {'a' if hours<12 else 'p'}.m."
#     return ans
#
# if __name__ == '__main__':
#     print("Example:")
#     print(time_converter('12:00'))

# from tkinter import *
#
#
# def clicked():
#     lbl.configure(text="Я же просил...")
#
#
# window = Tk()
# window.title("Добро пожаловать в приложение PythonRu")
# window.geometry('400x250')
# lbl = Label(window, text="Привет", font=("Arial Bold", 50))
# lbl.grid(column=0, row=0)
# btn = Button(window, text="Не нажимать!", command=clicked)
# btn.grid(column=1, row=0)
# window.mainloop()


# def checkio(data: list) -> list:
#     lst = list(filter(lambda x: data.count(x) > 1, data))
#     return lst
#
# if __name__ == "__main__":
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
#     assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
#     assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
#     assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
#     print("It is all good. Let's check it now")

# def frequency_sort(items):
#     if len(items) == len(set(items)):
#         return items
#     items1 = sorted(items, reverse=True)
#     items2 = sorted(items1, key=lambda item: items1.count(item), reverse=True)
#     return items2
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
#     assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
#     assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
#     assert list(frequency_sort([])) == []
#     assert list(frequency_sort([1])) == [1]
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# Упорядочить массив по частоте элементов, если кол-во элементов одинаково сохрянить изначальный порядок
# def frequency_sort(items):
#     return sorted(items, key=lambda x: (-items.count(x), items.index(x)))

# if __name__ == '__main__':
#     print("Example:")
#     print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
#     assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
#     assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
#     assert list(frequency_sort([])) == []
#     assert list(frequency_sort([1])) == [1]
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def flat_list(array, lst=None):
#     if lst is None:
#         lst = []
#     for item in array:
#         if type(item) == list:
#             flat_list(item, lst)
#         else:
#             lst.append(item)
#     return lst
#
# print(flat_list([1, 2, 3]))
# print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))

# def long_repeat(line: str) -> int:
#     if line == '':
#         return 0
#     count = 1
#     count2 = 1
#     for i, letter in enumerate(line):
#         if i == len(line) - 1:
#             continue
#         if letter == line[i + 1]:
#             count2 += 1
#         else:
#             count2 = 1
#         if count2 > count:
#             count = count2
#
#     return count
#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert long_repeat('sdsffffse') == 4, "First"
#     assert long_repeat('ddvvrwwwrggg') == 3, "Second"
#     assert long_repeat('abababaab') == 2, "Third"
#     assert long_repeat('') == 0, "Empty"
#     print('"Run" is good. How is "Check"?')

# def sum_numbers(text: str) -> int:
#     arr = text.split(' ')
#     arr = list(filter(str.isdigit, arr ))
#     arr = map(int, arr)
#     return sum(arr)
#
# if __name__ == '__main__':
#     print("Example:")
#     print(sum_numbers('hi'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert sum_numbers('hi') == 0
#     assert sum_numbers('who is 1st here') == 0
#     assert sum_numbers('my numbers is 2') == 2
#     assert sum_numbers('This picture is an oil on canvas '
#  'painting by Danish artist Anna '
#  'Petersen between 1845 and 1910 year') == 3755
#     assert sum_numbers('5 plus 6 is') == 11
#     assert sum_numbers('') == 0
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def split_list(items: list) -> list:
#     arr1 = []
#     arr2 = []
#     if len(items) % 2:
#         arr1 = items[:len(items) // 2 + 1]
#         arr2 = items[len(items) // 2 + 1:]
#     else:
#         arr1 = items[:len(items) // 2]
#         arr2 = items[len(items) // 2:]
#
#     return [arr1, arr2]
#
# def split_list(items: list) -> list:
#     i = len(items)//2 + len(items)%2
#     return items[:i], items[i:]
#
# if __name__ == '__main__':
#     print("Example:")
#     print(split_list([1, 2, 3]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
#     assert split_list([1, 2, 3]) == [[1, 2], [3]]
#     assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
#     assert split_list([1]) == [[1], []]
#     assert split_list([]) == [[], []]
#     print("Coding complete? Click 'Check' to earn cool rewards!")
# import datetime
#
# def days_diff(a, b):
#     one = datetime.datetime(*a)
#     two = datetime.datetime(*b)
#     delta = two - one
#
#     return abs(delta.days)
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(days_diff((1982, 4, 19), (1982, 4, 22)))
#     print(days_diff((2014, 1, 1), (2014, 8, 27)))
#     print(days_diff((2014, 8, 27), (2014, 1, 1)))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
#     assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
#     assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def count_digits(text: str) -> int:
#     return sum((sb.isdigit() for sb in text))
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(count_digits('hi'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert count_digits('hi') == 0
#     assert count_digits('who is 1st here') == 1
#     assert count_digits('my numbers is 2') == 1
#     assert count_digits('This picture is an oil on canvas '
#  'painting by Danish artist Anna '
#  'Petersen between 1845 and 1910 year') == 8
#     assert count_digits('5 plus 6 is') == 2

# def backward_string_by_word(text: str) -> str:
#     arr = text.split(' ')
#     arr = list(map(lambda x: x[::-1], arr))
#     return ' '.join(arr)
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(backward_string_by_word('hello world'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert backward_string_by_word('') == ''
#     assert backward_string_by_word('world') == 'dlrow'
#     assert backward_string_by_word('hello world') == 'olleh dlrow'
#     assert backward_string_by_word('hello   world') == 'olleh   dlrow'
#     assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def find_quotes(a):
#     arr = a.split('"')
#     new_arr = [v for k, v in enumerate(arr) if k % 2]
#     return new_arr
#
# if __name__ == '__main__':
#     print("Example:")
#     print(find_quotes('"Greetings"'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert find_quotes('"Greetings"') == ['Greetings']
#     assert find_quotes('Hi') == []
#     assert find_quotes('good morning mister "superman"') == ['superman']
#     assert find_quotes('"this" doesn\'t make any "sense"') == ['this', 'sense']

# def end_zeros(num: int) -> int:
#     count = 0
#     for letter in str(num)[::-1]:
#         if letter == '0':
#             count+=1
#         else:
#             return count
#     return count
#
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(end_zeros(111101))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert end_zeros(0) == 1
#     assert end_zeros(1) == 0
#     assert end_zeros(10) == 1
#     assert end_zeros(101) == 0
#     assert end_zeros(245) == 0
#     assert end_zeros(100100) == 2
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def is_all_upper_my(text: str) -> bool:
#     text = text.replace(' ', '')
#     if text == '' or text.isdigit() or not text.isalpha() and not text.isdigit():
#         return True
#     return text.isupper()
#
#
# def is_all_upper(text):
#     return all(ch.isupper() for ch in text if ch.isalpha())
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(is_all_upper('ALL UPPER'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_all_upper('ALL UPPER') == True
#     assert is_all_upper('all lower') == False
#     assert is_all_upper('mixed UPPER and lower') == False
#     assert is_all_upper('') == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def split_pairs_my(a):
#     i = 0
#     j = 1
#     arr = []
#     if len(a) % 2:
#         a = a + '_'
#     while j <= len(a)//2:
#         arr.append(a[i:i+2])
#         i+=2
#         j+=1
#     return arr
#
# def split_pairs(a):
#     return [a[i:i+2] if len(a[i:i+2]) == 2 else a[i:i+2] + "_" for i in range(0, len(a), 2)]
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(list(split_pairs('abcdf')))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(split_pairs('abcd')) == ['ab', 'cd']
#     assert list(split_pairs('abc')) == ['ab', 'c_']
#     assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
#     assert list(split_pairs('a')) == ['a_']
#     assert list(split_pairs('')) == []
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def nearest_value(values: set, one: int) -> int:
#     values = sorted(values)
#     x = min(map(lambda item: abs(item-one), values))
#     for item in values:
#         if abs(item-one) == x:
#             return item

# nearest_value=lambda s,v:min(s,key=lambda x:(abs(x-v),x))

# def nearest_value(values: set, one: int) -> int:
#     def distance(value): return abs(value - one), value > one
#     return min(values, key=distance)
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(nearest_value({0, -2}, -1))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
#     assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
#     assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
#     assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
#     assert nearest_value({-1, 2, 3}, 0) == -1
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def safe_pawns(pawns: set) -> int:
#     col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     row = [1, 2, 3, 4, 5, 6, 7, 8]
#     count = 0
#     for item in pawns:
#         x = col.index(item[:1])
#         y = row.index(int(item[1:]))
#         if y != 0:
#             y1 = row[y-1]
#         else:
#             continue
#         if x != 0:
#             x1 = col[x-1]
#         else:
#             x1 = 'n'
#         if x != 7:
#             x2 = col[x+1]
#         else:
#             x2 = 'n'
#         if x1+str(y1) in pawns or x2+str(y1) in pawns:
#             count+=1
#     return count
#
# def safe_pawns(pawns: set) -> int:
#     h_label = '_abcdefgh_'
#     v_label = '_12345678_'
#     safe = 0
#     for k in pawns:
#         r_b = h_label[h_label.find(k[0]) - 1] + v_label[v_label.find(k[1]) - 1]
#         l_b = h_label[h_label.find(k[0]) + 1] + v_label[v_label.find(k[1]) - 1]
#         if r_b in pawns or l_b in pawns:
#             safe += 1
#     return safe

#
# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
#     assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# from datetime import datetime
#
#
# def sun_angle(time):
#     anglePerSecond = 180 / 12 / 60 / 60
#     timeFormat = '%H:%M'
#     dTime = datetime.strptime(time, timeFormat)
#     minTime = datetime.strptime('06:00', timeFormat)
#     maxTime = datetime.strptime('18:00', timeFormat)
#
#     if (dTime >= minTime and dTime <= maxTime):
#         timeDelta = dTime - minTime
#         return (timeDelta.total_seconds() * anglePerSecond)
#
#     return "I don't see the sun!"
#
#
# def sun_angle_MY(time):
#     arr_time = time.split(':')
#     time_in_min = int(arr_time[0])*60 + int(arr_time[1])
#     if time_in_min < 360 or time_in_min > 1080:
#         return "I don't see the sun!"
#     else:
#         return (time_in_min - 360) * 0.25
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(sun_angle("07:00"))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert sun_angle("07:00") == 15
#     assert sun_angle("01:23") == "I don't see the sun!"
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def is_acceptable_password(password: str) -> bool:
#     return (
#         (
#             len(password) > 6
#             and any(map(str.isdigit, password))
#             and not all(map(str.isdigit, password))
#         )
#         or len(password) > 9
#     ) and not "password" in password.lower()


########################################--Check password with library re --#############################################

#
# import re
#
# # pattern = re.compile('(?i)^(?!.*password.*)((?=.*?\d)(?=.*?\D)[ \S]{7,}|[ \S]{10,})$')
#
# pattern = re.compile('''
# ^                  # beginning of string
# (?!.*password.*)   # string not contain the word "password"
# (                  # beginning of group capture
# (?=.*?\d)          # at least one digit
# (?=.*?\D)          # at least one non-digit
# [ \S]              # anything other than a tab or newline
# {7,}               # length should be bigger than 6
# |                  # or
# [ \S]              # anything other than a tab or newline
# {10,}              # length should be bigger than 9
# )                  # end of group capture
# $                  # end of string
# ''', re.VERBOSE | re.IGNORECASE)
#
#
# def is_acceptable_password(password):
#     passwd = pattern.search(password)
#     if passwd:
#         return sum(map(str.isalnum, set(passwd.group(0)))) > 2
#     return False


# def is_acceptable_password(password: str) -> bool:
#     if not password.lower().count('password') and len(set(password)) >= 3:
#         if len(password) > 9:
#             return True
#         else:
#             return len(password) > 6 and any(map(lambda x: x.isdigit(), password)) and any(
#                 ch.isalpha() for ch in password)
#     else:
#         return False


# if __name__ == '__main__':
#     print("Example:")
#     print(is_acceptable_password('short'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('short54') == True
#     assert is_acceptable_password('muchlonger') == True
#     assert is_acceptable_password('ashort') == False
#     assert is_acceptable_password('muchlonger5') == True
#     assert is_acceptable_password('sh5') == False
#     assert is_acceptable_password('1234567') == False
#     assert is_acceptable_password('12345678910') == True
#     assert is_acceptable_password('password12345') == False
#     assert is_acceptable_password('PASSWORD12345') == False
#     assert is_acceptable_password('pass1234word') == True
#     assert is_acceptable_password('aaaaaa1') == False
#     assert is_acceptable_password('aaaaaabbbbb') == False
#     assert is_acceptable_password('aaaaaabb1') == True
#     assert is_acceptable_password('abc1') == False
#     assert is_acceptable_password('abbcc12') == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")

##########################-- end of Check password with library re --#############################################
#
# from typing import Iterable
#
#
# def replace_last(items: list) -> Iterable:
#     if items:
#         items.insert(0, items.pop(-1))
#     return items
#
# def replace_last(items: list) -> Iterable:
#     return [items[-1]] + items[:-1] if items else items

# from typing import List, Tuple
#
# Coords = List[Tuple[int, int]]
#
#
# def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
#     num_vort = 3  # number of vertices of the shape
#     ratio = []
#     def square_len_lines(coords: list):
#
#         arr = []
#         arr_delta_x = []
#         arr_delta_y = []
#         for i in range(num_vort - 1):
#             arr_delta_x.append(coords[i][0] - coords[i + 1][0])
#             # print(coords[i][0] - coords[i + 1][0])
#             arr_delta_y.append(coords[i][1] - coords[i + 1][1])
#             # print(coords[i][1] - coords[i + 1][1])
#         arr_delta_x.append(coords[0][0] - coords[-1][0])
#         # print(coords[0][0] - coords_1[-1][0])
#         arr_delta_y.append(coords[0][1] - coords[-1][1])
#         # print(coords[0][1] - coords[-1][1])
#
#         # print(arr_delta_x)
#         # print(arr_delta_y)
#         for x, y in zip(arr_delta_x, arr_delta_y):
#             arr.append(x ** 2 + y ** 2)
#         return arr
#
#     for x, y in zip(sorted(square_len_lines(coords_1)), sorted(square_len_lines(coords_2))):
#         ratio.append(x/y)
#     return len(set(ratio))==1
#
# # def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
# #     d = lambda x1, y1, x2, y2: (x1 - x2)**2 + (y1 - y2)**2
# #
# #     a1, b1, c1 = coords_1
# #     s1 = sorted([d(*a1, *b1), d(*b1, *c1), d(*c1, *a1)])
# #     a2, b2, c2 = coords_2
# #     s2 = sorted([d(*a2, *b2), d(*b2, *c2), d(*c2, *a2)])
# #     return (s1[0] * s2[2], s1[1] * s2[2]) == (s2[0] * s1[2], s2[1] * s1[2])
#
# if __name__ == '__main__':
#     print("Example:")
#     print(similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]))
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
#     assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
#     assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
#     assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
#     assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
#     assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def foo(x):
#     def too(y):
#         return x*y
#     return too
# print(foo(3)(5))

from typing import List, Iterable

#
# def checkio(data: List[int]) -> [int, float]:
#     data.sort()
#     # print(data)
#     x = len(data)
#     if not x % 2:
#         return (data[x // 2 - 1] + data[x // 2]) / 2
#     return data[x // 2]
#
# # These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     print("Example:")
#     print(checkio([1, 2, 3, 4, 5]))
#     assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
#     assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
#     assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
#     assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
#     print("Start the long test")
#     assert checkio(list(range(1000000))) == 499999.5, "Long."
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def chunking_by(items: list, size: int) -> Iterable:
#     arr = []
#     step = size
#     while len(items) + size > step:
#         arr.append(items[step-size:step])
#         step+=size
#     return arr
#
# def chunking_by(items: list, size: int) -> Iterable:
#     return [items[i:i + size] for i in range(0, len(items), size)]
# #
#
# if __name__ == '__main__':
#     print("Example:")
#     print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))
# #
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
#     assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
#     assert list(chunking_by([5, 4], 7)) == [[5, 4]]
#     assert list(chunking_by([], 3)) == []
#     assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]
#     print("Coding complete? Click 'Check' to earn cool rewards!")


# graph = {'A': ['B', 'C'],
#          'B': ['A', 'D', 'E'],
#          'C': ['A', 'F'],
#          'D': ['B'],
#          'E': ['B', 'F'],
#          'F': ['C', 'E']}
#
# def dfs(graph, start):
#     visited, stack = [], [start]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.append(vertex)
#             stack.extend(set(graph[vertex]) - set(visited))
#     return visited
#
# print(dfs(graph, 'A'))


########################################################## графы
#
# def disconnected_users(net, users, source, crushes):
#     def flat_list(array, lst=None):
#         if lst is None:
#             lst = []
#         for item in array:
#             if type(item) == list:
#                 flat_list(item, lst)
#             else:
#                 lst.append(item)
#         return lst
#     def number_users(s):
#         summ = 0
#         for i in s:
#             summ = summ + users[i]
#         return summ
#
#     s1 = set(flat_list(net))
#     s2 = s1
#     s2.remove(crushes[0])
#     disc_users = number_users(s1) -number_users(s2)
#
#
#     return disc_users
#
# print(disconnected_users([
#         ['A', 'B'],
#         ['B', 'C'],
#         ['C', 'D']
#     ], {
#         'A': 10,
#         'B': 20,
#         'C': 30,
#         'D': 40
#     },
#         'A', ['C']))
#
# print( disconnected_users([
#         ['A', 'B'],
#         ['B', 'D'],
#         ['A', 'C'],
#         ['C', 'D']
#     ], {
#         'A': 10,
#         'B': 0,
#         'C': 0,
#         'D': 40
#     },
#         'A', ['B']))

##########################################################


from typing import Iterable


#
# def except_zero(items: list) -> Iterable:
#     pos_of_zero = []
#     for i, item in enumerate(items):
#         if item == 0:
#             pos_of_zero.append(i)
#     items.sort()
#     items = items[len(pos_of_zero):]
#     for item in pos_of_zero:
#         items.insert(item, 0)
#     return items


# def except_zero(items):
#     res = sorted(i for i in items if i)
#     for i, x in enumerate(items):
#         if not x: res.insert(i, 0)
#     return res
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
#     assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
#     assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
#     assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
#     assert list(except_zero([0, 0])) == [0, 0]
#     print("Coding complete? Click 'Check' to earn cool rewards!")


def frequency_sorting(numbers):
    numbers.sort()
    return sorted(numbers, key=lambda item: numbers.count(item), reverse=True)


# if __name__ == '__main__':
#     print("Example:")
#     print(frequency_sorting([1, 2, 3, 4, 5]))

def add_binary(a, b):
    return bin(int(a + b))[2:]


# print((add_binary(1,2.6)))


def how_deep(structure, i=None):
    s = str(structure)
    count = 0
    max_count = 0
    for ch in s:
        if ch == '(':
            count += 1
        if ch == ')':
            if count > max_count:
                max_count = count
            count -= 1
    return max_count


def how_deep_not_my(structure):
    depth, deepest = 0, 0
    for i in str(structure):
        depth += i.count('(') - i.count(')')
        deepest = max(depth, deepest)
    return deepest


def how_deep_not_my2(structure):
    if isinstance(structure, int):
        return 0
    return 1 + max((how_deep(e) for e in structure), default=0)


# print(how_deep((1, 2, (3,))))
# print(how_deep((1, 2, 3)))
# print(how_deep((1, 2, (3, (4,)))))

from typing import Iterable


def compress(items: list) -> Iterable:
    if not items:
        return items
    new_items = [items[0]]
    for item in items:
        if item != new_items[-1]:
            new_items.append(item)
    return new_items


# print("Example:")
# print(list(compress([
#     5, 5, 5,
#     4, 5, 6,
#     6, 5, 5,
#     7, 8, 0,
#     0])))

def count_inversion(sequence):
    count = 0
    for i, item1 in enumerate(sequence):
        for j, item2 in enumerate(sequence):
            if i < j and sequence[i] > sequence[j]:
                count += 1

    return count


# print(count_inversion([1, 2, 5, 3, 4, 7, 6]));
# # Checkio worior battle 1
#
# class Warrior:
#     health = 50
#     attack = 5
#     is_alive = True
#
#
#
# class Knight(Warrior):
#     attack = 7
#
#
# def fight(unit_1, unit_2):
#     while unit_1.health >=0 and unit_1.health >=0:
#         unit_2.health = unit_2.health - unit_1.attack
#         if unit_2.health <= 0:
#             unit_2.is_alive = False
#             break
#         unit_1.health = unit_1.health - unit_2.attack
#         if unit_1.health <= 0:
#             unit_1.is_alive = False
#             break
#     return unit_1.is_alive


# Checkio worior battle 2

# class Warrior:
#     def __init__(self, health=50, attack=5):
#         self.health = health
#         self.attack = attack
#         self.is_alive = True
#
#
# class Knight(Warrior):
#     def __init__(self, health=50, attack=7):
#         super().__init__(health, attack)
#
#
# class Army:
#     def __init__(self):
#         self.army_value = []
#
#     def add_units(self, units_class, number_of_units):
#         if units_class == Warrior:
#             while number_of_units:
#                 self.army_value.append(Warrior())
#                 number_of_units -= 1
#
#
#         if units_class == Knight:
#             while number_of_units:
#                 self.army_value.append(Knight())
#                 number_of_units -= 1
#
#     def is_alive(self):
#         if self.army_value:
#             return True
#         else:
#             return False
#
#
# class Battle:
#     def __init__(self):
#         pass
#
#     def fight(self, first_army, second_army):
#
#         while first_army.army_value and second_army.army_value:
#             if self.__fight_units(first_army.army_value[0], second_army.army_value[0]):
#                 second_army.army_value.pop(0)
#             else:
#                 first_army.army_value.pop(0)
#         return first_army.is_alive()
#
#     def __fight_units(self, unit_1, unit_2):
#         while True:
#             if unit_2.health > 0:
#                 unit_2.health -= unit_1.attack
#             if unit_2.health <= 0:
#                 unit_2.is_alive = False
#                 break
#             if unit_1.health > 0:
#                 unit_1.health -= unit_2.attack
#             if unit_1.health <= 0:
#                 unit_1.is_alive = False
#                 break
#         return unit_1.is_alive
#
# def fight(unit_1, unit_2):
#     while True:
#         if unit_2.health > 0:
#             unit_2.health -= unit_1.attack
#         if unit_2.health <= 0:
#             unit_2.is_alive = False
#             break
#         if unit_1.health > 0:
#             unit_1.health -= unit_2.attack
#         if unit_1.health <= 0:
#             unit_1.is_alive = False
#             break
#     return unit_1.is_alive


#############################################################
# код как мой только более красивый
#############################################################

# class Warrior:
#     def __init__(self):
#         self.health = 50
#         self.attack = 5
#
#     @property
#     def is_alive(self):
#         return self.health > 0
#
#
# class Knight(Warrior):
#     def __init__(self):
#         super().__init__()
#         self.attack = 7
#
#
# def fight(unit_1, unit_2):
#     round = 1
#     while unit_1.is_alive and unit_2.is_alive:
#         round += 1
#         if round % 2 == 0:
#             unit_2.health -= unit_1.attack
#         else:
#             unit_1.health -= unit_2.attack
#     return unit_1.is_alive
#
#
# class Army():
#     def __init__(self):
#         self.units = []
#
#     def add_units(self, unit, amount):
#         self.units.extend([unit() for i in range(amount)])
#
#
# class Battle():
#     def fight(self, army1, army2):
#         while len(army1.units) > 0 and len(army2.units) > 0:
#             if fight(army1.units[0], army2.units[0]):
#                 army2.units.pop(0)
#             else:
#                 army1.units.pop(0)
#         return len(army1.units) > 0


# Checkio worior battle 3
class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defense = 0

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2

class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 50



def fight(unit_1, unit_2):
    round = 1
    while unit_1.is_alive and unit_2.is_alive:
        round += 1
        if round % 2 == 0:
            if unit_2.defense < unit_1.attack:
                unit_2.health -= unit_1.attack - unit_2.defense
        else:
            if unit_1.defense < unit_2.attack:
                unit_1.health -= unit_2.attack - unit_1.defense
    return unit_1.is_alive


class Army():
    def __init__(self):
        self.units = []

    def add_units(self, unit, amount):
        self.units.extend([unit() for i in range(amount)])

    @property
    def is_alive(self):
        if self.units:
            return True
        else:
            return False


class Battle():
    def fight(self, army1, army2):
        while len(army1.units) > 0 and len(army2.units) > 0:
            if fight(army1.units[0], army2.units[0]):
                army2.units.pop(0)
            else:
                army1.units.pop(0)
        return army1.is_alive


