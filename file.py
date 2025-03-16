#1. Reverse a String

def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))




#2. Count the Number of Vowels in a String

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("hello world"))




#3. Check if a String is a Palindrome

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("python"))




#4. Check if Two Strings are Anagrams

from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

print(is_anagram("listen", "silent"))
print(is_anagram("apple", "pale"))




#5. Find All Occurrences of a Substring

def find_occurrences(string, substring):
    return [i for i in range(len(string)) if string.startswith(substring, i)]

print(find_occurrences("banana", "ana"))




#6. String Compression Using Repeated Character Counts

def compress_string(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    return ''.join(compressed)

print(compress_string("aaabbcccc"))



#7. Check if a String has All Unique Characters

def has_unique_chars(s):
    return len(set(s)) == len(s)

print(has_unique_chars("hello"))
print(has_unique_chars("abcde"))




#8. Convert a String to Uppercase or Lowercase

def convert_case(s, to_upper=True):
    return s.upper() if to_upper else s.lower()

print(convert_case("Hello World", True))
print(convert_case("Hello World", False))




#9. Count the Number of Words in a String

def count_words(s):
    return len(s.split())

print(count_words("Hello world this is Python"))




#10. Concatenate Two Strings Without Using + Operator

def concatenate_strings(str1, str2):
    return "{}{}".format(str1, str2)

print(concatenate_strings("Hello", "World"))




#11. Remove All Occurrences of a Specific Element from a List

def remove_element(lst, target):
    return [x for x in lst if x != target]

print(remove_element([1, 2, 3, 4, 2, 2, 5], 2))




#12. Find the Second Largest Number in a List

def second_largest(lst):
    unique_nums = list(set(lst))
    unique_nums.sort()
    return unique_nums[-2]

print(second_largest([10, 20, 4, 45, 99]))




#13. Count Occurrences of Each Element in a List

from collections import Counter

def count_elements(lst):
    return dict(Counter(lst))

print(count_elements([1, 2, 2, 3, 3, 3, 4]))




#14. Reverse a List In-Place

def reverse_list(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[-i-1] = lst[-i-1], lst[i]
    return lst

print(reverse_list([1, 2, 3, 4, 5]))




#15. Remove Duplicates While Preserving Order

def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print(remove_duplicates([1, 2, 2, 3, 4, 3, 5]))




#16. Check if a List is Sorted

def is_sorted(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

print(is_sorted([1, 2, 3, 4]))
print(is_sorted([4, 3, 2, 1]))
print(is_sorted([3, 2, 5, 1]))






#18. Find Intersection of Two Lists

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))


#19. Find Union of Two Lists Without Duplicates

def union(lst1, lst2):
    return list(set(lst1) | set(lst2))

print(union([1, 2, 3], [3, 4, 5]))




#20. Shuffle a List Randomly Without Using shuffle()

import random

def shuffle_list(lst):
    for i in range(len(lst)):
        j = random.randint(0, len(lst)-1)
        lst[i], lst[j] = lst[j], lst[i]
    return lst

print(shuffle_list([1, 2, 3, 4, 5]))




#21. Elements in First Set but Not in Second Set

def elements_not_in_second(set1, set2):
    return set1 - set2

print(elements_not_in_second({1, 2, 3}, {2, 3, 4}))




#22. Tuple Slicing Between Indices

def tuple_slice(tup, start, end):
    return tup[start:end]

print(tuple_slice((1, 2, 3, 4, 5), 1, 4))




#23. Union, Intersection, and Difference of Two Sets

def set_operations(set1, set2):
    return set1 | set2, set1 & set2, set1 - set2

print(set_operations({1, 2, 3}, {3, 4, 5}))




#24. Maximum and Minimum Values from a Tuple

def max_min_tuple(tup):
    return max(tup), min(tup)

print(max_min_tuple((3, 5, 1, 8, 2)))




#25. Count Element Occurrences in a Tuple

def count_element(tup, element):
    return tup.count(element)

print(count_element((1, 2, 2, 3, 4, 2), 2))




#26. Symmetric Difference of Two Sets

def symmetric_difference(set1, set2):
    return set1 ^ set2

print(symmetric_difference({1, 2, 3}, {3, 4, 5}))




#27. Word Frequency Dictionary

from collections import Counter

def word_frequency(words):
    return dict(Counter(words))

print(word_frequency(["apple", "banana", "apple", "orange", "banana"]))




#28. Merge Two Dictionaries (Sum Common Values)

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value
    return merged

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))




#29. Access Value in Nested Dictionary

def access_nested_value(d, keys):
    for key in keys:
        d = d.get(key)
        if d is None:
            return None
    return d

nested_dict = {'a': {'b': {'c': 42}}}
print(access_nested_value(nested_dict, ['a', 'b', 'c']))




#30. Invert a Dictionary

def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted.setdefault(value, []).append(key)
    return inverted

print(invert_dict({'a': 1, 'b': 2, 'c': 1}))





